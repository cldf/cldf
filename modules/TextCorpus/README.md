# Text Corpus

Texts can roughly be defined as cohesive stretches of discourse in the object language. They are
part of the Boasian triad, and fundamental to corpus-based language description.

In CLDF text corpora are marked by a common property `dc:conformsTo` with value
[`http://cldf.clld.org/v1.0/terms.rdf#TextCorpus`](http://cldf.clld.org/v1.0/terms.rdf#TextCorpus)
on a `TableGroup`.

Text Corpora require only an [`ExampleTable`](../../components/examples), listing the lines of text.


## Multiple texts

But typically a corpus will contain multiple texts. In this case, metadata about the texts should
be given as rows of a `ContributionTable` with the `name` property specifying the title of a text.
Lines of text should be linked to a text using a `contributionReference` property in `ExampleTable`.


## Ordering

While an ordering of the lines in the texts may be conveyed implicitly via the order of rows in
`ExampleTable`, it is recommended to be more explicit and use a property [`position`](http://cldf.clld.org/v1.0/terms.rdf#TextCorpus) on `ExampleTable`.
The `position` property may also be list-valued, thus specifying a multi-level ordering, e.g. to
group lines into texts and paragraphs within texts.


## Alternative Translations

Often, text corpora contain translations of the object language into more than one other language,
e.g. corpora for languages that are spoken in areas where the primary lingua franca is not English.
In such cases, the translations should be given as `translatedText` properties of multiple "copies"
of the object language text. The complete line, including glossing, should contain the translation
(and corresponding `metaLanguageReference`) for the language that is also used as meta language in
the annotations. The "copies" should copy the `primaryText` property but **not** `analyzedWord` or 
`gloss` and link to the source line using a `exampleReference` property.

ID | Primary_Text | Analyzed_Word                          | Gloss | Translated_Text                 | Meta_Language_ID | Full_Example
---|--------------|----------------------------------------|-------|---------------------------------|------------------|---
1-de | nicchihuilia in nopiltzin ce calli | ni-c-chihui-lia in no-piltzin ce calli | 1SG.SUBJ-3SG.OBJ-mach-APPL DET 1SG.POSS-Sohn ein Haus | Ich machte meinem Sohn ein Haus | stan1295         |
1-eng | nicchihuilia in nopiltzin ce calli | | | I made my son a house           | stan1293         | 1-de
