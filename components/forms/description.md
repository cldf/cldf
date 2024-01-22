# Forms

Forms, i.e. written denotations of the linguistic sign (cf. [GOLD's FormUnit](http://linguistics-ontology.org/gold/2010/FormUnit)), are stored in a
`FormTable` in CLDF datasets (typically `Wordlist`s).

Each form is stored as a separate row in this table.
Some analyses, e.g. alignments, require segmented lexical forms. 
If these can be supplied, they should be added in a [Segments](http://cldf.clld.org/v1.0/terms.rdf#segments) column, by default as space-separated strings.

The CLDF Ontology provides some more properties which may be supplied in corresponding columns of the `FormTable`:
- [`motivationStructure`](http://cldf.clld.org/v1.0/terms.rdf#motivationStructure)
- [`prosodicStructure`](http://cldf.clld.org/v1.0/terms.rdf#prosodicStructure)
- [`root`](http://cldf.clld.org/v1.0/terms.rdf#root)
- [`stem`](http://cldf.clld.org/v1.0/terms.rdf#stem)

A [`value`](http://cldf.clld.org/v1.0/terms.rdf#value) column may be used to supply the raw value as it can be found in the source - if this is different
from `Form`. This is particularly useful for "retro-digitized" datasets, where
the CLDF dataset is already the result of data clean-up.

As with any CLDF component, 
- comments and references to sources can be added via
[`comment`](http://cldf.clld.org/v1.0/terms.rdf#comment) and [`source`](http://cldf.clld.org/v1.0/terms.rdf#source) columns respectively,
- additional data can be supplied in additional columns.


## Example

Many examples for `FormTable` can be found in the datasets in the [lexibank community](https://zenodo.org/communities/lexibank).

The one for the [Intercontinental Dictionary Series](https://ids.clld.org) is described here:
https://github.com/intercontinental-dictionary-series/ids/blob/v4.3/cldf/cldf-metadata.json#L59-L171
Datasets created using the lexibank workflow (implemented in the [`pylexibank` package](https://pypi.org/project/pylexibank/))
derive the segmentation of a form using orthography profiles (see [Moran and Cysouw 2018](https://doi.org/10.5281/zenodo.129678))
and the name of the profile used for a particular form is kept in the custom (non-CLDF) `profile`
column.
