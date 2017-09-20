# CLDF Examples

## A WALS feature as CLDF structure dataset

[Feature 1A of WALS Online](http://wals.info/feature/1A), converted to a CLDF StructureDataset is available at [`wals_1A_cldf`](wals_1A_cldf). This dataset
has been created using the code and instructions at https://github.com/glottobank/pycldf/tree/master/examples

One of the design goals of CLDF was to make re-use of existing tools for linguistic data possible. As an example, we can convert the CLDF
dataset to the legacy custom tab-delimited export of WALS features (e.g.
http://wals.info/feature/1A.tab), using tools from the [`csvkit` package](https://csvkit.readthedocs.io/):
- We use `csvjoin` twice, to augment the `ValueTable` with metadata about languages and parameters.
- The we use `csvcut` to prune the excess columns and re-order the remaining ones.
- Using `sed` we replace the first line, thereby renaming the columns.
- Finally we use `csvformat` to switch to tab-delimited values.

```bash
$ csvjoin -c Language_ID,ID values.csv languages.csv \
| csvjoin -c Parameter_ID,ID - parameters.csv \
| csvcut -c 2,8,4,5,9,10,13,14,19 \
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

```bash
$ csvjoin -c Word_ID,ID cognates.csv forms.csv \
| csvsort -c Concept,Cognate_set_ID,Language - \
| csvcut -c Concept,Cognate_set_ID,Alignment,Language - \
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
