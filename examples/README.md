# CLDF Examples

## Examples for testing

Small toy examples for testing implementations of the specification are available from the `pycldf` test suite at
https://github.com/cldf/pycldf/tree/master/tests/data


## A WALS feature as CLDF structure dataset

[Feature 1A of WALS Online](http://wals.info/feature/1A), converted to a CLDF StructureDataset is available at [`wals_1A_cldf`](wals_1A_cldf). This dataset
has been created using the code and instructions in the [pycldf repository](https://github.com/cldf/pycldf/tree/master/examples).

One of the design goals of CLDF was to make re-use of existing tools for linguistic data possible. As an example, we can convert the CLDF
dataset to the legacy custom tab-delimited export of WALS features (e.g.
http://wals.info/feature/1A.tab), using tools from the [`csvkit` package](https://csvkit.readthedocs.io/):
- We use `csvjoin` three times, to augment the `ValueTable` with metadata about languages, 
  parameters and feature values.
- The we use `csvcut` to prune the excess columns and re-order the remaining ones.
- Using `sed` we replace the first line, thereby renaming the columns.
- Finally we use `csvformat` to switch to tab-delimited values.

```shell
$ csvjoin -c Language_ID,ID wals_1A_cldf/values.csv wals_1A_cldf/languages.csv \
| csvjoin -c Parameter_ID,ID - wals_1A_cldf/parameters.csv \
| csvcut -C Name2 \
| csvjoin -c Code_ID,ID - wals_1A_cldf/codes.csv \
| csvcut -c Language_ID,Name,Value,Name2,Latitude,Longitude,Genus,Family,Area \
| sed "1s/.*/wals code,name,value,description,latitude,longitude,genus,family,area/" \
| csvformat -T \
| head -n 5
wals code	name	value	description	latitude	longitude	genus	family	area
abi	Abipón	2	Moderately small	-29.0	-61.0	South Guaicuruan	Guaicuruan	Phonology
abk	Abkhaz	5	Large	43.0833333333	41.0	Northwest Caucasian	Northwest Caucasian	Phonology
ach	Aché	1	Small	-25.25	-55.1666666667	Tupi-Guaraní	Tupian	Phonology
acm	Achumawi	2	Moderately small	41.5	-121.0	Palaihnihan	Hokan	Phonology
```

If we wanted to be fancy, we could even add the citation information, using [jq](https://stedolan.github.io/jq/)
to read the CLDF metadata:
```shell
$ cat wals_1A_cldf/StructureDataset-metadata.json | jq -r '."dc:bibliographicCitation"'
Ian Maddieson. 2013. Consonant Inventories.
In: Dryer, Matthew S. & Haspelmath, Martin (eds.)
The World Atlas of Language Structures Online.
Leipzig: Max Planck Institute for Evolutionary Anthropology.
(Available online at http://wals.info/chapter/1 )
```
and adding in the date:
```shell
$ cat wals_1A_cldf/StructureDataset-metadata.json \
| jq -r '."dc:bibliographicCitation"' \
| sed "s/ )/, Accessed on $(date -I).)/g"
Ian Maddieson. 2013. Consonant Inventories.
In: Dryer, Matthew S. & Haspelmath, Martin (eds.)
The World Atlas of Language Structures Online.
Leipzig: Max Planck Institute for Evolutionary Anthropology.
(Available online at http://wals.info/chapter/1, Accessed on 2021-04-22.)
```

Putting it all together:
```shell
$ ( cat wals_1A_cldf/StructureDataset-metadata.json | jq -r '."dc:bibliographicCitation"' | sed "s/ )/, Accessed on $(date -I).)/g" ; echo ""; csvjoin -c Language_ID,ID wals_1A_cldf/values.csv wals_1A_cldf/languages.csv | csvjoin -c Parameter_ID,ID - wals_1A_cldf/parameters.csv | csvcut -C Name2 | csvjoin -c Code_ID,ID - wals_1A_cldf/codes.csv | csvcut -c Language_ID,Name,Value,Name2,Latitude,Longitude,Genus,Family,Area | sed "1s/.*/wals code,name,value,description,latitude,longitude,genus,family,area/" | csvformat -T | head -n 5 ) | cat
```
will yield
```csv
Ian Maddieson. 2013. Consonant Inventories.
In: Dryer, Matthew S. & Haspelmath, Martin (eds.)
The World Atlas of Language Structures Online.
Leipzig: Max Planck Institute for Evolutionary Anthropology.
(Available online at http://wals.info/chapter/1, Accessed on 2021-04-22.)

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
| csvgrep -c Segment_slice -r "." -i \
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

Note that the first invocation of `csvgrep` is used to filter out partial cognates.


## Examples "in the wild"

- A *StructureDataset* with `CodeTable` and `ExampleTable`: [WALS Online v2020.1](https://doi.org/10.5281/zenodo.4683137)
- A *Dictionary* with `ExampleTable`: The [Palula dictionary](https://doi.org/10.5281/zenodo.4675089)
- A *Wordlist* with `CognateTable`: [TuLeD](https://doi.org/10.5281/zenodo.4629306)
- A *Wordlist* published as supplementary material: [Challenges of annotation and analysis (Hill & List 2017)](http://doi.org/10.5281/zenodo.886179)
