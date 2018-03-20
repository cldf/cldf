## Forms

Forms, i.e. written denotations of the linguistic sign (cf. [GOLD's FormUnit](http://linguistics-ontology.org/gold/2010/FormUnit)), are stored in a
`FormTable` in CLDF datasets (typically `Wordlist`s).

Each form is stored as a separate row in this table, providing, at the least, the following columns:
 
- [ID](http://cldf.clld.org/v1.0/terms.rdf#id): A unique identifier for the row within the table.
- [Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference): A reference to a language (or variety) the form belongs to.
- [Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference): A reference to the meaning denoted by the form.
- [Form](http://cldf.clld.org/v1.0/terms.rdf#form): The written expression of the form.
 
Some analyses, e.g. alignments, require segmented lexical forms. If these can be supplied, they should be added in a [Segments](http://cldf.clld.org/v1.0/terms.rdf#segments) column, by default as space-separated strings.

As with any CLDF component, 
- comments and references to sources can be added via
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) and [Source](http://cldf.clld.org/v1.0/terms.rdf#source) columns respectively,
- additional data can be supplied in additional columns.
