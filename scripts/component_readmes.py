import re
import json
import pathlib
from xml.etree import ElementTree

from pycldf.terms import TERMS
from csvw.metadata import Table


def get_comment(t):
    c = t.element.find("{http://www.w3.org/2000/01/rdf-schema#}comment")
    try:
        xml = ElementTree.tostring(c, default_namespace='http://www.w3.org/1999/xhtml')
    except ValueError:
        xml = ElementTree.tostring(c)

    res = re.sub(
        r'ns[0-9]+:comment(\s[^>]+)?',
        'div',
        xml.decode('utf8')
    ).replace('\n', ' ').replace('<html:', '<').replace('</html:', '</')
    return re.sub('\s+', ' ', res)


def cardinality(col, term):
    res = None
    if term:
        # Make sure, cardinality is consistent with the ontology:
        tcol = term.to_column()
        try:
            res = term.element.find("{http://purl.org/dc/terms/}extent").text
        except:
            res = None
        assert (res == 'multivalued' and tcol.separator) or \
               (res == 'singlevalued' and not tcol.separator) or \
               (res is None), 'y'
        assert bool(col.separator) == bool(tcol.separator), 'x'

    # Make sure, cardinality is consistent with separator spec:
    card = col.common_props.get('dc:extent')
    assert (card == 'multivalued' and col.separator) or \
           (card == 'singlevalued' and not col.separator) or \
           (card is None), 'z'
    return res or card or 'unspecified'


def colrow(col, pk):
    dt = '`{}`'.format(col.datatype.base if col.datatype else 'string')
    if col.separator:
        dt = 'list of {} (separated by `{}`)'.format(dt, col.separator)
    desc = col.common_props.get('dc:description', '').replace('\n', ' ')
    term = None
    if col.propertyUrl:
        term = TERMS.by_uri.get(col.propertyUrl.uri)
    card = cardinality(col, term)
    if (not desc) and term:
        desc = get_comment(term)

    pk = pk or []
    if col.name in pk:
        desc = (desc + '<br>') if desc else desc
        desc += 'Primary key'

    if term and term.references:
        desc = (desc + '<br>') if desc else desc
        desc += 'References {}'.format(term.references)

    return ' | '.join([
        '[{}]({})'.format(col.name, col.propertyUrl)
        if col.propertyUrl else '`{}`'.format(col.name),
        dt,
        card,
        desc,
    ])


def table2markdown(table):
    res = []
    res.append('## [{}]({}): `{}`\n'.format(
        table.common_props['dc:conformsTo'].split('#')[1],
        table.common_props['dc:conformsTo'],
        table.url.string,
    ))
    if table.common_props.get('dc:description'):
        res.append(table.common_props['dc:description'] + '\n')
    res.append('Name/Property | Datatype | Cardinality | Description')
    res.append(' --- | --- | --- | --- ')
    for col in table.tableSchema.columns:
        res.append(colrow(col, table.tableSchema.primaryKey))
    return '\n'.join(res)


if __name__ == '__main__':
    for p in pathlib.Path(__file__).parent.parent.resolve().joinpath('components').glob('*/*.json'):
        readme = p.parent.joinpath('description.md').read_text(encoding='utf8')
        cols = table2markdown(Table.fromvalue(json.loads(p.read_text(encoding='utf8'))))
        p.parent.joinpath('README.md').write_text(readme + '\n' + cols, encoding='utf8')
