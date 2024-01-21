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

## [ValueTable](http://cldf.clld.org/v1.0/terms.rdf#ValueTable): `values.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | singlevalued | <div> <p> An identifier referencing a language either </p> <ul> <li>by providing a foreign key to <code>LanguageTable</code> or</li> <li>by using a known encoding scheme.</li> </ul> </div> <br>References <code>LanguageTable</code>
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | singlevalued | <div> <p> An identifier referencing a parameter either </p> <ul> <li>by providing a foreign key to <code>ParameterTable</code> or</li> <li>by using a known encoding scheme.</li> </ul> </div> <br>References <code>ParameterTable</code>
[Value](http://cldf.clld.org/v1.0/terms.rdf#value) | `string` | singlevalued | <div> <p> The value (a.k.a. datapoint or measurement) of a language for a structural feature. </p> <p> For features with a limited, discrete set of valid values (a.k.a. categorical variables) it is recommended to relate items of <code>ValueTable</code> to the respective code in <code>CodeTable</code>. </p> </div> 
[Code_ID](http://cldf.clld.org/v1.0/terms.rdf#codeReference) | `string` | singlevalued | <div> <p> An identifier referencing a code (aka category) description by providing a foreign key to <code>CodeTable</code>. </p> </div> <br>References <code>CodeTable</code>
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | unspecified | <div> <p> A human-readable comment on a resource, providing additional context. </p> </div> 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | multivalued | <div> <p>List of source specifications, of the form &lt;source_ID&gt;[], e.g. http://glottolog.org/resource/reference/id/318814[34], or meier2015[3-12] where meier2015 is a citation key in the accompanying BibTeX file.</p> </div> 