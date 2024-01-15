# Language Metadata

If a CLDF dataset provides language metadata which goes beyond what could be
retrieved from a catalog like [Glottolog](https://glottolog.org), it must
include a data file `languages.csv` or a table with common property 
`"dc:conformsTo": "http://cldf.clld.org/v1.0/terms.rdf#LanguageTable"`.

Rows in the language table can then be referenced from other tables using a
[`languageReference`](http://cldf.clld.org/v1.0/terms.rdf#languageReference) property.


## What's a language?

For the purposes of CLDF, a language is one of the objects whose attributes are described in a dataset.
Thus, if a dataset contains the results of a sociolinguistic study, rows in `LanguageTable` will
likely be sociolects. Whether and how such rows are related to languoids as understood for example by 
Glottolog can be indicated in the [Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) column.

See also the related discussion in https://github.com/cldf/cldf/issues/68

### Dialects

If a dataset contains data about dialects, it is recommended to add a [`parentLanguageGlottocode`](http://cldf.clld.org/v1.0/terms.rdf#parentLanguageGlottocode)
property
- to provide a stable reference to Glottolog,
- to indicate the language-level object which might be used to compare data across datasets.


## Example

See https://github.com/cldf-datasets/wals/blob/master/cldf/languages.csv

```csv
ID,Name,Macroarea,Latitude,Longitude,Glottocode,ISO639P3code,Family,Subfamily,Genus,GenusIcon,ISO_codes,Samples_100,Samples_200,Country_ID,Source
aab,Arapesh (Abu),,-3.45,142.95,,,Torricelli,,Kombio-Arapesh,c0000dd,,false,false,PG,Nekitel-1985
aar,Aari,Africa,6,36.5833333333,aari1239,aiw,Afro-Asiatic,Omotic,South Omotic,ccccccc,aiw,false,false,ET,Hayward-1990a
aba,Abau,Papunesia,-4,141.25,abau1245,aau,Sepik,,Upper Sepik,ddd0000,aau,false,false,PG,Bailey-1975
...
```