# Media resources

Often, cross-linguistic data is created by analyzing primary data like audio recordings,
or using media like elcitation stimuli. In such cases it is useful if to include this
information in the CLDF dataset. Since actual media data is typically not suitable for
inclusion in tabular data formats like CSV, CLDF specifies a scheme to reference media
via URL and media type.


## URLs

Specification of URLs to access the media files is quite flexible:
- Smallish amounts of media data may be included in a
  MediaTable using the [data URI scheme](https://en.wikipedia.org/wiki/Data_URI_scheme).
- It is also possible to package media files with the CLDF data and reference the files
  using relative [file URIs](https://en.wikipedia.org/wiki/File_URI_scheme).
- If all media files are available from the same location, e.g. a file server, specifying
  the full URL for each item may unneccesarily inflate the dataset size. In this case,
  a `valueUrl` property on the MediaTable's `id` column can be used. I.e. CLDF consumers
  **must** determine a media item's URL by looking for a column with `propertyUrl` 
  http://www.w3.org/ns/dcat#downloadUrl first, and if none is found, expand the
  URI template given as `valueUrl` for the `id` column for the item.


## Linking media items

Which objects in a CLDF dataset are linked to media resources can vary. E.g. in APiCS
each language contribution provides a PDF version and an audio recording of a glossed
text; in the Vanuatu Voices dataset, each form is linked to an audio recording.
Thus, for APiCS one would add a column with `propertyURL` 
http://cldf.clld.org/v1.0/terms.rdf#mediaReference
to the ContributionTable, for VanuatuVoices it would be added to the FormTable. Also,
since audio recordings in Vanuatu Voices are provided in multiple media types, this
reference could be made list-valued, thus short cutting the need for an association table.

## [MediaTable](http://cldf.clld.org/v1.0/terms.rdf#MediaTable): `media.csv`

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | 
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Media_Type](http://www.w3.org/ns/dcat#mediaType) | `string` | 
[URL](http://www.w3.org/ns/dcat#downloadUrl) | `anyURI` | 