# Dictionary Module

In CLDF dictionaries are marked by a common property `dc:conformsTo` with value
[`http://cldf.clld.org/v1.0/terms.rdf#Dictionary`](http://cldf.clld.org/v1.0/terms.rdf#Dictionary)
on a `TableGroup`.

A simple dictionary (e.g. for publication in [Dictionaria](http://dictionaria.clld.org)) 
is a set of two tables, in CLDF represented by the two related components
- [`EntryTable`](../../components/entries) and
- [`SenseTable`](../../components/senses)

The sense table contains all the senses which are represented in the
dictionary. Each sense is linked to exactly one entry, but entries may
have multiple senses linked to them (e.g. German /spinnen/ 1. ‘spin’ 2.
‘be crazy’). There is thus a many-to-one relationship between senses and
entries.

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

A CLDF dictionary may have an [examples component](../../components/examples),
which contains all the examples which are represented in the
dictionary. Each example is linked to one or more senses, and senses may
have multiple examples linked to them. There is thus a many-to-many
relationship between examples and senses. 
