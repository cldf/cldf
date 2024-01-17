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


## Speaker area

Datasets may provide information about speaker areas of the languages they describe, i.e. the geographic
areas where the speakers of the respective languages live.

In this case, `LanguageTable` SHOULD contain a [`speakerArea`](http://cldf.clld.org/v1.0/terms.rdf#speakerArea)
property, pointing to a media resource in `MediaTable`.
The linked media resource may be an image of a map, depicting the area, or some other multimedia content 
for human consumption. But it may also be a [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) resource
(i.e. a media resource with `mediaType` `application/geo+json`). In the latter case:

1. If the GeoJSON object is of `type` `FeatureCollection` it MUST 
   contain a [feature](https://datatracker.ietf.org/doc/html/rfc7946#section-3.2) with a [geometry](https://datatracker.ietf.org/doc/html/rfc7946#section-3.1) 
   of type `Polygon` or `Multipolygon` and a key `cldf:languageReference` in its `properties` object with the 
   linking language's `id` as value.
2. If the GeoJSON object is of `type` `Feature` it MUST be of [geometry](https://datatracker.ietf.org/doc/html/rfc7946#section-3.1) 
   `Polygon` or `Multipolygon`.


## Example

Metadata about the languoids listed in [Glottolog](https://glottolog.org) is available in the
`LanguageTable` of the [Glottolog CLDF dataset](https://zenodo.org/doi/10.5281/zenodo.3260727).
This table is described here: https://github.com/glottolog/glottolog-cldf/blob/v4.8/cldf/cldf-metadata.json#L275-L402

> [!NOTE]
> The `Family_ID` column in this table is a so-called "self-referencing foreign key", i.e. a foreign key
> that references the same table.

## [LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable): `languages.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | unspecified | <div> <p>A title, name or label for an entity.</p> </div> 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | unspecified | <div> <p>The name of a macroarea as defined by <a href="http://glottolog.org">Glottolog</a>.</p> </div> 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | unspecified | <div> <p> A latitude in the <a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a> standard coordinate system, specified as decimal number of degrees. </p> </div> 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | unspecified | <div> <p> A longitude in the <a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a> standard coordinate system, specified as decimal number of degrees. </p> </div> 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | unspecified | <div> <p>A Glottocode denoting a languoid described in <a href="http://glottolog.org">Glottolog</a>.</p> </div> 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | unspecified | <div> An ISO 639-3 language code, i.e. a three-letter code denoting a valid ISO 639-3 language or macrolanguage. </div> 