# Media resources

Often, cross-linguistic data is created by analyzing primary data like audio recordings,
or using media such as elicitation stimuli. In such cases it is useful to include this
information in the CLDF dataset. Since actual media data is typically not suitable for
inclusion in tabular data formats like CSV, CLDF specifies a scheme to reference media
via URL and media type.


## URLs

Specification of URLs to access the media files is quite flexible:
- Small amounts of media data may be included in a
  MediaTable directly storing a [data URI](https://en.wikipedia.org/wiki/Data_URI_scheme) as value
  of [Download_URL](http://cldf.clld.org/v1.0/terms.rdf#downloadUrl).
- It is also possible to package media files with the CLDF data and reference the files
  using relative [file URIs](https://en.wikipedia.org/wiki/File_URI_scheme) as value of
  [Download_URL](http://cldf.clld.org/v1.0/terms.rdf#downloadUrl).
- If all media files are available from the same location, e.g. a file server, specifying
  the full URL for each item may unneccesarily inflate the dataset size. In this case,
  a `valueUrl` property on the MediaTable's `id` column can be used that specifies the
  URL template.

Thus, CLDF consumers MUST determine a media item's URL as follows:
1. If MediaTable contains a column with `propertyUrl` http://www.w3.org/ns/dcat#downloadUrl its value is the URL.
2. Otherwise, expand the URI template given as `valueUrl` for the `id` column for the item.

Note that dereferencing (aka downloading) a representation of the URL (i.e. the file content) MUST be done in a way
that can handle HTTP URL **as well as** `file://` and `data://` URLs.


## Linking media items

Which objects in a CLDF dataset are linked to media resources can vary. E.g. in 
[APiCS Online](https://apics-online.info/)
each language contribution provides a PDF version and an audio recording of a glossed
text; in the [Vanuatu Voices](https://vanuatuvoices.clld.org/) dataset, each form is linked to an audio recording.
Thus, for APiCS one would add a column with `propertyURL` 
`http://cldf.clld.org/v1.0/terms.rdf#mediaReference`
to the `ContributionTable`, for Vanuatu Voices it would be added to the `FormTable`. Also,
since audio recordings in Vanuatu Voices are provided in multiple media types, this
reference could be made list-valued, thus short cutting the need for an association table.


## [MediaTable](http://cldf.clld.org/v1.0/terms.rdf#MediaTable): `media.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | unspecified | <div> <p>A title, name or label for an entity.</p> </div> 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | unspecified | <div> <p>A description for an entity.</p> </div> 
[Media_Type](http://cldf.clld.org/v1.0/terms.rdf#mediaType) | `string` | unspecified | <div> <p>A media type (also known as a Multipurpose Internet Mail Extensions or MIME type) as defined by <a href="https://tools.ietf.org/html/rfc6838">IETF's RFC 6838</a>.</p> </div> 
[Download_URL](http://cldf.clld.org/v1.0/terms.rdf#downloadUrl) | `anyURI` | unspecified | <div> <p>URL where a media resource is available directly, typically through HTTP, but other schemes such as <a href="https://en.wikipedia.org/wiki/File_URI_scheme">file:</a> (interpreted relative to the metadata location) or <a href="https://en.wikipedia.org/wiki/Data_URI_scheme">data:</a> are permissible as well. </p> </div> 