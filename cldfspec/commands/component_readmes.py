"""
Create the component-specific README files by concatenating `description.md` and
a generated description of the metadata.
"""
import re
import json
from xml.etree import ElementTree

from pycldf.terms import Terms
from csvw.metadata import Table
from cldfspec.util import REPO_DIR


def run(args):
    for p in REPO_DIR.joinpath('components').glob('*/*.json'):
        readme = p.parent.joinpath('description.md').read_text(encoding='utf8')
        cols = table2markdown(Table.fromvalue(json.loads(p.read_text(encoding='utf8'))))
        p.parent.joinpath('README.md').write_text(readme + '\n' + cols, encoding='utf8')


def cardinality(col, term):
    #
    # FIXME: move to pycldf
    #
    res = None
    if term:
        # Make sure, cardinality is consistent with the ontology:
        tcol = term.to_column()
        res = term.cardinality
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


def colrow(col, pk, TERMS):
    dt = '`{}`'.format(col.datatype.base if col.datatype else 'string')
    if col.separator:
        dt = 'list of {} (separated by `{}`)'.format(dt, col.separator)
    desc = col.common_props.get('dc:description', '').replace('\n', ' ')
    term = None
    if col.propertyUrl:
        term = TERMS.by_uri.get(col.propertyUrl.uri)
    card = cardinality(col, term)
    if (not desc) and term:
        desc = term.comment(one_line=True)

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
    TERMS = Terms(REPO_DIR / 'terms.rdf')
    for col in table.tableSchema.columns:
        res.append(colrow(col, table.tableSchema.primaryKey, TERMS))
    return '\n'.join(res)
