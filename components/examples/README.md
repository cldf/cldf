# Examples

Often, cross-linguistic data comes with examples, i.e. sentence-sized chunks of
text used to exemplify a statement about a language; e.g. showing
- usage of a particular lexeme in a language or
- existence of a particular construction.

Such examples have two basic properties: Text in the primary language and a
translation into a target language.

Often examples are glossed using
[Interlinear glossed text](http://en.wikipedia.org/wiki/Interlinear_gloss) 
according to the [Leipzig Glossing Rules](http://www.eva.mpg.de/lingua/resources/glossing-rules.php). In this case, the example is extended
with two properties: The aligned primary text and aligned glosses.

The default description of the example table is available in 
[*ExampleTable-metadata.json*](ExampleTable-metadata.json).

Rows in the example table can then be referenced from other tables using a
[`exampleReference`](http://cldf.clld.org/v1.0/terms.rdf#exampleReference) property.

Note that words in gloss and aligned text may be further split into morphemes and clitics using `-` and `=` as separators according to the 
[Leipzig Glossing Rules](http://www.eva.mpg.de/lingua/resources/glossing-rules.php).
Thus, `-` and `=` must not be used for the separator property of the corresponding column.

Often, examples are glossed incompletely, e.g. leaving out person or place names or unparsable words.
In such cases it is recommended to consistently use U+2026 - i.e. `…`, the [Unicode character "ellipsis"](https://en.wikipedia.org/wiki/Ellipsis) -
in `Analyzed_Word` and `Gloss`.


## Grammaticality judgements

Sometimes it is useful to provide "ungrammatical" examples, i.e. sentences or phrases that are
grammatically incorrect. Typically, this is marked using some typographical symbols to convey the
[grammaticality judgement](https://github.com/cysouw/pandoc-ling?tab=readme-ov-file#the-basic-structure-of-a-linguistic-example).

In CLDF, ungrammatical examples MUST
- have a non-empty [`grammaticalityJudgement`](http://cldf.clld.org/v1.0/terms.rdf#grammaticalityJudgement) value, namely
  the typographical marker to be used for the example,
- link (via `languageReference`) to special item(s) in `LanguageTable` with an empty `Glottocode` to
  prevent data aggregators from inadvertently assigning such an example to a proper language
  (if they fail to honour `grammaticalityJudgement`).


## Editing examples

The CSV format for examples specified above is not particularly suited for editing
in particular not for interlinear glosses. The tool most often used for glossing
examples seems to be the *Field Linguist's Toolbox* (aka *Toolbox*) or successors
thereof. It should be noted, though, that conversion of CSV examples to and from
a format that can be read and edited by Toolbox is very simple. We basically have
to map the columns in the CSV specification to Toolbox markers. So, considering
a Toolbox example like
```
\ref xv1
\tx vyanten ente mwi abwilyep
\mb vyanten en=te mw=i abwilyep
\gl person $dem=$dem.med mw=i abwilyep
\ft this man is a sorcerer
```
(which uses markers as exported from tools like ELAN), we would map 
- `ID` to `\ref`
- `Primary` to `\tx`
- `Analyzed` to `\mb`
- `Gloss` to `\gl`
- `Translation` to `\ft`


## Example

The [examples](https://github.com/cldf-datasets/lgr/blob/v1.0/cldf/examples.csv) used in the 
[Leipzig Glossing Rules](https://doi.org/10.5281/zenodo.10275705) document are available as CLDF dataset. The
`ExampleTable` is described here: https://github.com/cldf-datasets/lgr/blob/v1.0/cldf/Generic-metadata.json#L43-L137

## [ExampleTable](http://cldf.clld.org/v1.0/terms.rdf#ExampleTable): `examples.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | singlevalued | <div> <p> An identifier referencing a language either </p> <ul> <li>by providing a foreign key to <code>LanguageTable</code> or</li> <li>by using a known encoding scheme.</li> </ul> </div> <br>References <code>LanguageTable</code>
[Primary_Text](http://cldf.clld.org/v1.0/terms.rdf#primaryText) | `string` | singlevalued | The example text in the source language.
[Analyzed_Word](http://cldf.clld.org/v1.0/terms.rdf#analyzedWord) | list of `string` (separated by `	`) | multivalued | The sequence of words of the primary text to be aligned with glosses
[Gloss](http://cldf.clld.org/v1.0/terms.rdf#gloss) | list of `string` (separated by `	`) | multivalued | The sequence of glosses aligned with the words of the primary text
[Translated_Text](http://cldf.clld.org/v1.0/terms.rdf#translatedText) | `string` | singlevalued | The translation of the example text in a meta language
[Meta_Language_ID](http://cldf.clld.org/v1.0/terms.rdf#metaLanguageReference) | `string` | singlevalued | References the language of the translated text<br>References <code>LanguageTable</code>
[LGR_Conformance](http://cldf.clld.org/v1.0/terms.rdf#lgrConformance) | `string` | singlevalued | The level of conformance of the example with the Leipzig Glossing Rules
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | unspecified | <div> <p> A human-readable comment on a resource, providing additional context. </p> </div> 