# Language Metadata

If a CLDF dataset provides language metadata which goes beyond what could be
retrieved from a catalog like [Glottolog](http://glottolog.org), it must
include a data file `languages.csv` or a table with `"dc:conformsTo": "http://cldf.clld.org/v1.0/terms.rdf#LanguageTable"`.

Rows in the language table can then be referenced from other tables using a
[`languageReference`](http://cldf.clld.org/v1.0/terms.rdf#languageReference) property.
