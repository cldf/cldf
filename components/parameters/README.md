# Parameters

Obviously, cross-linguistic data often compares languages using comparative concepts,
e.g. typological features like in WALS, or Swadesh terms as in many wordlists.

While it may sometimes be enough to refer to such a concept by ID, e.g.
using a value like `116A` as 
[`parameterReference`](http://cldf.clld.org/v1.0/terms.rdf#parameterReference)
to refer to [WALS feature 116A](http://wals.info/feature/116A)
in a [Structure Dataset](../../modules/StructureDataset), often additional metadata
must be provided. This should be done in CLDF datasets by including a
data file `parameters.csv` or a table with `"dc:conformsTo": "http://cldf.clld.org/v1.0/terms.rdf#ParameterTable"`, and pointing to rows in this table
using the [`parameterReference`](http://cldf.clld.org/v1.0/terms.rdf#parameterReference)
property.

## [ParameterTable](http://cldf.clld.org/v1.0/terms.rdf#ParameterTable): `parameters.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | unspecified | <div> <p>A title, name or label for an entity.</p> </div> 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | unspecified | <div> <p>A description for an entity.</p> </div> 