from clldutils.csvw.metadata import TableGroup
tg = TableGroup.from_file('example.tsv-metadata.json')
for item in tg.tables[0]:
    print(item)
