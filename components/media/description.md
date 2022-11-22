# Media resources

Often, cross-linguistic data is created by analyzing primary data like audio recordings,
or using media such as elicitation stimuli. In such cases it is useful to include this
information in the CLDF dataset. Since actual media data is typically not suitable for
inclusion in tabular data formats like CSV, CLDF specifies a scheme to reference media
via [URL](https://en.wikipedia.org/wiki/URL) and [media type](https://en.wikipedia.org/wiki/Media_type).


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
that can handle HTTP URLs **as well as** [`file://`](https://en.wikipedia.org/wiki/File_URI_scheme) and
[`data://`](https://en.wikipedia.org/wiki/Data_URI_scheme) URLs.

If a `MediaTable` contains a [Path_In_Zip](http://cldf.clld.org/v1.0/terms.rdf#pathInZip) column and
the value of a media item for this column is non-empty,
- the URL MUST locate the containing Zip file,
- the content retrieved when downloading the URL MUST be treated as Zip archive (i.e. as having media type `application/zip`) and
- the value of the [Media_Type](http://cldf.clld.org/v1.0/terms.rdf#mediaType) column is understood as media type of the contained file.


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
