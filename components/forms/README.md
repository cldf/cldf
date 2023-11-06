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

## [FormTable](https://cldf.clld.org/v1.0/terms.rdf#FormTable): `forms.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](https://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Language_ID](https://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | singlevalued | A reference to a language (or variety) the form belongs to<br>References LanguageTable
[Parameter_ID](https://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | unspecified | A reference to the meaning denoted by the form<br>References ParameterTable
[Form](https://cldf.clld.org/v1.0/terms.rdf#form) | `string` | singlevalued | The written expression of the form. If possible the transcription system used for the written form should be described in CLDF metadata (e.g. via adding a common property `dc:conformsTo` to the column description using concept URLs of the GOLD Ontology (such as [phonemicRep](http://linguistics-ontology.org/gold/2010/phonemicRep) or [phoneticRep](http://linguistics-ontology.org/gold/2010/phoneticRep)) as values).
[Segments](https://cldf.clld.org/v1.0/terms.rdf#segments) | list of `string` (separated by ` `) | multivalued | <div> <p> A list of segments (aka a sound sequence) is understood as the strict segmental representation of a <a href="http://linguistics-ontology.org/gold/2010/FormUnit">form unit</a> of a language, which is usually given in phonetic transcription. <a href="http://linguistics-ontology.org/gold/2010/Suprasegmental">Suprasegmental elements</a>, like tone or accent, of sound sequences are usually represented in a sequential form, although they are usually co-articulated along with the segmental elements of a sound sequence. Alternatively, suprasegmental aspects could also be represented as part of the <a href="#prosodicStructure">prosodic structure</a> of a word form. </p> </div> 
[Comment](https://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | unspecified | <div> <p> A human-readable comment on a resource, providing additional context. </p> </div> 
[Source](https://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | multivalued | <div> <p>List of source specifications, of the form &lt;source_ID&gt;[], e.g. http://glottolog.org/resource/reference/id/318814[34], or meier2015[3-12] where meier2015 is a citation key in the accompanying BibTeX file.</p> </div> 