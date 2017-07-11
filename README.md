# Cross-linguistic Data Formats

## Why?

To allow exchange of cross-linguistic data and [decouple development of tools and methods from that of databases](bigger_picture.md), standardized data formats are necessary.

Once established, these dataformats could become a foundation not only for tools but also for instruction material in the spirit of [Data Carpentry](http://datacarpentry.org/) for historical linguistics and linguistic typology.


## What?

The main types of cross-linguistic data we are concerned with here are any tabular data which is typically
analysed using quantitative (automated) methods or made accessible using software tools like the `clld` framework, such as
- wordlists (or more complex lexical data including e.g. cognate judgements),
- structure datasets (e.g. [WALS features](http://wals.info/feature)),
- simple dictionaries.


## Design principles

- Data should be both editable "by hand" and amenable to reading and writing by software (preferably software the typical linguist can be expected to use correctly).
- Data should be encoded as UTF-8 text files.
- If entities can be referenced, e.g. languages through their Glottocode, 
  this should be done rather than duplicating information like language names.
- Identifier should be resolvable HTTP URLs if possible. If not, they should be documented in the metadata.
- Compatibility with existing tools, standards and practice should always be kept in mind.

Since we are concerned with tabular data here, CLDF is built on W3C's 
[Model for Tabular Data and Metadata on the Web](http://www.w3.org/TR/tabular-data-model/#standard-file-metadata) and 
[Metadata Vocabulary for Tabular Data](https://www.w3.org/TR/tabular-metadata/).

The CLDF specification is split into a [core specification](core.md), applying to
all kinds of CLDF data and [modules](#modules), describing the data model for a particular kind of cross-linguistic data.


## Conformance Levels

While the [JSON-LD dialect](https://www.w3.org/TR/tabular-metadata/#json-ld-dialect) to be used for metadata according to the
[Metadata Vocabulary for Tabular Data](https://www.w3.org/TR/tabular-metadata/)
can be edited by hand, this may be already be beyond what can be expected by
typical linguists.

Thus, CLDF specifies two conformance levels for datasets:

### Metadata-free conformance

A dataset can be CLDF conformant without providing a separate metadata description file. To do so, the dataset must follow the default specification
for the appropriate module regarding
- file names
- CSV dialect
- column names

exactly.


### Extended conformance

A dataset is CLDF conformant if it uses a custom metadata file, derived from
the default profile for the appropriate module, possibly overriding/customizing
- the CSV [dialect description](http://w3c.github.io/csvw/metadata/#dialect-descriptions)
- the table property [url](http://w3c.github.io/csvw/metadata/#tables)
- the column property [titles](http://w3c.github.io/csvw/metadata/#columns)
- the inherited column properties
  - [default](http://w3c.github.io/csvw/metadata/#cell-default)
  - [null](http://w3c.github.io/csvw/metadata/#cell-null)
  - [separator](http://w3c.github.io/csvw/metadata/#cell-separator)

and by adding
- common properties,
- foreign keys, to specify relations between tables of the dataset.

Thus, using extended conformance via metadata, a dataset may
- use tab-separated data files,
- use non-standard file names,
- use non-standard column names,
- add metadata describing attribution and provenance of the data,
- specify [relations between multiple tables](http://w3c.github.io/csvw/metadata/#common-properties) in a dataset.

Note that it is possible to convert a CLDF dataset with metadata into one
without, automatically; although this means added metadata will be lost.


## CLDF Ontology

CLDF data uses terms from the [CLDF Ontology](http://cldf.clld.org/terms.rdf) to mark `TableGroup` or `Table` objects which have special meaning within the CLDF framework.

Columns in tabular data recognized by CLDF-aware applications typically contain
linguistic data (apart from bookkeeping information like identifiers). For this
data we try to describe the specific data values using terms from the
[General Ontology for Linguistic Description - GOLD](http://linguistics-ontology.org/) or - if no matching concepts are provided by GOLD - from the [CLDF Ontology](http://cldf.clld.org/terms.rdf).


<a id="modules"> </a>

## CLDF Modules

Much like [Dublin Core Application Profiles](http://dublincore.org/documents/profile-guidelines/), CLDF Modules describe of linguistic 
datatypes using terms of the CLDF Ontology grouped into tables.

In the [CLDF Ontology](http://cldf.clld.org/terms.rdf) modules are modeled as subclasses of [`dcmitype:Dataset`](http://dublincore.org/documents/2012/06/14/dcmi-terms/?v=dcmitype#Dataset).

For each type of CLDF dataset there is a *CLDF module*, i.e. a default metadata profile describing the required tables, columns and datatypes.
*metadata-free conformance* means data files will be read as if they were accompanied by the corresponding default metadata.

- [Wordlist](modules/wordlist/)
- [Structure dataset](modules/structure_dataset/)
- [Dictionary](modules/dictionary/)


## CLDF Components

Some types of cross-linguistic data may be part of different CLDF modules. These
types are specified as *components* in a way that can be re-used across modules (typically as [table descriptions](http://w3c.github.io/csvw/metadata/#tables), which can be appended to the `tables` property of a module's metadata).

- [Language metadata](components/languages/)
- [Examples](components/examples/)


## CLDF data on the Web

The core format specification is already following the guidelines of the [Model for Tabular Data and Metadata on the Web](http://www.w3.org/TR/tabular-data-model/), thus makes sure our formats follow best practices for Web publishing.

Additionally CLDF data providers may serve their datasets as [JSONP](http://en.wikipedia.org/wiki/JSONP) to make it possible to retrieve data from a browser-based application. For CLDF data served as JSONP we specify the name of the callback function as `cldf_data` to make it possible to serve static files.


## Examples

To stipulate further discussion and help experiments with tools, some variant of CLDF data may be obtained here:

- [A WALS chapter as CLDF](examples/wals)

These downloads have been created using the [pycldf package](https://github.com/glottobank/pycldf).


## Open questions

- Should language IDs follow the [BCP 47](https://tools.ietf.org/html/bcp47) standard?
- Some data structures often encountered in historical linguistics cannot readily be represented by simple csv files, e.g. alignments (in particular multiple alignments), phylogenetic trees, and to a lesser degree distance matrices.


## History

Work on this concrete proposal for a cross-linguistic data format was triggered by the [LANCLID 2 workshop](http://www.eva.mpg.de/linguistics/conferences/2014-ws-lanclid2/index.html) held in April 2015 in Leipzig -
in particular by Harald Hammarström's presentation [A Proposal for Data Interface Formats for Cross-Linguistic Data](https://github.com/clld/lanclid2/blob/master/presentations/hammarstrom.pdf).
