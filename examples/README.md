# CLDF Examples

## A WALS feature as CLDF structure dataset

[Feature 1A of WALS Online](http://wals.info/feature/1A), converted to a CLDF StructureDataset is available at [`wals_1A_cldf`](wals_1A_cldf). This dataset
has been created using the code and instructions at https://github.com/glottobank/pycldf/tree/master/examples

One of the design goals of CLDF was to make re-use of existing tools for linguistic data possible. As an example, we can convert the CLDF
dataset to the legacy custom tab-delimited export of WALS features (e.g.
http://wals.info/feature/1A.tab), using tools from the [`csvkit` package](https://csvkit.readthedocs.io/):
- We use `csvjoin` three, to augment the `ValueTable` with metadata about languages, 
  parameters and feature values.
- The we use `csvcut` to prune the excess columns and re-order the remaining ones.
- Using `sed` we replace the first line, thereby renaming the columns.
- Finally we use `csvformat` to switch to tab-delimited values.

```bash
$ csvjoin -c Language_ID,ID values.csv languages.csv \
| csvjoin -c Parameter_ID,ID - parameters.csv \
| csvjoin -c Code_ID,ID - codes.csv \
| csvcut -c 2,9,4,25,11,12,15,16,22 \
| sed "1s/.*/wals code,name,value,description,latitude,longitude,genus,family,area/" \
| csvformat -T \
| head -n 5
wals code	name	value	description	latitude	longitude	genus	family	area
abi	Abipón	2	Moderately small	-29.0	-61.0	South Guaicuruan	Guaicuruan	Phonology
abk	Abkhaz	5	Large	43.0833333333	41.0	Northwest Caucasian	Northwest Caucasian	Phonology
ach	Aché	1	Small	-25.25	-55.1666666667	Tupi-Guaraní	Tupian	Phonology
acm	Achumawi	2	Moderately small	41.5	-121.0	Palaihnihan	Hokan	Phonology
```

## A Wordlist with cognate judgements

The directory [`wordlist`](wordlist) contains an example of a CLDF Wordlist,
including cognates and partial cognates.

A first inspection with the `cldf stats` command from the `pycldf` package reveals:

```bash
$ cldf stats Wordlist-metadata.json
<cldf:v1.0:Wordlist at ../../glottobank/cldf/examples/wordlist>
key            value
-------------  --------------------------------------------
dc:conformsTo  http://cldf.clld.org/v1.0/terms.rdf#Wordlist

Path                 Type                     Rows
-------------------  ---------------------  ------
forms.csv            Form Table               1825
cognates.csv         Cognate Table            1825
partialcognates.csv  Partial Cognate Table    2531
sources.bib          Sources                     2
```

Again, we can use the tools from the `csvkit` package, e.g. to show the
alignments for all cognate sets for a particular concept:

```bash
$ csvjoin -c Form_ID,ID cognates.csv forms.csv \
| csvsort -c Concept,Cognateset_ID,Language - \
| csvcut -c Concept,Cognateset_ID,Alignment,Language - \
| csvgrep -c Concept -m "the skin" \
| csvformat -T
Concept	Cognate_set_ID	Alignment	Language
the skin	2	ʃ ɔ̆ ³⁵ + j a m ⁵⁵	Maru
the skin	3	a ³¹ - + ʐ ɿ - ⁵⁵	Achang_Longchuan
the skin	3	- - a + r i j -	Old_Burmese
the skin	3	a ³¹ - + ʐ ɿ - ⁵⁵	Xiandao
the skin	204	ʃ ŏ ²¹ + k ṵ - ʔ ⁵⁵	Atsi
the skin	204	ʃ ă ³⁵ + k a̰ u ʔ ⁵⁵	Bola
the skin	204	ʃ ŏ ⁵⁵ + k ṵ - k ⁵⁵	Lashi
the skin	343	ɑ ⁵³ + tθ ɑ ⁵⁵ + ɑ ⁵³ + j e ²²	Rangoon
```


## Examples "in the wild"

- http://doi.org/10.5281/zenodo.886179
