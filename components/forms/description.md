# Forms

Forms, i.e. written denotations of the linguistic sign (cf. [GOLD's FormUnit](http://linguistics-ontology.org/gold/2010/FormUnit)), are stored in a
`FormTable` in CLDF datasets (typically `Wordlist`s).

Each form is stored as a separate row in this table.
Some analyses, e.g. alignments, require segmented lexical forms. 
If these can be supplied, they should be added in a [Segments](https://cldf.clld.org/v1.0/terms.rdf#segments) column, by default as space-separated strings.

The CLDF Ontology provides some more properties which may be supplied in corresponding columns of the `FormTable`:
- [Motivation_Structure](https://cldf.clld.org/v1.0/terms.rdf#motivationStructure)
- [Prosodic_Structure](https://cldf.clld.org/v1.0/terms.rdf#prosodicStructure)
- [Root](https://cldf.clld.org/v1.0/terms.rdf#root)
- [Stem](https://cldf.clld.org/v1.0/terms.rdf#stem)

A [Value](https://cldf.clld.org/v1.0/terms.rdf#value) column may be used to supply the raw value as it can be found in the source - if this is different
from `Form`. This is particularly useful for "retro-digitized" datasets, where
the CLDF dataset is already the result of data clean-up.

As with any CLDF component, 
- comments and references to sources can be added via
[Comment](https://cldf.clld.org/v1.0/terms.rdf#comment) and [Source](https://cldf.clld.org/v1.0/terms.rdf#source) columns respectively,
- additional data can be supplied in additional columns.


## Example

See https://github.com/intercontinental-dictionary-series/lindseyende/blob/master/cldf/forms.csv

```csv
ID,Local_ID,Language_ID,Parameter_ID,Value,Form,Segments,Comment,Source,Cognacy,Loan,Graphemes,Profile,Transcriptions,AlternativeValues
ende1235-1-100-1,,ende1235,1-100,ekaklle ulle,ekaklle ulle,e k a k ɽ e + u ɽ e,,lindsey2019,,,^ e k a k ll e + u ll e $,default,StandardOrth;Phonetic,ekakɽe uɽe
ende1235-1-210-1,,ende1235,1-210,ekaklle,ekaklle,e k a k ɽ e,,lindsey2019,,,^ e k a k ll e $,default,StandardOrth;Phonetic,ekakɽe
ende1235-1-212-1,,ende1235,1-212,ekaklle,ekaklle,e k a k ɽ e,"also: täpe, matu",lindsey2019,,,^ e k a k ll e $,default,StandardOrth;Phonetic,ekakɽe
ende1235-1-213-1,,ende1235,1-213,pänpän,pänpän,p ə n p ə n,,lindsey2019,,,^ p ä n p ä n $,default,StandardOrth;Phonetic,pənpən
...
```
