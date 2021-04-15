# Entries

When dictionaries or lexicons are encoded using CLDF's `Dictionary` module,
each entry (a.k.a. headword, lemma, lemon's [LexicalEntry](http://lemon-model.net/lemon#LexicalEntry)) is stored as a row in the `EntryTable`.

## [EntryTable](http://cldf.clld.org/v1.0/terms.rdf#EntryTable): `entries.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | singlevalued | <div> <p> An identifier referencing a language either </p> <ul> <li>by providing a foreign key into the LanguageTable or</li> <li>by using a known encoding scheme.</li> </ul> </div> <br>References LanguageTable
[Headword](http://cldf.clld.org/v1.0/terms.rdf#headword) | `string` | singlevalued | <div> <p> The headword of a dictionary entry. </p> </div> 
[Part_Of_Speech](http://cldf.clld.org/v1.0/terms.rdf#partOfSpeech) | `string` | unspecified | <div> <p> The part-of-speech of dictionary entry. </p> </div> 