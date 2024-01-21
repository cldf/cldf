# Values

The core data of a CLDF [`StructureDataset`](../../modules/StructureDataset) is the list of values 
(a.k.a. measurements or datapoints). Each value is stored as a separate row in the `Vauetable`, 
providing, at the least, the following columns:
 
- [`id`](http://cldf.clld.org/v1.0/terms.rdf#id): A unique identifier for the row within the table.
- [`languageReference`](http://cldf.clld.org/v1.0/terms.rdf#languageReference): A reference to a language (or variety) the form belongs to.
- [`parameterReference`](http://cldf.clld.org/v1.0/terms.rdf#parameterReference): A reference to the meaning denoted by the form.
- [`value`](http://cldf.clld.org/v1.0/terms.rdf#value): The measurement.

For categorical variables, it is often useful to supply the list of valid values using a 
[`CodeTable`](../codes). In this case, a [`codeReference`](http://cldf.clld.org/v1.0/terms.rdf#codeReference) column in the `ValueTable` should be used to
link value to code.

As with any CLDF component, 
- comments and references to sources can be added via
[`comment`](http://cldf.clld.org/v1.0/terms.rdf#comment) and [`source`](http://cldf.clld.org/v1.0/terms.rdf#source) columns respectively,
- additional data can be supplied in additional columns.

For a way to store typed data as values, see the description of [`ParameterTable`](../parameters).


## Example

The [`ValueTable` of the World Atlas of Language Structures](https://github.com/cldf-datasets/wals/blob/v2020.2/cldf/values.csv)
is described here: https://github.com/cldf-datasets/wals/blob/v2020.2/cldf/StructureDataset-metadata.json#L45-L110 

> [!NOTE]
> In addition to the default columns, the WALS `ValueTable` also contains an [`exampleReference`](http://cldf.clld.org/v1.0/terms.rdf#exampleReference) column,
> linking a value to an example (if available) to illustrate the coding.
