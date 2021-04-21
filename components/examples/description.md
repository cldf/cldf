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
[`ExampleTable-metadata.json`](ExampleTable-metadata.json).

Rows in the example table can then be referenced from other tables using a
[`exampleReference`](http://cldf.clld.org/v1.0/terms.rdf#exampleReference) property.

Note that words in gloss and aligned text may be further split into morphemes and clitics using `-` and `=` as separators according to the 
[Leipzig Glossing Rules](http://www.eva.mpg.de/lingua/resources/glossing-rules.php).
Thus, `-` and `=` must not be used for the separator property of the corresponding column.


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

See https://github.com/dictionaria/daakaka/blob/master/cldf/examples.csv

```csv
ID,Language_ID,Primary_Text,Analyzed_Word,Gloss,Translated_Text,Meta_Language_ID,Comment,Corpus_Reference,Sense_IDs,alt_translation1
XV000001,bpa,vyanten ente mwi abwilyep,vyanten\ten=te\tmw=i\tabwilyep,person\t$dem=$dem.med\tmw=i\tabwilyep,this man is a sorcerer,,,,SN000011,man ia i wan poson man
XV000002,bpa,mesyu abwilyep swa sa ngetak,mesyu\tabwilyep\tswa\tsa\tnge=tak,fish\tpoisonous\tone\t$top\t$3sg=$dem.prox,this is a poisonous fish,,,,SN000012 ; SN001614,wan poson fis hem ia
XV000003,bpa,nam akuorkote seli,na=m\takuor-kote\tseli,$1sg=$real\tcross-in.two\troad,I crossed the road,,,,SN000020 ; SN001408,mi krosem road
...
```
