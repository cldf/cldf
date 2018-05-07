## Values

The core data of a CLDF `StructureDataset` is the list of values (a.k.a. measurements or datapoints).
Each value is stored as a separate row in the `Vauetable`, providing, at the least, the following columns:
 
- [ID](http://cldf.clld.org/v1.0/terms.rdf#id): A unique identifier for the row within the table.
- [Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference): A reference to a language (or variety) the form belongs to.
- [Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference): A reference to the meaning denoted by the form.
- [Value](http://cldf.clld.org/v1.0/terms.rdf#value): The measurement.

For categorical variables, it is often useful to supply the list of valid values using a `CodeTable`. In this case, a [Code_ID](http://cldf.clld.org/v1.0/terms.rdf#codeReference) column in the `ValueTable` should be used to
link value to code.

As with any CLDF component, 
- comments and references to sources can be added via
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) and [Source](http://cldf.clld.org/v1.0/terms.rdf#source) columns respectively,
- additional data can be supplied in additional columns.


### Example

The [CLDF download](https://cdstar.shh.mpg.de/bitstreams/EAEA0-7269-77E5-3E10-0/wals_dataset.cldf.zip) linked from
the download page of [WALS Online](http://wals.info) contains a `ValueTable` in `values.csv` starting with

```
ID,Language_ID,Parameter_ID,Value,Code_ID,Comment,Source,Contribution_ID
1A-kgi,kgi,1A,Large,1A-5,,Santos-1977,1
1A-cve,cve,1A,Small,1A-1,,Thurman-1970,1
```


### Multi-dimensional features

Multi-dimensional features are useful to model data like paradigms. 
To support multi-dimensional features, we specify a standard separator for 
`Parameter_ID` components: `~`. 
I.e. a local feature ID for a multi-dimensional feature can be coded as
```
Language_ID Feature_ID Value
deu         Sg~1P     ich
deu         Pl~1P     wir
