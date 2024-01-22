# Entries

When dictionaries or lexicons are encoded using CLDF's `Dictionary` module,
each entry (a.k.a. headword, lemma, lemon's [LexicalEntry](http://lemon-model.net/lemon#LexicalEntry)) is stored as a row in the `EntryTable`.


## Example

The `EntryTable` of the [Daakaka dictionary](https://dictionaria.clld.org/contributions/daakaka#tabout) is described here: 
https://github.com/dictionaria/daakaka/blob/v1.3/cldf/cldf-metadata.json#L45-L162
Like most dictionaries collected in Dictionaria, it provides a lot more information for each entry
than what is covered by the CLDF's default `EntryTable`, e.g. [encyclopedic information](https://dictionaria.clld.org/contributions/daakaka#twords2).
