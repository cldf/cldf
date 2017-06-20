# Cross-linguistic Data Formats

## Why?

To allow exchange of cross-linguistic data and [decouple development of tools and methods from that of databases](bigger_picture.md), standardized data formats are necessary.

Once established, these dataformats could become a foundation not only for tools but also for instruction material in the spirit of [Data Carpentry](http://datacarpentry.org/) for historical linguistics and linguistic typology.


## What?

The main types of cross-linguistic data we are concerned with here are any mostly tabular data which is typically
analysed using quantitative (automated) methods or visualised using software tools, such as
- wordlists (or more complex lexical data including e.g. cognate judgements),
- structure datasets (e.g. [WALS features](http://wals.info/feature)),
- simple dictionaries.


## Design principles

- Data should be both editable "by hand" and amenable to reading and writing by software.
- Data should be encoded as UTF-8 text files.
- Reference entities rather than duplicate.
- IDs should be resolvable HTTP URLs if possible. If not, they should be documented in the metadata.
- Compatibility with existing tools, standards and practice should alsways be kept in mind.


## Core format specification

A cross-linguistic dataset is encoded in the following set of files:

- The core data file, encoded in csv, 
- additional metadata provided as JSON file following the guidelines of the [Model for Tabular Data and Metadata on the Web](http://www.w3.org/TR/tabular-data-model/#standard-file-metadata), 
- sources - if not referenced by Glottolog ID - supplied as BibTeX file (with the citation keys serving as local Source IDs).
- Examples - if not referenced - may be supplied as [*cldf* IGT](igt.md) file.

If the name of the dataset is `clds`, the respective filenames are
- `clds.csv`
- `clds.csv-metadata.json`
- `clds.bib`
- `clds.igt.csv`

Additional tabular data, e.g. cognate judgements accompanying a wordlist, can be tied in using additional table descriptions in the metadata file.


### Identifiers

Following our design goal to reference rather than duplicate entities, identifiers should be used to reference existing entities (e.g. Glottolog languages, WALS features, etc.). To do so, identifiers must be formatted as resolvable HTTP(S) URLs.

Alternatively, identifiers may be used to reference dataset local entities which are defined in the datasets metadata (or not at all). In this case identiers must be composed of the characters defined by the regular expression `[a-zA-Z0-9\-_]`. This restriction makes sure that these identifiers can be used as path components of HTTP URLs (see [rfc3986](https://tools.ietf.org/html/rfc3986#section-2.3)).

Issues: #3


### The data file

The core data file is encoded in [csv](http://tools.ietf.org/html/rfc4180) using the [UTF-8](http://en.wikipedia.org/wiki/UTF-8) character encoding. This file must have a header, i.e. the first row
must contain the list of column names. While the file may contain any number of columns, columns with a specific 
meaning in our context are detected by name:

- `ID`: identifies a row in the data file; either a local ID - preferably an [UUID](http://en.wikipedia.org/wiki/Universally_unique_identifier) - or an (equally universally unique) URL like http://wold.clld.org/word/7214142329897819 or http://wals.info/valuesets/1A-niv
- `Language_ID`: identifies the language or variety the data in the row is about. A [Glottolog languoid URL](http://glottolog.org), or *glottocode* or ISO-639-3 code (FIXME: require a URL, or a disambiguating prefix?), or a local identifier.
- `Source`: Semicolon-separated source specifications, of the form *<source_ID>[<source context>]*, e.g. *http://glottolog.org/resource/reference/id/318814[34]*, or *meier2015[3-12]* where *meier2015* is a citation key in the accompanying BibTeX file.
- `Example`: Semicolon-separated example specifications, of the form *<example_ID>[<context>]*, e.g. *http://apics-online.info/sentences/1-1[exception]*, or* sentence5* where *sentence5* is an ID in `clds.igt.csv`.
- `Comment`: Free text comment.

The core data file may also be encoded in tsv, i.e. using the `tab` character as column separator. If so, this must be
indicated by using `.tsv` as filename extension. (Tools like `csvkit` can be used to easily convert from tsv to csv.)


#### Compatibility

- Using UTF-8 as character encoding means editing these files with MS Excel is not completely trivial, because Excel assumes cp1252 as default character encoding - Libre Office Calc on the other hand handles these files just fine.
- The tool support for csv files is getting better and better due to the hype around "data science". Some particularly useful tools are
  - [csvkit](https://csvkit.readthedocs.org/en/stable/)
  - [q - Text as Data](http://harelba.github.io/q/)


### The metadata file

Metadata must be specified using [JSON-LD](http://json-ld.org/) as described in the [Metadata Vocabulary for Tabular Data](http://www.w3.org/TR/tabular-metadata/). 

However, to make tooling simpler, we restrict the metadata specification as follows:
- Metadata files must specify a `tables` property on top-level. While this add a bit of verbosity to the metadata description, it makes it possible to describe mutiple data tables in one metadata file.
- The table provided in the CLDF data file must be listed in `tables` using a `dc:type` attribute with value `cldf-values`.
- If each row in the data file corresponds to a resource on the web, the `tableSchema` property should provide an `aboutUrl` property.
- If individual cells in a row correspond to resources on the web, the corresponding column specification should provide a `valueUrl` property.

Each dataset should provide a dataset distribution description using the 
[DCAT vocabulary](http://www.w3.org/TR/vocab-dcat/#class-distribution). This will make it easy to  
[catalog](http://www.w3.org/TR/vocab-dcat/#class-catalog) cross-linguistic datasets.

An example for a metadata file could thus look as follows:
```python
{
  "@context": "http://www.w3.org/ns/csvw",
  "dc:title": "The Dataset",
  "dc:bibliographicCitation": "Cite me like this!",
  "dc:license": "http://creativecommons.org/licenses/by/4.0/",
  "tables": [
    {
      "url": "ds1.csv",
      "dc:type": "cldf-values",
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

This also provides a well-specified mechanism to document the particular CSV dialect used for the data files, as described in the [example for object properties](http://www.w3.org/TR/2015/WD-tabular-metadata-20150416/#object-properties); thus, the sometimes heated 
debate over "tab" versus "comma" could be elegantly circumvented.


## Data types

- [Wordlists](wordlist.md)
- [Structure dataset](structure_dataset.md)
- [Interlinear glossed text](igt.md)
- [Language metadata](language_metadata.md)


## cldf data on the Web

The core format specification is already following the guidelines of the [Model for Tabular Data and Metadata on the Web](http://www.w3.org/TR/tabular-data-model/), thus makes sure our formats follow best prectices for Web publishing.

Additionally cldf data providers may serve their datasets as [JSONP](http://en.wikipedia.org/wiki/JSONP) to make it possible to retrieve data from a browser-based application. For cldf data served as JSONP we specify the name of the callback function as `cldf_data` to make it possible to serve static files.


## Examples

To stipulate further discussion and help experiments with tools, some variant of cldf data may be obtained here:

- [A WALS chapter as cldf](examples/wals)

These downloads have been created using the [pycldf package](https://github.com/glottobank/pycldf).


## Open questions

- What about example sentences, formatted as [interlinear glossed text](http://en.wikipedia.org/wiki/Interlinear_gloss)? One solution would be to treat them like other structured properties of core data rows like sources, i.e. just add references in the core data file. Of course this would be facilitated with example collections - or [corpus journals](http://dlc.hypotheses.org/691).
- Should language IDs follow the [BCP 47](https://tools.ietf.org/html/bcp47) standard?
- Since the metadata file will often contain metadata about languages, i.e. about things with a spatial extension, we might consider using GeoJSON as format, because this will be more immediately useful. Unfortunately, the things described in a GeoJSON file are called *features*, which might be confusing, when used for languages which in turn may be described by *features* in the typological sense.
- Some data strcutures often encountered in historical linguistics cannot readily be represented by simple csv files, e.g. alignments (in particular multiple alignments), phylogenetic trees, and to a lesser degree distance matrices.


## History

Work on this concrete proposal for a cross-linguistic data formats was triggered by the [LANCLID 2 workshop](http://www.eva.mpg.de/linguistics/conferences/2014-ws-lanclid2/index.html) held in April 2015 in Leipzig -
in particular by Harald Hammarström's presentation [A Proposal for Data Interface Formats for Cross-Linguistic Data](https://github.com/clld/lanclid2/blob/master/presentations/hammarstrom.pdf).
