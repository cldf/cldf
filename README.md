# CLDF: Cross-linguistic Data Formats

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
- specify [relations between multiple tables](http://w3c.github.io/csvw/metadata/#common-properties) in a dataset,
- supply default values for required columns like `Language_ID`, using virtual columns.

Note that it is possible to convert a CLDF dataset with metadata into one
without, automatically; although this means added metadata will be lost.


## CLDF Ontology

CLDF data uses terms from the [CLDF Ontology](http://cldf.clld.org/v1.0/terms.rdf) to mark [`TableGroup`](http://w3c.github.io/csvw/metadata/#table-groups) or [`Table`](http://w3c.github.io/csvw/metadata/#tables) objects which have special meaning within the CLDF framework.

Columns in tabular data recognized by CLDF-aware applications typically contain
linguistic data (apart from bookkeeping information like identifiers). For this
data we try to describe the specific data values using terms from the
[General Ontology for Linguistic Description - GOLD](http://linguistics-ontology.org/) or - if no matching concepts are provided by GOLD - from the [CLDF Ontology](http://cldf.clld.org/v1.0/terms.rdf).


<a id="modules"> </a>

## CLDF Modules

Much like [Dublin Core Application Profiles](http://dublincore.org/documents/profile-guidelines/), CLDF Modules describe of linguistic 
datatypes using terms of the CLDF Ontology grouped into tables.

In the [CLDF Ontology](http://cldf.clld.org/v1.0/terms.rdf) modules are modeled as subclasses of [`dcat:Distribution`](http://www.w3.org/ns/dcat#Distribution), thus additional metadata as recommended in the [DCAT specification](https://www.w3.org/TR/vocab-dcat/#class-distribution) should be provided.

For each type of CLDF dataset there is a *CLDF module*, i.e. a default metadata profile describing the required tables, columns and datatypes.
*metadata-free conformance* means data files will be read as if they were accompanied by the corresponding default metadata.

- [Wordlist](modules/Wordlist/)
- [Structure dataset](modules/StructureDataset/)
- [Dictionary](modules/Dictionary/)


## CLDF Components

Some types of cross-linguistic data may be part of different CLDF modules. These
types are specified as *components* in a way that can be re-used across modules (typically as [table descriptions](http://w3c.github.io/csvw/metadata/#tables), which can be appended to the `tables` property of a module's metadata).

- [Language metadata](components/languages/)
- [Parameter metadata](components/parameters/)
- [Examples](components/examples/)
- [Cognates](components/cognates/)
- [Partial cognates](components/partialcognates/)


## Examples

To stipulate further discussion and help experiments with tools, some examples of CLDF datasets are available in the [examples directory](examples/).


## Versioning

Changes to the CLDF specification will be released as new versions, using
a [Semantic Versioning](http://semver.org/) number scheme. While older versions
can be accessed via [releases of this repository](releases) or from 
[ZENODO](https://zenodo.org), where releases will be archived, the latest
released version is also reflected in the `master` branch of this repository,
i.e. whatever you see navigating the directory tree at [https://github.com/glottobank/cldf](https://github.com/glottobank/cldf/tree/master)
reflects the latest released version of the specification.


## History

Work on this concrete proposal for a cross-linguistic data format was triggered by the [LANCLID 2 workshop](http://www.eva.mpg.de/linguistics/conferences/2014-ws-lanclid2/index.html) held in April 2015 in Leipzig -
in particular by Harald Hammarström's presentation [A Proposal for Data Interface Formats for Cross-Linguistic Data](https://github.com/clld/lanclid2/blob/master/presentations/hammarstrom.pdf).
