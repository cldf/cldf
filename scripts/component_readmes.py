import json
import pathlib

from pycldf.terms import TERMS
from csvw.metadata import Table


def colrow(col, pk):
    dt = '`{}`'.format(col.datatype.base if col.datatype else 'string')
    if col.separator:
        dt = 'list of {} (separated by `{}`)'.format(dt, col.separator)
    desc = col.common_props.get('dc:description', '').replace('\n', ' ')

    pk = pk or []
    if col.name in pk:
        desc = (desc + '<br>') if desc else desc
        desc += 'Primary key'

    if col.propertyUrl:
        term = TERMS.by_uri.get(col.propertyUrl.uri)
        if term and term.references:
            desc = (desc + '<br>') if desc else desc
            desc += 'References {}'.format(term.references)

    return ' | '.join([
        '[{}]({})'.format(col.name, col.propertyUrl)
        if col.propertyUrl else '`{}`'.format(col.name),
        dt,
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
    res.append('Name/Property | Datatype | Description')
    res.append(' --- | --- | --- ')
    for col in table.tableSchema.columns:
        res.append(colrow(col, table.tableSchema.primaryKey))
    return '\n'.join(res)


if __name__ == '__main__':
    for p in pathlib.Path(__file__).parent.parent.resolve().joinpath('components').glob('*/*.json'):
        readme = p.parent.joinpath('description.md').read_text(encoding='utf8')
        cols = table2markdown(Table.fromvalue(json.loads(p.read_text(encoding='utf8'))))
        p.parent.joinpath('README.md').write_text(readme + '\n' + cols, encoding='utf8')
