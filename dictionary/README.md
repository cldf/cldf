# Dictionary Module

A simple dictionary (e.g. for publication in [Dictionaria](http://dictionaria.clld.org)) is a set of three tables.

## Entries

Dictionary entries must be stored as rows in a CSV file either named `entries.csv` or specified as table with 
common property `"dc:type": "dictionaria:entries"` in the metadata file.

Each entry row must contain information in the following three columns:

* `ID`: a unique alphanumeric code, chosen arbitrarily
* `headword`: lemma, or citation form
* `part-of-speech`

In addition, some optional standard columns are recognized:

* lemma in original script
* pronunciation of lemma
* variant form
* general comments
* bibliographical references (list of bibref IDs)
* etymological origin
* source language (for loanwords) 
* source word (for loanwords)
* sound file ID

Entries may have additional language-specific fields, e.g.

* gender
* inflectional class
* form in divergent dialect X
* sociolinguistic information such as literary vs. colloquial, obsolete, taboo, etc.

Finally, an entry can contain (standard or language-specific)
*association fields*, i.e. fields that establish a relationship between
the entry and some other entry. The content of an association field is a
list of entry IDs. The name of an association field is relational, i.e.
it is a transitive or copula verb or ends in a preposition, e.g.

`FIXME`: Specify syntax for column names of association fields!

* it contains*(list of entry IDs)
* it is part of*(list of entry IDs)
* its causative is*(list of entry IDs)
* its numeral classifier is*(list of entry IDs)

## Senses

The sense table contains all the senses which are represented in the
dictionary. Each sense is linked to exactly one entry, but entries may
have multiple senses linked to them (e.g. German /spinnen/ 1. ‘spin’ 2.
‘be crazy’). There is thus a many-to-one relationship between senses and
entries.

Each sense must minimally contain information in the following
three fields (again, the ID is a code that can be chosen arbitrarily):

* `ID`
* `description`: sense description (= list of semicolon-delimited sense descriptors)
* `entry_ID`: ID of related entry

standard fields:

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

The example table contains all the examples which are represented in the
dictionary. Each example is linked to one or more senses, and senses may
have multiple examples linked to them. There is thus a many-to-many
relationship between examples and senses.

Each example must minimally contain information in the following
four fields:

* `ID`
* `primary_text`
* `translation`
* `sense_ID`: semicolon-separated list of IDs of related senses (this is a list, not a single ID,
because an example may illustrate several senses)
 

standard fields:

* analyzed text (including hyphens between morphemes, or more abstract morphophonological representation)
* literal translation 
* name of speaker who provided the example
* date
