# Values

The core data of a CLDF `StructureDataset` is the list of values (a.k.a. measurements or datapoints).
Each value is stored as a separate row in the `Vauetable`, providing, at the least, the following columns:
 
- [ID](http://cldf.clld.org/v1.0/terms.rdf#id): A unique identifier for the row within the table.
- [Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference): A reference to a language (or variety) the form belongs to.
- [Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference): A reference to the meaning denoted by the form.
- [Value](http://cldf.clld.org/v1.0/terms.rdf#value): The measurement.

For categorical variables, it is often useful to supply the list of valid values using a `CodeTable`. In this case, a [codeReference](http://cldf.clld.org/v1.0/terms.rdf#codeReference) column in the `ValueTable` should be used to
link value to code.

As with any CLDF component, 
- comments and references to sources can be added via
[comment](http://cldf.clld.org/v1.0/terms.rdf#comment) and [source](http://cldf.clld.org/v1.0/terms.rdf#source) columns respectively,
- additional data can be supplied in additional columns.


## Example

See https://github.com/cldf-datasets/wals/blob/master/cldf/values.csv

```csv
ID,Language_ID,Parameter_ID,Value,Code_ID,Comment,Source,Example_ID
81A-aab,aab,81A,2,81A-2,,Nekitel-1985[94],
82A-aab,aab,82A,1,82A-1,,Nekitel-1985[94],
83A-aab,aab,83A,2,83A-2,,Nekitel-1985[94],
87A-aab,aab,87A,2,87A-2,,Nekitel-1985[95],
88A-aab,aab,88A,2,88A-2,,Nekitel-1985[95],
89A-aab,aab,89A,2,89A-2,,Nekitel-1985[95],
92A-aab,aab,92A,2,92A-2,,Nekitel-1985[99],
93A-aab,aab,93A,2,93A-2,,Nekitel-1985[100],
97A-aab,aab,97A,4,97A-4,,,
112A-aab,aab,112A,2,112A-2,,Nekitel-1985[passim],
...
```


## Multi-dimensional features

Multi-dimensional features are useful to model data like paradigms. 
To support multi-dimensional features, we specify a standard separator for 
`Parameter_ID` components: `~`. 
I.e. a local feature ID for a multi-dimensional feature can be coded as
```
Language_ID Feature_ID Value
deu         Sg~1P     ich
deu         Pl~1P     wir
```