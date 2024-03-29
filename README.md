# CLDF: Cross-linguistic Data Formats

CLDF is a specification of data formats suitable to encode 
[cross-linguistic data](https://cldf.clld.org/)
in a way that maximizes interoperability and reusability, thus contributing to
FAIR Cross-Linguistic Data.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", 
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be 
interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).


## Conformance Levels

CLDF is based on W3C's suite of specifications for [CSV on the Web](https://www.w3.org/TR/tabular-data-primer/), 
or short CSVW. Thus, cross-linguistic data in CLDF is modeled as interrelated tabular data.
A CLDF dataset is:

- a set of UTF-8 encoded [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) files 
- described by metadata in form of a [CSVW TableGroup](http://w3c.github.io/csvw/metadata/#table-groups) serialized as JSON file
- with a [common property](http://w3c.github.io/csvw/metadata/#dfn-common-property) `dc:conformsTo` having one of the
  [CLDF module](#cldf-modules) URIs as value.

The main content of the metadata is the description of the [**schema**](https://en.wikipedia.org/wiki/Database_schema)
of the dataset, i.e. the tables, columns and relations between them, als known as **schema objects**.
The following typographical conventions will be used in the following when refering to schema objects:
- Properties and property values as used in a CLDF metadata are typeset in a [`monospaced font`](https://en.wikipedia.org/wiki/Monospaced_font).
- Filenames or column names as they appear in CSV data are typeset in *italics*.

While the [JSON-LD dialect](https://www.w3.org/TR/tabular-metadata/#json-ld-dialect) to be used for metadata according 
to the [Metadata Vocabulary for Tabular Data](https://www.w3.org/TR/tabular-metadata/) can be edited by hand, this may 
already be beyond what can be expected by regular users. Thus, CLDF specifies two conformance levels for datasets: 
metadata-free or extended.


### Metadata-free conformance

A dataset can be CLDF conformant without providing a separate metadata description file. To do so, the dataset MUST 
follow the default specification for the appropriate module regarding:

- filenames
- column names (for specified columns)
- CSV dialect

Thus, rather than not *having* any metadata, the dataset does not *specify*
any; instead it falls back to using the defaults.
Such single-CSV file datasets MAY contain additional columns not specified in 
the default module descriptions.

The default filenames and column names are described in [components](components). The default CSV dialect is 
[RFC4180](http://tools.ietf.org/html/rfc4180) using the [UTF-8](http://en.wikipedia.org/wiki/UTF-8) character encoding, 
i.e. the CSV dialect specified as:

```json
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

For a single CSV file to be a CLDF-compliant dataset without metadata
- the first line must contain the comma-separated list of column names,
- and no comment lines are allowed.

> [!TIP]
> Thus, a minimal metadata-free CLDF [StructureDataset](modules/StructureDataset) will consist of a CSV
> file named *values.csv*, with content looking like the example below:

```csv
ID,Language_ID,Parameter_ID,Value
1,stan1295,wals-1A,average
```


### Extended conformance

A dataset is CLDF conformant if 
- it contains a metadata file, derived from the default profile for the appropriate module,
- it contains the minimal set of components (i.e. CSV data files) specified for the module at least.

The metadata MUST contain a `dc:conformsTo` property with one of the [CLDF module URLs](#cldf-ontology) as value.

> [!TIP]
> Thus, a minimal extended CLDF [`StructureDataset`](modules/StructureDataset) will consist of
> - a JSON file containing the metadata (with a freely chosen name),
> - a CSV file containing the dataset's [`ValueTable`](components/values) (with a name as specified in the metadata).

Providing a metadata file allows for considerable flexibility in describing the data files, because the following
aspects can be customized (within the boundaries of the CSVW specification):
- the CSV [dialect description](http://w3c.github.io/csvw/metadata/#dialect-descriptions) (possibly per table), e.g. to:
  - allow comment lines (if appropriately prefixed with [`commentPrefix`](http://w3c.github.io/csvw/metadata/#dialect-commentPrefix))
  - omit a header line (if appropriately indicated by `"header": false`)
  - use tab-separated data files (if appropriately indicated by `"delimiter": "\t"`)
- the table property [`url`](http://w3c.github.io/csvw/metadata/#tables)
- the column property [`titles`](http://w3c.github.io/csvw/metadata/#columns)
- the inherited column properties
  - [`default`](http://w3c.github.io/csvw/metadata/#cell-default)
  - [`null`](http://w3c.github.io/csvw/metadata/#cell-null)
  - [`separator`](http://w3c.github.io/csvw/metadata/#cell-separator)
- adding common properties,
- adding [`foreign keys`](#foreign-keys), to specify relations between tables of the dataset.

Thus, using extended conformance via metadata, a dataset may:

- use tab-separated data files,
- use non-default file names,
- use non-default column names,
- add metadata describing attribution and provenance of the data,
- specify [relations between multiple tables](http://w3c.github.io/csvw/metadata/#foreign-key-reference-between-tables) in a dataset,
- supply default values for required columns like `languageReference`, using [virtual columns](http://w3c.github.io/csvw/metadata/#use-of-virtual-columns).

In particular, since the metadata description resides in a separate file, it is often possible to retrofit 
existing CSV files into the CLDF framework by adding a metadata description.

Thus, conformant CLDF processing software MUST implement support for the CSVW specification to the [extent necessary](#metadata).

> [!TIP]
> So, the minimal example from the previous section may consist of the following two files under extended conformance:
> A metadata description file `cldf-metadata.json`:

```json
{
  "@context": ["http://www.w3.org/ns/csvw", {"@language": "en"}],
  "dc:conformsTo": "http://cldf.clld.org/v1.0/terms.rdf#StructureDataset",
  "dialect": {"commentPrefix": "#", "delimiter":  ";"},
  "tables": [
    {
      "url": "data.csv",
      "dc:conformsTo": "http://cldf.clld.org/v1.0/terms.rdf#ValueTable",
      "tableSchema": {
        "columns": [
          {"name": "No", "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#id"},
          {"name": "LID", "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#languageReference"},           
          {"name": "PID", "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#parameterReference"},
          {"name": "Val", "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#value"}
        ]
      }
    }
  ]
}
```

> and `ValueTable` in a file `data.csv`:

```csv
No;LID;PID;Val
# Comments are allowed now!
1;stan1295;wals-1A;average
```


## CLDF Ontology

CLDF metadata uses terms from the [CLDF Ontology](http://cldf.clld.org/v1.0/terms.rdf), as specified in the file [*terms.rdf*](terms.rdf), 
to mark 
- [`TableGroup`](http://w3c.github.io/csvw/metadata/#table-groups) objects as representing a [CLDF module](modules),
- [`Table`](http://w3c.github.io/csvw/metadata/#tables) objects as representing a [CLDF component](components) or
- individual columns as representing [CLDF properties](http://cldf.clld.org/v1.0/terms.rdf#properties).

While many of these properties are similar (or identical) to properties defined 
elsewhere - most notably in the [General Ontology for Linguistic Description - GOLD](http://linguistics-ontology.org/) - 
we opted for inclusion to avoid ambiguity, but made sure to reference the related properties in the ontology.

> [!IMPORTANT]
> The CLDF-specific meaning of tables and columns in a dataset is determined by the **ontology terms**
> they are associated with, i.e. URLs specified as `dc:conformsTo` property for tables or as `propertyUrl`
> property for columns in the metadata file. The filenames and the column **names** of the CSV files are
> only used to **connect** metadata and actual data. Thus, while it is possible (and intentionally easy) to
> use CLDF data in a CLDF-agnostic way (e.g. importing data files of a CLDF dataset into a spreadsheet program),
> CLDF conformant tools MUST reference CLDF tables and columns by ontology terms and **not** by file or
> column name.

> [!NOTE]
> **Ontology terms** are the values for the `rdf:about` property of `rdf:Class` and `rdf:Property` objects
> in [*terms.rdf*](terms.rdf). Often we refer to ontology terms using just the [URL fragment](https://en.wikipedia.org/wiki/URI_fragment)
> or *local name*, rather than the full URL.

> [!NOTE]
> While filenames and column names in CLDF datasets (with metadata) can be freely chosen, the ontology
> recommends defaults for these as values of the `csvw:url` and `csvw.name` properties in *terms.rdf*.

> [!CAUTION]
> In an ill-advised attempt to version the ontology, `v1.0` has been baked into the term
> URIs. While this may be a good idea in case of incompatible changes (e.g. if the semantics
> of a term changed), it presents an obstacle for interoperability in case of backwards-compatible
> changes. So starting with CLDF 1.1, we will keep `http://cldf.clld.org/v1.0/terms.rdf`
> as namespace for **all** versions of the 1.x series, and specify the particular version
> when a term was introduced using `dc:hasVersion` properties per term.

> [!TIP]
> For better human readability the [CLDF Ontology](http://cldf.clld.org/v1.0/terms.rdf) should
> be visited with a browser capable of rendering XSLT - such as Firefox.


## CLDF Dataset

<a name="metadata"></a>
### CLDF Metadata file

A CLDF dataset is described with metadata provided as JSON file following the 
[Metadata Vocabulary for Tabular Data](https://www.w3.org/TR/tabular-metadata/). 
To make tooling simpler, we restrict the metadata specification as follows:

- Metadata files MUST specify a `tables` property on top-level, i.e. MUST describe a 
  [`TableGroup`](http://w3c.github.io/csvw/metadata/#table-groups). While this adds a 
  bit of verbosity to the metadata description, it makes it possible to describe multiple 
  tables in one metadata file.
- The common property `dc:conformsTo` of the `TableGroup` is used to indicate the
  [CLDF module](modules), e.g. 
  `"dc:conformsTo": "http://cldf.clld.org/v1.0/terms.rdf#Wordlist"`
- The common property `dc:conformsTo` of a `Table` is used to associate tables with
  a particular role in a CLDF module using appropriate classes from the 
  [CLDF Ontology](http://cldf.clld.org/v1.0/terms.rdf).
- If each row in the data file corresponds to a resource on the web (i.e. a resource
  identified by a dereferenceable HTTP URI), the `tableSchema` property SHOULD provide an 
  `aboutUrl` property.
- If individual cells in a row correspond to resources on the web, the corresponding 
  column specification SHOULD provide a `valueUrl` property.

Each dataset SHOULD provide a dataset distribution description using the 
[DCAT vocabulary](http://www.w3.org/TR/vocab-dcat/#class-distribution). This will make it easy to  
[catalog](http://www.w3.org/TR/vocab-dcat/#class-catalog) cross-linguistic datasets. 
In particular, each dataset description SHOULD include these properties:

- [`dc:bibliographicCitation`](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/terms/bibliographicCitation) and
- [`dc:license`](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/terms/license).

Thus, an example for a CLDF dataset description could look as follows:

```json
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
          }
        ],
        "aboutUrl": "http://example.org/valuesets/{ID}",
        "primaryKey": "ID"
      }
    }
  ]
}
```


### CLDF Data files

It is possible to add any kind of CSV files to a CLDF dataset (by virtue of being an extension of CSVW). 
While the CLDF standard recognizes (and attaches specified semantics) to tables described with a common property 
`dc:conformsTo` with one of the [component](#cldf-components) URIs of the [CLDF Ontology](http://cldf.clld.org/v1.0/terms.rdf) as value,
additional tables lacking this property in their metadata are acceptable.

Similarly, while CLDF semantics can be assigned to individual columns by 
assigning one of the property URIs defined in the 
[CLDF Ontology](http://cldf.clld.org/v1.0/terms.rdf) as `propertyUrl`, additional columns - also in [CLDF components](components) - are
acceptable.
CLDF conformant software MUST detect CLDF-specific columns by matching the `propertyUrl` to CLDF Ontology terms
and NOT by matching column name to default column names recommended in the ontology.


#### Column specifications

- CLDF column properties are assumed to have a complete row (or rather the
  entity a row stores data about) as scope; e.g. a [`source` column](#sources)
  is assumed to link to source information for any piece of data in the row.
  Thus, **each property can be used only once per table**, which makes processing simpler.
- More generally, CLDF assumes **column names (not just propertyUrls) in a table to be unique**.
- Since CLDF is designed to enable data reuse, data creators should assume that schema information
  like table or column names ends up in all sorts of environments, e.g. as names in SQL databases or
  as parts of URLs of a web application. Thus, it is RECOMMENDED to stick to ASCII characters in such
  names and avoid usage of punctuation other than `:._-`.
- **Cardinality:** CSVW allows specifying columns as "multivalued", i.e. as containing a list of values (of the same datatype),
  using the `separator` property. Thus, CLDF consumers MUST consult a column's `separator` property,
  to figure out whether the value must be interpreted as list or not. Note that this also applies to foreign keys.
  However, CLDF may restrict the cardinality as follows:
  - The specification of a property in the ontology MAY contain a `dc:extent` property
    with value `singlevalued` or `multivalued`, fixing cardinality of any instance of
    such a column in any table.
  - The specification of a column in the default metadata of a *component* MAY contain
    a `dc:extent` property with value `singlevalued` or `multivalued`, fixing cardinality.


#### Identifier

Each CLDF data table SHOULD contain a column which uniquely identifies a row in 
the table. This column SHOULD be marked using:

- a `propertyUrl` of `http://cldf.cld.org/v1.0/terms.rdf#id`
- the column name *ID* in the case of metadata-free conformance.

To allow usage of identifiers as path components of URIs and ensure they are
portable across systems, identifiers SHOULD be composed of 
[alphanumeric characters](https://en.wikipedia.org/wiki/Alphanumeric), 
underscore `_` and hyphen `-` only, i.e. match the regular expression 
`[a-zA-Z0-9\-_]+` (see [RFC 3986](https://tools.ietf.org/html/rfc3986#section-2.3)).

Following our design goal to reference rather than duplicate data, identifiers
may be used to reference existing entities (e.g. [Glottolog languages](http://glottolog.org/glottolog/language), [WALS features](http://wals.info/feature),
etc.). This can be done as follows:

- If the identifier can be interpreted as link to another entity, e.g. 
  using the WALS three-lettered language codes to identify languages, this should be 
  indicated by assigning the column an appropriate `valueUrl` property, e.g. 
  `http://wals.info/languoid/lect/wals_code_{ID}`
- If the identifier follows a specified identification scheme, e.g. [ISO 639-3](http://www-01.sil.org/iso639-3/) for
  languages, this can be indicated by adding [a virtual column](http://w3c.github.io/csvw/metadata/#x5-6-1-1-use-of-virtual-columns) with a suitable `propertyUrl`
  to the table's list of columns.


#### Missing data

Data creators often want to distinguish two kinds of missing data, in particular when the data is extracted from
sources:
1. data that is missing/unknown because it was never extracted from the source,
2. data that is indicated in the source as unknown.

The CSVW data model can be used to express this difference as follows:

- Case 1 can be modeled by not including the relevant data as row at all.
- Case 2 can be modeled using the `null` property of the relevant column specification (defaulting to the empty
string) as value in a data row.


#### Sources

Considering that any single step in collecting (cross-)linguistic data involves some
amount of analysis and judgement calls, it is essential to make it easy to trace
assertions back to their source.

Each CLDF data table may contain a column listing sources for the data asserted in the
row. This column - if present - MUST be marked using:

- a `propertyUrl` of `http://cldf.cld.org/v1.0/terms.rdf#source`
- the column name *Source* in the case of metadata-free conformance.

Sources are specified as semicolon-separated (unless the metadata specifies a different `separator`) source specifications, of the form
*source_ID[source context]*, e.g. *meier2015[3-12]* where *meier2015* is a citation key in the accompanying [sources file](#sources-reference-file).


#### Foreign keys

Often cross-linguistic data is [relational](https://en.wikipedia.org/wiki/Relational_model), e.g. *cognate judgements* 
group *forms* into *cognate sets*, creating a [many-to-many relationship](https://en.wikipedia.org/wiki/Many-to-many_(data_model)) 
between a `FormTable` and a `CognatesetTable`. 

To make such relations explicit, the CLDF Ontology provides a set of
[reference properties](http://cldf.clld.org/v1.0/terms.rdf#reference-properties).

Reference properties MUST be interpreted as foreign keys, e.g. a 
`propertyUrl` `http://cldf.clld.org/v1.0/terms.rdf#languageReference`
specified for column *Col1* of a table with `url` *table1.csv* is equivalent to a 
[CSVW foreign key constraint](http://w3c.github.io/csvw/metadata/#schema-foreignKeys)
```json
  "foreignKeys": [
       {
           "columnReference": "Col1",
           "reference": {
               "resource": "languages.csv",
               "columnReference": "ID"
           }
       }
   ]
```
assuming that the `LanguageTable` component has `url` `languages.csv` and a column *ID* with 
`propertyUrl` `http://cldf.clld.org/v1.0/terms.rdf#id`.

While spelling out foreign key constraints may feel cumbersome, it is still RECOMMENDED that metadata creators
do so, to make the data compatible with CSVW tools. The foreign key constraints MUST be specified explicitly 
if the referenced column does not have a `propertyUrl` `http://cldf.clld.org/v1.0/terms.rdf#id`.

> [!NOTE]
> Columns for reference properties may still be "nullable", i.e. contain `null` values, to allow
> for rows where no reference can be specified.


### Sources reference file

References to sources can be supplied as part of a CLDF dataset as an UTF-8 
encoded BibTeX file (with the citation keys serving as local source identifiers). The filename of this BibTeX file MUST be either:

- *sources.bib* in case of metadata-free conformance
- or specified as path relative to the metadata file given for top-level common property `dc:source` in the dataset's metadata.


### Compressed data or reference files

CLDF datasets may contain large data or reference files which may be inconvenient (e.g. because the size exceeds GitHub's
100MB filesize limit). In such cases, the dataset creator may compress individual files using the
[ZIP format](https://en.wikipedia.org/wiki/ZIP_(file_format)) (which works really well on CSV and BibTeX files).
The resulting ZIP archive MUST contain the zipped file and nothing else and MUST be named after the original
file, adding `.zip` as filename extension. The filename references in the metadata MUST be kept unchanged.

CLDF processing software MAY implement zip-file discovery, i.e. if a filename referenced in the metadata cannot
be found, but a file *filename_with_extension.zip* is found, processing MUST proceed with the unzipped content of 
*filename_with_extension.zip*.

If CLDF processing software does not support zip-file discovery, it should signal the corresponding error
in a transparent way. I.e. it should be clear for the user that the ZIP archive should be unzipped before
running the processing software.


## CLDF Modules

Much like 
[Dublin Core Application Profiles](http://dublincore.org/documents/profile-guidelines/),
[CLDF Modules](modules) group terms of the CLDF Ontology into tables.
Thus, CLDF module specifications are recommendations for groups
of tables modeling typical cross-linguistic datatypes. Currently, the CLDF
specification recognizes the following modules:

- [`Wordlist`](modules/Wordlist)
- [`StructureDataset`](modules/StructureDataset)
- [`Dictionary`](modules/Dictionary)
- [`ParallelText`](modules/ParallelText)
- [`TextCorpus`](modules/TextCorpus)

In addition, a CLDF dataset can be specified as 
[`Generic`](http://cldf.clld.org/v1.0/terms.rdf#Generic), imposing no requirements
on tables or columns. Thus, `Generic` datasets are a way to evolve new data types 
(to become recognized modules), while already providing (generic) tool support.

In the CLDF Ontology [modules](http://cldf.clld.org/v1.0/terms.rdf#modules) are modeled 
as subclasses of [`dcat:Distribution`](http://www.w3.org/ns/dcat#Distribution), thus 
additional metadata as recommended in the 
[DCAT specification](https://www.w3.org/TR/vocab-dcat/#class-distribution) SHOULD be 
provided.


## CLDF Components

Some types of cross-linguistic data may be part of different CLDF modules. These
types are specified as [CLDF components](components) in a way that can be re-used across modules 
(typically as [table descriptions](http://w3c.github.io/csvw/metadata/#tables), which can be appended 
to the `tables` property of a module's metadata). A *component* is a CSVW table description with a
`dc:conformsTo` property having one of the [component terms in the CLDF Ontology](https://cldf.clld.org/v1.0/terms.html#ValueTable) as value.
Each component listed below is described in a README and specified by the default
metadata file in the respective directory.

- [Language metadata](components/languages)
- [Parameter metadata](components/parameters)
- [Values](components/values) - as defined for a [`StructureDataset`](modules/StructureDataset)
- [Codes](components/codes)
- [Dictionary Entries](components/entries)
- [Dictionary Senses](components/senses)
- [(Glossed) Examples](components/examples)
- [Forms](components/forms) - as defined for a [`Wordlist`](modules/Wordlist)
- [Cognates](components/cognates)
- [CognateSets](components/cognatesets)
- [Borrowings](components/borrowings)
- [Functional Equivalents](components/functionalequivalents)
- [Functional Equivalents Sets](components/functionalequivalentsets)
- [(Classification) tree](components/trees)
- [Parameter networks](components/parameternetworks)
- [Citeable units](components/contributions)
- [Media files](components/media)


A component corresponds to a certain type of data. Thus, to make sure all instances of
such a type have the same set of properties, we allow at most one component for each type
in a CLDF dataset.


## Extensions

In addition to the specification of the CLDF data model and its representation on disk, several "mini-specifications"
extend the scope of the CLDF specification, by describing best practices and recommendations for common usage patterns
of CLDF data.

- [Dataset discovery](extensions/discovery.md)
- [CLDF Markdown](extensions/markdown.md)
- [CLDF SQL](extensions/sql.md)


## Reference implementation

In order to be able to assess the validity of CLDF datasets, i.e. to check datasets for CLDF conformance,
a reference implementation of CLDF is available as Python package [pycldf](https://pypi.org/project/pycldf/).

This package provides commandline functionality to validate datasets as well as a Python API to
programmatically read and write CLDF datasets.


## Compatibility

Using CSV as basic format for data files ensures compatibility of CLDF with many off-the-shelf computing
tools.

- Using UTF-8 as character encoding means editing these files with MS Excel is not completely trivial, because Excel 
  assumes cp1252 as default character encoding - Libre Office Calc on the other hand handles these files just fine.
- The tool support for CSV files is getting better and better due to increasing interest in [data science](https://en.wikipedia.org/wiki/Data_science). Some particularly useful tools are:
  - [csvkit](https://csvkit.readthedocs.io/en/latest/)
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
