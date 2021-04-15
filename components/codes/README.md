# Codes

Often cross-linguistic data contains data for 
[categorical variables](https://en.wikipedia.org/wiki/Categorical_variable) that categorise the 
variable into a set of distinct states. For example [WALS feature 27A](http://wals.info/feature/27A) 
categorizes languages according to their strategy for reduplication into
- A. Productive full and partial reduplication
- B. Full reduplication only
- C. No productive reduplication

Specifying the range of possible category states (e.g. "A", "B", and "C" in the example above) 
for a given parameter is useful for error checking. Or if a subset of the data do not exhibit 
all possibilities, then this provides a way to document the full range of possibilities.

This specification can be done by adding a codes table with the default description
[`CodeTable-metadata.json`](CodeTable-metadata.json).

In a structure dataset's `ValueTable` the codes can be referenced using a foreign
key `Code_ID`.

## [CodeTable](http://cldf.clld.org/v1.0/terms.rdf#CodeTable): `codes.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | singlevalued | The parameter or variable the code belongs to.<br>References ParameterTable
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | unspecified | <div> <p>A title, name or label for an entity.</p> </div> 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | unspecified | <div> <p>A description for an entity.</p> </div> 