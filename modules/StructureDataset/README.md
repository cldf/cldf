## Structure Dataset

Structure datasets are lists of values measured/coded/determined for a language and a (often typological) feature.
Typical examples are WALS datasets, e.g. the 
[list of coded values for the language Abau](http://wals.info/languoid/lect/wals_code_aba).

In CLDF structure datasets are marked by a common property `dc:conformsTo` with value
[`http://cldf.clld.org/v1.0/terms.rdf#StructureDataset`](http://cldf.clld.org/v1.0/terms.rdf#StructureDataset)
on a `TableGroup`.

Structure datasets require only a [`ValueTable`](../../components/values), but often
additional information about
- [languages](../../components/languages),
- [parameters](../../components/parameters) (aka features)
- [codes](../../components/codes) (aka feature values)

or [examples](../../components/examples), illustrating particular codings are added.
