# Senses

When dictionaries or lexicons are encoded using CLDF's `Dictionary` module,
each entry may be related to multiple senses (lemon's [LexicalSense](http://lemon-model.net/lemon#LexicalSense)) stored as rows in the `SenseTable`.


## Example

See https://github.com/dictionaria/iquito/blob/main/cldf/senses.csv

```csv
ID,Description,Entry_ID,Anthropology_Note,Grammar_Note,Scientific_Name,Sociolinguistics_Note
SN000001,"play a trick on someone, joke with someone by deceiving them or deliberately lying to them",LX000001,,,,
SN000002,play with,LX000001,,,,
SN000003,alone,yaajaa,,,,
SN000004,the.same,yaajaa,,,,
SN000005,thigh,LX000002,,Poss.pref,,
SN000006,leg,LX000002,,"In this sense, ‘thigh’ serves as a metonym for the entire limb. Poss.pref",,
SN000007,"his, her, or its thigh",LX000003,,,,
SN000008,"his, her, or its leg",LX000003,,,,
SN000009,vulva,LX000004,,Poss.pref,,
...
```
## [SenseTable](http://cldf.clld.org/v1.0/terms.rdf#SenseTable): `senses.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | unspecified | <div> <p>A description for an entity.</p> </div> 
[Entry_ID](http://cldf.clld.org/v1.0/terms.rdf#entryReference) | `string` | unspecified | <div> <p> An identifier referencing a dictionary entry by providing a foreign key into the EntryTable. </p> </div> <br>References EntryTable