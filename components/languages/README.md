# Language Metadata

If a CLDF dataset provides language metadata which goes beyond what could be
retrieved from a catalog like [Glottolog](http://glottolog.org), it must
include a data file `languages.csv` or a table with `"dc:conformsTo": "http://cldf.clld.org/v1.0/terms.rdf#LanguageTable"`.

Rows in the language table can then be referenced from other tables using a
[`languageReference`](http://cldf.clld.org/v1.0/terms.rdf#languageReference) property.

## [LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable): `languages.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | unspecified | <div> <p>A title, name or label for an entity.</p> </div> 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | unspecified | <div> <p>A macroarea as defined by <a href="http://glottolog.org">Glottolog</a>.</p> </div> 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | unspecified | <div> <p> A latitude in the <a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a> standard coordinate system, specified as decimal number of degrees. </p> </div> 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | unspecified | <div> <p> A longitude in the <a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a> standard coordinate system, specified as decimal number of degrees. </p> </div> 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | unspecified | <div> <p>A <a href="http://glottolog.org">Glottolog</a> code denoting a languoid.</p> </div> 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | unspecified | <div> An ISO 639-3 language code, i.e. a three-letter code denoting a valid ISO 639-3 language or macrolanguage. </div> 