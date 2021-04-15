# Senses

When dictionaries or lexicons are encoded using CLDF's `Dictionary` module,
each entry may be related to multiple senses (lemon's [LexicalSense](http://lemon-model.net/lemon#LexicalSense)) stored as rows in the `SenseTable`.

## [SenseTable](http://cldf.clld.org/v1.0/terms.rdf#SenseTable): `senses.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | unspecified | <div> <p>A description for an entity.</p> </div> 
[Entry_ID](http://cldf.clld.org/v1.0/terms.rdf#entryReference) | `string` | unspecified | <div> <p> An identifier referencing a dictionary entry by providing a foreign key into the EntryTable. </p> </div> <br>References EntryTable