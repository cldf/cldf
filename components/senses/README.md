# Senses

When dictionaries or lexicons are encoded using CLDF's `Dictionary` module,
each entry may be related to multiple senses (lemon's [LexicalSense](http://lemon-model.net/lemon#LexicalSense)) stored as rows in the `SenseTable`.

## [SenseTable](http://cldf.clld.org/v1.0/terms.rdf#SenseTable): `senses.csv`

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Entry_ID](http://cldf.clld.org/v1.0/terms.rdf#entryReference) | `string` | References EntryTable