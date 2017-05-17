# Dictionary specification for CLDF

(the following were basic information I received from @haspelmath, please feel free to edit further)

## (1) The entry table*

Each entry must contain information in the following three fields:

 

* (entry) ID (a unique alphanumeric code, chosen arbitrarily)
* headword (= lemma, or citation form)
* part-of-speech

### standard fields:

* lemma in original script
* pronunciation of lemma
* variant form
* general comments
* bibliographical references (list of bibref IDs)
* etymological origin
* source language (for loanwords) 
* source word (for loanwords)
* sound file ID

### language-specific fields (some examples):

* gender
* inflectional class
* form in divergent dialect X
* sociolinguistic information such as literary vs. colloquial, obsolete, taboo, etc.
 
Finally, an entry can contain (standard or language-specific)
*association fields*, i.e. fields that establish a relationship between
the entry and some other entry. The content of an association field is a
list of entry IDs. The name of an association field is relational, i.e.
it is a transitive or copula verb or ends in a preposition, e.g.


* it contains*(list of entry IDs)
* it is part of*(list of entry IDs)
* its causative is*(list of entry IDs)
* its numeral classifier is*(list of entry IDs)

## (2) The sense table

The sense table contains all the senses which are represented in the
dictionary. Each sense is linked to exactly one entry, but entries may
have multiple senses linked to them (e.g. German /spinnen/ 1. ‘spin’ 2.
‘be crazy’). There is thus a many-to-one relationship between senses and
entries.

Each sense must minimally contain information in the following
three fields (again, the ID is a code that can be chosen arbitrarily):

* (sense) ID
* sense description (= list of semicolon-delimited sense descriptors)
* ID of related entry

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


## (3) The example table
 

The example table contains all the examples which are represented in the
dictionary. Each example is linked to one or more senses, and senses may
have multiple examples linked to them. There is thus a many-to-many
relationship between examples and senses.

Each example must minimally contain information in the following
four fields:

 

* (example) ID
* primary text
* translation
* list of IDs of related senses (this is a list, not a single ID,
because an example may illustrate several senses)
 

standard fields:

* analyzed text (including hyphens between morphemes, or more abstract morphophonological representation)
* literal translation 
* name of speaker who provided the example
* date
