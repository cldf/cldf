# Language Metadata

If a CLDF dataset provides language metadata which goes beyond what could be
retrieved from a catalog like [Glottolog](http://glottolog.org), it must
include a data file `languages.csv` or a table with `"dc:conformsTo": "http://cldf.clld.org/v1.0/terms.rdf#LanguageTable"`.

Rows in the language table can then be referenced from other tables using a
[`languageReference`](http://cldf.clld.org/v1.0/terms.rdf#languageReference) property.

## [LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable): `languages.csv`

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | 
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 