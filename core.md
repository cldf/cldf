## Core format specification

### Data files

A CLDF dataset is a set of CSV files.
The exact set of required data files varies per [module](README.md#modules).

The following list of column names (either specified in the CSV files or as `name` property of a column's metadata) is recognized by CLDF:

- `ID`: identifies a row in the data file; either a local ID - preferably an [UUID](http://en.wikipedia.org/wiki/Universally_unique_identifier) - or an (equally universally unique) URL like http://wold.clld.org/word/7214142329897819 or http://wals.info/valuesets/1A-niv
- `Language_ID`: identifies the language or variety the data in the row is about.
- `Source`: Semicolon-separated source specifications, of the form *<source_ID>[<source context>]*, e.g. *http://glottolog.org/resource/reference/id/318814[34]*, or *meier2015[3-12]* where *meier2015* is a citation key in the accompanying BibTeX file.
- `Example_ID`: Semicolon-separated example IDs.
- `Comment`: Free text comment.

Note: CLDF datasets with a metadata file may override the separator used for
lists in `Source` or `Example_ID` values.

If the dataset contains a [languages component](components/languages/), values for `Language_ID` will be interpreted as foreign keys
referencing rows in this component.


#### CSV dialect for metadata-free conformance

In case of metadata-free conformance, these files must follow
[RFC4180](http://tools.ietf.org/html/rfc4180) using the [UTF-8](http://en.wikipedia.org/wiki/UTF-8) character encoding,
i.e. use the CSV dialect specified by
```python
{
  "encoding": "utf-8",
  "lineTerminators": ["\r\n", "\n"],
  "quoteChar": "\"",
  "doubleQuote": true,
  "skipRows": 0,
  "header": true,
  "headerRowCount": 1,
  "delimiter": ",",
  "skipColumns": 0,
  "skipBlankRows": false,
  "skipInitialSpace": false,
  "trim": false
}
```

Notes:
- The first line of each file must contain the comma-separated list of column
  names.
- No comment lines are allowed.


#### CSV dialect for extended conformance

In case of extended conformance, a custom dialect description (possibly per
table) can be used. In particular,
- files may contain comment lines (if appropriately prefixed with 
  [`commentPrefix`](http://w3c.github.io/csvw/metadata/#dialect-commentPrefix)),
- files may omit a header line (if appropriately indicated by `"header": false`).


#### Compatibility

- Using UTF-8 as character encoding means editing these files with MS Excel is not completely trivial, because Excel assumes cp1252 as default character encoding - Libre Office Calc on the other hand handles these files just fine.
- The tool support for csv files is getting better and better due to the hype around "data science". Some particularly useful tools are
  - [csvkit](https://csvkit.readthedocs.org/en/stable/)
  - [q - Text as Data](http://harelba.github.io/q/)


### Metadata file

A CLDF dataset may be described with metadata provided as JSON file following the [Metadata Vocabulary for Tabular Data](https://www.w3.org/TR/tabular-metadata/), 
If a metadata file is present, it must be derived from the default profile for
the appropriate module.

In particular, to make tooling simpler, we restrict the metadata specification as follows:
- Metadata files must specify a `tables` property on top-level, i.e. must describe a [`TableGroup`](http://w3c.github.io/csvw/metadata/#table-groups). While this adds a bit of verbosity to the metadata description, it makes it possible to describe mutiple tables in one metadata file.
- The common property `dc:format` of the `TableGroup` is used to indicate the
  minimal required CLDF version, e.g. `"dc:format": "cldf:v1.0"`
- The common property `dc:type` of the `TableGroup` is used to indicate the
  CLDF module, e.g. `"dc:format": "cldf:wordlist"`
- The common property `dc:type` of a `Table` is used to associate tables with
  a particular role in a CLDF module; i.e. it should be reserved for this use,
  although recognized values for CLDF purposes will always be prefixed with `cldf:`.
- If each row in the data file corresponds to a resource on the web, the `tableSchema` property should provide an `aboutUrl` property.
- If individual cells in a row correspond to resources on the web, the corresponding column specification should provide a `valueUrl` property.

Each dataset should provide a dataset distribution description using the 
[DCAT vocabulary](http://www.w3.org/TR/vocab-dcat/#class-distribution). This will make it easy to  
[catalog](http://www.w3.org/TR/vocab-dcat/#class-catalog) cross-linguistic datasets.
In particular, each dataset description should include properties
- `dc:bibliographicCitation` and
- `dc:license`.

Thus, an example for a CLDF dataset description could look as follows:
```python
{
  "@context": "http://www.w3.org/ns/csvw",
  "dc:format": "cldf:v1.0",
  "dc:type": "cldf:structure-dataset",
  "dc:title": "The Dataset",
  "dc:bibliographicCitation": "Cite me like this!",
  "dc:license": "http://creativecommons.org/licenses/by/4.0/",
  "tables": [
    {
      "url": "ds1.csv",
      "dc:type": "cldf:values",
      "tableSchema": {
        "columns": [
          {
            "name": "ID",
            "datatype": "string"
          },
          {
            "name": "Language_ID",
            "datatype": "string",
            "valueUrl": "http://glottolog.org/resource/languoid/id/{Language_ID}"
          },
          {
            "name": "Parameter_ID",
            "datatype": "string"
          },
          {
            "name": "Value",
            "datatype": "string"
          },
          {
            "name": "Comment",
            "datatype": "string"
          },
          {
            "name": "Source",
            "datatype": "string"
          }
        ],
        "aboutUrl": "http://example.org/valuesets/{ID}",
        "primaryKey": "ID"
      }
    }
  ]
}
```


### Sources file

Sources - if not referenced by Glottolog ID - can be supplied by a CLDF dataset  as BibTeX file (with the citation keys serving as local Source IDs).
The filename of this BibTeX file must be 
- `sources.bib` in case of metadata-free conformance
- or specified as top-level common property `dc:source` in the dataset's metadata.


### Identifiers

Following our design goal to reference rather than duplicate entities, identifiers should be used to reference existing entities (e.g. Glottolog languages, WALS features, etc.). To do so, identifiers 
- must be formatted as resolvable HTTP(S) URLs in case of metadata-free conformance
- or the associated column description in the metadata must specify an 
  appropriate `valueUrl` property, to expand the identifier to a HTTP URL.

Alternatively, identifiers may be used to reference dataset local entities which are defined in the datasets metadata (or not at all). In this case identiers must be composed of the characters defined by the regular expression `[a-zA-Z0-9\-_]`. This restriction makes sure that these identifiers can be used as path components of HTTP URLs (see [rfc3986](https://tools.ietf.org/html/rfc3986#section-2.3)).
