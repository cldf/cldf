## Language Metadata

If a CLDF dataset provides language metadata which goes beyond what could be
retrieved from a catalog like [Glottolog](http://glottolog.org), it must
include a data file `languages.csv` or a table with `"dc:type": "cldf:languages"`.

Any column named `Language_ID` in any of the other data files will then be
interpreted as foreign key referencing an `ID` in the languages file. Thus,
if a dataset provides metadata for at least one language it must list all its
languages in the languages file.
