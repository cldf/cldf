# CLDF Examples

## A WALS feature as CLDF structure dataset

[Feature 1A of WALS Online](http://wals.info/feature/1A), converted to a CLDF StructureDataset is available at [`wals_1A_cldf`](wals_1A_cldf). This dataset
has been created using the code and instructions at https://github.com/glottobank/pycldf/tree/master/examples

One of the design goals of CLDF was to make re-use of existing tools for linguistic data possible. As an example, we can convert the CLDF
dataset to the legacy custom tab-delimited export of WALS features (e.g.
http://wals.info/feature/1A.tab), using tools from the [`csvkit` package](https://csvkit.readthedocs.io/):
- We use `csvjoin` twice, to augment the `ValueTable` with metadata about languages and parameters.
- The we use `csvcut` to prune the excess columns and re-order the remaining ones.
- Finally we use `csvformat` to switch to tab-delimited values.

```bash
$ csvjoin -c Language_ID,ID values.csv languages.csv | csvjoin -c Parameter_ID,ID - parameters.csv | csvcut -c 2,8,4,5,9,10,13,14,19 | csvformat -T | head -n 5
Language_ID	Name	Value	Comment	Latitude	Longitude	Genus	Family	Area
xoo	!Xóõ	5	Large	-24.0	21.5	Tu	Tu	Phonology
ood	O'odham	3	Average	32.0	-112.0	Tepiman	Uto-Aztecan	Phonology
aiz	Aizi	3	Average	5.25	-4.5	Kru	Niger-Congo	Phonology
akw	Akawaio	1	Small	6.0	-59.5	Cariban	Cariban	Phonology
```

Renaming the columns is left as exercise for the reader :)


## Examples "in the wild"

- http://doi.org/10.5281/zenodo.886179
