# Entries

When dictionaries or lexicons are encoded using CLDF's `Dictionary` module,
each entry (a.k.a. headword, lemma, lemon's [LexicalEntry](http://lemon-model.net/lemon#LexicalEntry)) is stored as a row in the `EntryTable`.

## [EntryTable](http://cldf.clld.org/v1.0/terms.rdf#EntryTable): `entries.csv`

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | 
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References LanguageTable
[Headword](http://cldf.clld.org/v1.0/terms.rdf#headword) | `string` | 
[Part_Of_Speech](http://cldf.clld.org/v1.0/terms.rdf#partOfSpeech) | `string` | 