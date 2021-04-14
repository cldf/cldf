# CLDF: Cross-linguistic Data Formats

**Table of Contents**

* [Conformance Levels](#conformance-levels)
   * [Metadata-free conformance](#metadata-free-conformance)
   * [Extended conformance](#extended-conformance)
* [CLDF Ontology](#cldf-ontology)
* [CLDF Dataset](#cldf-dataset)
   * [CLDF Metadata file](#cldf-metadata-file)
   * [CDLF Data files](#cldf-data-files)
   * [Sources file](#sources)
* [CLDF Modules](#cldf-modules)
* [CLDF Components](#cldf-components)
* [Compatibility](#compatibility)
* [Examples](#examples)
* [Versioning](#versioning)
* [History](#history)


## Conformance Levels

A CLDF dataset is

- a set of UTF-8 encoded CSV files 
- described by a [TableGroup](http://w3c.github.io/csvw/metadata/#table-groups) serialized as JSON file
- with a [common property](http://w3c.github.io/csvw/metadata/#dfn-common-property) `dc:conformsTo` having one of the [CLDF module](#cldf-modules) URIs as value.

While the [JSON-LD dialect](https://www.w3.org/TR/tabular-metadata/#json-ld-dialect) to be used for metadata according to the [Metadata Vocabulary for Tabular Data](https://www.w3.org/TR/tabular-metadata/) can be edited by hand, this may already be beyond what can be expected by regular users. Thus, CLDF specifies two conformance levels for datasets: metadata-free or extended.

### Metadata-free conformance

A dataset can be CLDF conformant without providing a separate metadata description file. To do so, the dataset must *exactly* follow the default specification for the appropriate module regarding:

- file names
- column names (for specified columns)
- CSV dialect

Thus, rather than not *having* any metadata, the dataset does not *specify*
any; and instead it falls back to using the defaults, i.e. "free" as in "beer" not
as in "gluten-free". The CSV file may contain additional columns not specified in 
the default module descriptions.

The default file names and column names are described in [`components`](components). The default CSV dialect is [RFC4180](http://tools.ietf.org/html/rfc4180) using the [UTF-8](http://en.wikipedia.org/wiki/UTF-8) character encoding, i.e. use the CSV dialect specified by

```
{
  "encoding": "utf-8",
  "lineTerminators": ["\r\n", "\n"],
  "quoteChar": "\"",
  "doubleQuote": true,
  "skipRows": 0,
  "commentPrefix": "#",
  "header": true,
  "headerRowCount": 1,
  "delimiter": ",",
  "skipColumns": 0,
  "skipBlankRows": false,
  "skipInitialSpace": false,
  "trim": false
}
```

Some of the effects of this metadata-free conformance are:
- The first line of each file must contain the comma-separated list of column names.
- No comment lines are allowed.

### Extended conformance

A dataset is CLDF conformant if it uses a custom metadata file, derived from the default profile for the appropriate module, possibly overriding/customizing:

- the CSV [dialect description](http://w3c.github.io/csvw/metadata/#dialect-descriptions) (possibly per table), e.g. to:
  - allow comment lines (if appropriately prefixed with [`commentPrefix`](http://w3c.github.io/csvw/metadata/#dialect-commentPrefix))
  - omit a header line (if appropriately indicated by `"header": false`)
  - use tab-separated data files (if appropriately indicated by `"delimiter": "\t"`)
- the table property [url](http://w3c.github.io/csvw/metadata/#tables)
- the column property [titles](http://w3c.github.io/csvw/metadata/#columns)
- the inherited column properties
  - [default](http://w3c.github.io/csvw/metadata/#cell-default)
  - [null](http://w3c.github.io/csvw/metadata/#cell-null)
  - [separator](http://w3c.github.io/csvw/metadata/#cell-separator)
- adding common properties,
- adding [foreign keys](#foreign-keys), to specify relations between tables of the dataset.

Thus, using extended conformance via metadata, a dataset may

- use tab-separated data files,
- use non-standard file names,
- use non-standard column names,
- add metadata describing attribution and provenance of the data,
- specify [relations between multiple tables](http://w3c.github.io/csvw/metadata/#foreign-key-reference-between-tables) in a dataset,
- supply default values for required columns like `Language_ID`, using [virtual columns](http://w3c.github.io/csvw/metadata/#use-of-virtual-columns).

In particular, since the metadata description resides in a separate file, it is often possible to retrofit existing CSV files into the CLDF framework by adding a metadata description.

## CLDF Ontology

CLDF data uses terms from the [CLDF Ontology](http://cldf.clld.org/v1.0/terms.rdf), as specified in the file `terms.rdf`, to mark [`TableGroup`](http://w3c.github.io/csvw/metadata/#table-groups) or [`Table`](http://w3c.github.io/csvw/metadata/#tables) objects which have special meaning within the CLDF framework.

The CLDF Ontology also provides a set of [properties](http://cldf.clld.org/v1.0/terms.rdf#properties) to attach semantics to individual columns. While many of these properties are similar (or identical) to properties defined elsewhere - most notably in the [General Ontology for Linguistic Description - GOLD](http://linguistics-ontology.org/) - we opted for inclusion to avoid ambiguity, but made sure to reference the related related properties in the Ontology.

Note that the column *names* in the default table descriptions (e.g. [`formTable`](components/forms)) are not always the same as the column *properties*. Each column has both a `csvw:name` and a separate `propertyURL` linking the column to the ontology. Each property also has a `rdf:label` which might also be different.

**Notes:**
- In an ill-advised attempt to version the ontology, `v1.0` has been baked into the term
  URIs. While this may be a good idea in case of incompatible changes (e.g. if the semantics
  of a term changed), it presents an obstacle for initeroperability in case of backwards-compatible
  changes. So starting with CLDF 1.1, we will keep `http://cldf.clld.org/v1.0/terms.rdf`
  as namespace for **all** versions of the 1.x series, and specify the particular version
  when a term was introduced using `dc:hasVersion` properties per term.
- For better human readability the [CLDF Ontology](http://cldf.clld.org/v1.0/terms.rdf) should
be visited with a browser capable of rendering XSLT - such as Firefox.


## CLDF Dataset

### CLDF Metadata file

A CLDF dataset is described with metadata provided as JSON file following the [Metadata Vocabulary for Tabular Data](https://www.w3.org/TR/tabular-metadata/). To make tooling simpler, we restrict the metadata specification as follows:

- Metadata files must specify a `tables` property on top-level, i.e. must describe a 
  [`TableGroup`](http://w3c.github.io/csvw/metadata/#table-groups). While this adds a 
  bit of verbosity to the metadata description, it makes it possible to describe multiple 
  tables in one metadata file.
- The common property `dc:conformsTo` of the `TableGroup` is used to indicate the
  CLDF module, e.g. 
  `"dc:conformsTo": "http://cldf.clld.org/v1.0/terms.rdf#Wordlist"`
- The common property `dc:conformsTo` of a `Table` is used to associate tables with
  a particular role in a CLDF module using appropriate classes from the 
  [CLDF Ontology](http://cldf.clld.org/v1.0/terms.rdf).
- If each row in the data file corresponds to a resource on the web (i.e. a resource
  identified by a dereferenceable HTTP URI), the `tableSchema` property should provide an 
  `aboutUrl` property.
- If individual cells in a row correspond to resources on the web, the corresponding 
  column specification should provide a `valueUrl` property.

Each dataset should provide a dataset distribution description using the [DCAT vocabulary](http://www.w3.org/TR/vocab-dcat/#class-distribution). This will make it easy to  [catalog](http://www.w3.org/TR/vocab-dcat/#class-catalog) cross-linguistic datasets. In particular, each dataset description should include properties

- `dc:bibliographicCitation` and
- `dc:license`.

Thus, an example for a CLDF dataset description could look as follows:

```
{
  "@context": "http://www.w3.org/ns/csvw",
  "dc:conformsTo": "http://cldf.clld.org/v1.0/terms.rdf#StructureDataset",
  "dc:title": "The Dataset",
  "dc:bibliographicCitation": "Cite me like this!",
  "dc:license": "http://creativecommons.org/licenses/by/4.0/",
  "null": "?",
  "tables": [
    {
      "url": "ds1.csv",
      "dc:conformsTo": "http://cldf.clld.org/v1.0/terms.rdf#ValueTable",
      "tableSchema": {
        "columns": [
          {
            "name": "ID",
            "datatype": "string",
            "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#id"
          },
          {
            "name": "Language_ID",
            "datatype": "string",
            "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#languageReference",
            "valueUrl": "http://glottolog.org/resource/languoid/id/{Language_ID}"
          },
          {
            "name": "Parameter_ID",
            "datatype": "string",
            "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#parameterReference"
          },
          {
            "name": "Value",
            "datatype": "string",
            "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#value"
          },
          {
            "name": "Comment",
            "datatype": "string",
            "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#comment"
          },
          {
            "name": "Source",
            "datatype": "string",
            "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#source"
          },
          {
            "name": "Glottocode",
            "virtual": true,
            "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#glottocode",
            "valueUrl": "{Language_ID}"
          },
        ],
        "aboutUrl": "http://example.org/valuesets/{ID}",
        "primaryKey": "ID"
      }
    }
  ]
}
```


### CLDF Data files

While it is possible to add any kind of CSV files to a CLDF dataset, the CLDF standard
recognizes (and attaches specified semantics) to tables described with a common property `dc:conformsTo` with one of the [table type](#cldf-components) URIs of the [CLDF ontology](http://cldf.clld.org/v1.0/terms.rdf) as value.

Additionally, CLDF semantics can be assigned to individual columns by 
assigning one of the property URIs defined in the 
[CLDF ontology](http://cldf.clld.org/v1.0/terms.rdf) as `propertyUrl`.

Note: CLDF column properties are assumed to have a complete row (or rather the
entity a row stores data about) as scope; e.g. a [source column](#sources)
is assumed to provide source information for any piece of data in the row.
Thus, each property can be used only once per table, which makes processing simpler.


#### Identifier

Each CLDF data table should contain a column which uniquely identifies a row in 
the table. This column must be marked using

- a `propertyUrl` of `http://cldf.cld.org/v1.0/terms.rdf#id`
- the column name `ID` in the case of metadata-free conformance.

To allow usage of identifiers as path components of URIs and ensure they are
portable across systems, identifiers must be composed of 
[alphanumeric characters](https://en.wikipedia.org/wiki/Alphanumeric), 
underscore `_` and hyphen `-` only, i.e. match the regular expression 
`[a-zA-Z0-9\-_]+` (see [RFC 3986](https://tools.ietf.org/html/rfc3986#section-2.3)).

Following our design goal to reference rather than duplicate data, identifiers
may be used to reference existing entities (e.g. [Glottolog languages](http://glottolog.org/glottolog/language), [WALS features](http://wals.info/feature),
etc.). This can be done as follows:

- If the identifier can be interpreted as links to other entities, e.g. 
  using the WALS three-lettered language codes to identify languages, this should be 
  indicated by assigning the column an appropriate `valueUrl` property, e.g. 
  `http://wals.info/languoid/lect/wals_code_{ID}`
- If the identifier follows a specified identification scheme, e.g. [ISO 639-3](http://www-01.sil.org/iso639-3/) for
  languages, this can be indicated by adding [a virtual column](http://w3c.github.io/csvw/metadata/#x5-6-1-1-use-of-virtual-columns) with a suitable `propertyUrl`
  to the table's list of columns.


#### Sources

Considering that any single step in collecting (cross-)linguistic data involves some
amount of analysis and judgement calls, it is essential to make it easy to trace
assertions back to their source.

Each CLDF data table may contain a column listing sources for the data asserted in the
row. This column must be marked using

- a `propertyUrl` of `http://cldf.cld.org/v1.0/terms.rdf#source`
- the column name `Source` in the case of metadata-free conformance.

Sources are specified as semicolon-separated source specifications, of the form
*source_ID[source context]*, e.g. *meier2015[3-12]* where *meier2015* is a citation key in the accompanying [sources file](#sources).


#### Foreign keys

Often cross-linguistic data is [relational](https://en.wikipedia.org/wiki/Relational_model), e.g. *cognate judgements* group *forms* into *cognate sets*, creating a [many-to-many relationship](https://en.wikipedia.org/wiki/Many-to-many_(data_model)) between a `FormTable` and a `CognatesetTable`. 

To make such relations explicit, the CLDF Ontology provides a set of
[reference properties](http://cldf.clld.org/v1.0/terms.rdf#reference-properties).

Reference properties are interpreted as *optional* foreign key, i.e.

- if a `table1.csv` makes reference to a `table2.csv`, and both are part of the dataset, then mentioning the `ID` from table2 in a column of table1 (typically using the column-name `table2_ID`) is sufficient as a reference, and this is implicit equivalent to a [foreignKeys](http://w3c.github.io/csvw/metadata/#schema-foreignKeys) property of `table1.csv`:

```
  "columns": [
      "name": "table2_ID",
      ...
      ]
  "foreignKeys": [
       {
           "columnReference": "table2_ID",
           "reference": {
               "resource": "table2.csv",
               "columnReference": "ID"
           }
       }
   ]
```

- otherwise values in the column are interpreted as identifiers of the referenced
  entities (in which case the actual entities can only be resolved by context
  or via additonal `valueUrl` properties on the column).


<a id="sources"> </a>

### Sources reference file

References to sources - if not referenced by Glottolog ID - can be supplied as part of a CLDF dataset as an UTF-8 encoded BibTeX file (with the citation keys serving as local Source IDs). The filename of this BibTeX file must be either:

- `sources.bib` in case of metadata-free conformance
- or specified as top-level common property `dc:source` in the dataset's metadata.


## CLDF Modules

Much like 
[Dublin Core Application Profiles](http://dublincore.org/documents/profile-guidelines/),
CLDF Modules group terms of the CLDF Ontology into tables.
Thus, CLDF module specifications are recommendations for groups
of tables modeling typical cross-linguistic datatypes. Currently, the CLDF
specification recognizes the following modules:

- [Wordlist](modules/Wordlist)
- [Structure dataset](modules/StructureDataset)
- [Dictionary](modules/Dictionary)
- [Parallel text](modules/ParallelText)

In addition, a CLDF dataset can be specified as 
[*Generic*](http://cldf.clld.org/v1.0/terms.rdf#Generic), imposing no requirements
on tables or columns. Thus, *Generic* datasets are a way to evolve new data types 
(to become recognized modules), while already providing (generic) tool support.

In the CLDF Ontology [modules](http://cldf.clld.org/v1.0/terms.rdf#modules) are modeled 
as subclasses of [`dcat:Distribution`](http://www.w3.org/ns/dcat#Distribution), thus 
additional metadata as recommended in the 
[DCAT specification](https://www.w3.org/TR/vocab-dcat/#class-distribution) should be 
provided.

For each type of CLDF dataset there is a *CLDF module*, i.e. a default metadata profile 
describing the required tables, columns and datatypes.
*metadata-free conformance* means data files will be read as if they were accompanied by 
the corresponding default metadata.


## CLDF Components

Some types of cross-linguistic data may be part of different CLDF modules. These
types are specified as *components* in a way that can be re-used across modules (typically as [table descriptions](http://w3c.github.io/csvw/metadata/#tables), which can be appended to the `tables` property of a module's metadata).

- [Language metadata](components/languages)
- [Parameter metadata](components/parameters)
- [Values](components/values) - as defined for a [`StructureDataset`](modules/StructureDataset)
- [Codes](components/codes)
- [Entries](components/entries)
- [Senses](components/senses)
- [Examples](components/examples)
- [Forms](components/forms) - as defined for a [`Wordlist`](modules/Wordlist)
- [Cognates](components/cognates)
- [CognateSets](components/cognatesets)
- [Borrowings](components/borrowings)
- [Functional Equivalents](components/functionalequivalents)
- [Functional Equivalents Sets](components/functionalequivalentsets)

A component corresponds to a certain type of data. Thus, to make sure all instances of
such a type have the same set of properties, we allow at most one component for each type
in a CLDF dataset.


## Compatibility

- Using UTF-8 as character encoding means editing these files with MS Excel is not completely trivial, because Excel assumes cp1252 as default character encoding - Libre Office Calc on the other hand handles these files just fine.
- The tool support for CSV files is getting better and better due to the hype around "data science". Some particularly useful tools are
  - [csvkit](https://csvkit.readthedocs.org/en/stable/)
  - [q - Text as Data](http://harelba.github.io/q/)

## Versioning

Changes to the CLDF specification will be released as new versions, using
a [Semantic Versioning](http://semver.org/) number scheme. While older versions
can be accessed via [releases of this repository](https://github.com/cldf/cldf/releases) or from 
[ZENODO](https://zenodo.org), where releases will be archived, the latest
released version is also reflected in the `master` branch of this repository,
i.e. whatever you see navigating the directory tree at [https://github.com/cldf/cldf](https://github.com/cldf/cldf/tree/master)
reflects the latest released version of the specification.

## History

Work on this proposal for a cross-linguistic data format was triggered by the [LANCLID 2 workshop](http://www.eva.mpg.de/linguistics/conferences/2014-ws-lanclid2/index.html) held in April 2015 in Leipzig -
in particular by Harald Hammarström's presentation [A Proposal for Data Interface Formats for Cross-Linguistic Data](https://github.com/clld/lanclid2/blob/master/presentations/hammarstrom.pdf).
