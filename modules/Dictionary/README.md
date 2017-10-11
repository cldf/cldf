# Dictionary Module

A simple dictionary (e.g. for publication in [Dictionaria](http://dictionaria.clld.org)) is a set of two tables.

## Entries

Dictionary entries must be stored as rows in a CSV file either named `entries.csv` or specified as table with 
common property 
```
"dc:conformsTo": "http://cldf.clld.org/v1.0/terms.rdf#EntryTable"
``` 
in the metadata file.

Each entry row must contain information in the following three columns:

* [`ID`](http://cldf.clld.org/v1.0/terms.rdf#id): a unique alphanumeric code, chosen arbitrarily
* [`headword`](http://cldf.clld.org/v1.0/terms.rdf#headword): lemma, or citation form
* [`part_of_speech`](http://cldf.clld.org/v1.0/terms.rdf#partOfSpeech)


## Senses

The sense table contains all the senses which are represented in the
dictionary. Each sense is linked to exactly one entry, but entries may
have multiple senses linked to them (e.g. German /spinnen/ 1. ‘spin’ 2.
‘be crazy’). There is thus a many-to-one relationship between senses and
entries.

Senses must be stored as rows in a CSV file either named `senses.csv` or specified as table with 
common property 
```
"dc:conformsTo": "http://cldf.clld.org/v1.0/terms.rdf#SenseTable"
``` 
in the metadata file.

Each sense must minimally contain information in the following
three fields (again, the ID is a code that can be chosen arbitrarily):

* [`ID`](http://cldf.clld.org/v1.0/terms.rdf#id)
* [`Description`](http://cldf.clld.org/v1.0/terms.rdf#description): sense description (= list of semicolon-delimited sense descriptors)
* [`Entry_ID`](http://cldf.clld.org/v1.0/terms.rdf#entryReference): ID of related entry

Often, the sense table contains also

* list of comma-delimited semantic domains*
* scientific name (for plant and animal species)*
* comments on sense*
* bibliographical references *(list of bibref IDs)
* sense description in the object language*

language-specific fields (e.g.)

* sense description in language X

Like entries, senses can contain fields for associated senses, e.g.

* synonymous with (list of sense IDs)
* antonymous with (list of sense IDs)


## Examples

A CLDF dictionary may have an [examples component](../../components/examples/README.md),
which contains all the examples which are represented in the
dictionary. Each example is linked to one or more senses, and senses may
have multiple examples linked to them. There is thus a many-to-many
relationship between examples and senses. The links between examples
and senses must be specified in a column
* `sense_ID`: semicolon-separated list of IDs of related senses

in the examples table.
