# Cross-linguistic Data Formats


## Why?

To allow exchange of cross-linguistic data and [decouple development of tools and methods from that of databases](bigger_picture.md), standardized data formats are necessary.

Once established, these dataformats could become a foundation not only for tools but also for instruction material in the spirit of [Data Carpentry](http://datacarpentry.org/) for historical linguistics.

Very important: these dataformats are not necessarily the same formats as used in individual projects! These are interchange formats that might be supported to attain specific functionalities from external tools and methods.

## What?

The main types of cross-linguistic data we are concerned with here are wordlists and structure datasets which are used in historical linguistics and linguistic typology.


## Design goals

- Data should be both editable "by hand" and amenable to reading and writing by software.
- UTF-8 encoded line-based (ideally LF) text files.
- Reference entities rather than duplicate (i.e. use `long form tables`, sometimes called [`narrow form`][http://en.wikipedia.org/wiki/Wide_and_narrow_data])
- IDs should be resolvable HTTP URLs if possible. If not, they should be documented in the metadata
- Compatibility with existing tools, standards and practice should always be kept in mind.


## Core format specification

A cross-linguistic dataset is encoded in the following set of files:

- The core data file, encoded in csv (discussion point: should we allow tsv, be it only because it is used so much in current practice? tsv-assumptions: column separator is `\t`, quotes are always taken as literals)
- Metadata provided as JSON file (discussion point: also allow YAML, because it is much easier to edit by hand without introducting errors) following the guidelines of the [Model for Tabular Data and Metadata on the Web](http://www.w3.org/TR/tabular-data-model/#standard-file-metadata)
- The core data file can be amended by subsidiary `linked` files to explicate local IDs, e.g.
	- Sources - if not referenced by Glottolog ID, or other standard bibliographic identifiers like OCLC or ISBN - supplied as BibTeX file (with the citation keys serving as local Source IDs).
	- Languoids - if not referenced by Glottolog ID or ISO 639/3, or BCP47, supplying information on the languages references in the core data file
	- Explications about definitions of Features and Values - if not references by external ID - can be supplied in separate linked data files
	- Examples - if not referenced - may be supplied as [*cldf* IGT](igt.md) file.

If the name of the dataset is `clds`, the respective filenames are

- `clds.csv` (or `clds.tsv`)
- `clds-metadata.json` (or `clds-metadata.yaml`)

Optionally also e.g.

- `clds-references.bib`
- `clds-languoids.csv`
- `clds-feature.csv`
- `clds-igt.csv`

Proposal: the part of the file-name behind the dash should correspond to a column name in the core data file, except for the "metadata" file, allowing for further specification of the columns in the core data file.

### Identifiers

Following our design goal to reference rather than duplicate entities, identifiers should be used to reference existing entities (e.g. Glottolog languages, WALS features, etc.). To do so, identifiers must be formatted as resolvable HTTP(S) URLs.

Alternatively, identifiers may be used to reference dataset local entities which are defined in the datasets metadata (or not at all). In this case identiers must be composed of the characters defined by the regular expression `[a-zA-Z0-9\-_]`. This restriction makes sure that these identifiers can be used as path components of HTTP URLs (see [rfc3986](https://tools.ietf.org/html/rfc3986#section-2.3)).

Issues: #3


### The data file

The core data file is encoded in [csv](http://tools.ietf.org/html/rfc4180) using the [UTF-8](http://en.wikipedia.org/wiki/UTF-8) character encoding. This file must have a header, i.e. the first row must contain the list of column names. While the file may contain any number of columns, columns with a specific meaning in our context are detected by name:

- `ID`: identifies a row in the data file; either a local ID - preferably an [UUID](http://en.wikipedia.org/wiki/Universally_unique_identifier) - or an (equally universally unique) URL like http://wold.clld.org/word/7214142329897819 or http://wals.info/valuesets/1A-niv
- `Language_ID`: identifies the language or variety the data in the row is about. A [Glottolog languoid URL](http://glottolog.org), or *glottocode* or ISO-639-3 code (FIXME: require a URL, or a disambiguating prefix?), or a local identifier.
- `Feature_ID`: the `question` to be asked to the language, i.e. the `Domain` or `Function` or `Trait` to be investigated
- `Value_ID`: the `answer` to the question, i.e. the actual information about the language in question.
- `Source`: Semikolon-separated source specifications, of the form *<source_ID>[<source context>]*, e.g. *http://glottolog.org/resource/reference/id/318814[34]*, or *meier2015[3-12]* where *meier2015* is a citation key in the accompanying BibTeX file.
- `Example`: Semikolon-separated example specifications, of the form *<example_ID>[<context>]*, e.g. *http://apics-online.info/sentences/1-1[exception]*, or* sentence5* where *sentence5* is an ID in `clds.igt.csv`.
- `Comment`: Free text comment. (Diskussion topic: do not allow comments in the main data file?)

Diskussion: do we allow for a second separator inside csv-cells (above: semicolon)? It makes files more powerful, but also more complex. If we decide on a second-level separator, then I would propose a highly unusual UTF-8 symbol, e.g. \u2005 (FOUR-PER-EM SPACE) or \u204F (REVERSED SEMICOLON).

#### Compatibility

- Using UTF-8 as character encoding means editing these files with MS Excel is not completely trivial, because Excel assumes cp1252 as default character encoding - Libre Office Calc on the other hand handles these files just fine.
- The tool support for csv files is getting better and better due to the hype around "data science". Some particularly useful tools are
  - [csvkit](https://csvkit.readthedocs.org/en/stable/)
  - [q - Text as Data](http://harelba.github.io/q/)


### The metadata file

Metadata should be specified using [JSON-LD](http://json-ld.org/) as described in the [Metadata Vocabulary for Tabular Data](http://www.w3.org/TR/tabular-metadata/), containing a dataset distribution description using the 
[DCAT vocabulary](http://www.w3.org/TR/vocab-dcat/#class-distribution). This will make it easy to  
[catalog](http://www.w3.org/TR/vocab-dcat/#class-catalog) cross-linguistic datasets.

It would also provide a well-specified mechanism to document the particular CSV dialect used for the data files, as described in the [example for object properties](http://www.w3.org/TR/2015/WD-tabular-metadata-20150416/#object-properties); thus, the sometimes heated 
debate over "tab" versus "comma" could be elegantly circumvented.

Alternative: also allow YAML files (which are much easier to process by hand)

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

- [WALS as cldf](http://wals.info/download)
- [SAILS as cldf](http://sails.clld.org/download)

These downloads have been created using the [clld toolkit](https://github.com/clld/clld/blob/master/clld/web/adapters/cldf.py).


## Open questions

- What about example sentences, formatted as [interlinear glossed text](http://en.wikipedia.org/wiki/Interlinear_gloss)? One solution would be to treat them like other structured properties of core data rows like sources, i.e. just add references in the core data file. Of course this would be facilitated with example collections - or [corpus journals](http://dlc.hypotheses.org/691).
- Should language IDs follow the [BCP 47](https://tools.ietf.org/html/bcp47) standard?
- Since the metadata file will often contain metadata about languages, i.e. about things with a spatial extension, we might consider using GeoJSON as format, because this will be more immediately useful. Unfortunately, the things described in a GeoJSON file are called *features*, which might be confusing, when used for languages which in turn may be described by *features* in the typological sense.
- Some data strcutures often encountered in historical linguistics cannot readily be represented by simple csv files, e.g. alignments (in particular multiple alignments), phylogenetic trees, and to a lesser degree distance matrices.


## History

Work on this concrete proposal for a cross-linguistic data formats was triggered by the [LANCLID 2 workshop](http://www.eva.mpg.de/linguistics/conferences/2014-ws-lanclid2/index.html) held in April 2015 in Leipzig -
in particular by Harald Hammarström's presentation [A Proposal for Data Interface Formats for Cross-Linguistic Data](https://github.com/clld/lanclid2/blob/master/presentations/hammarstrom.pdf).
