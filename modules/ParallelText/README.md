# Parallel Text Dataset

A parallel text typically consist of a set of meanings that are translated into different languages.

- The meanings are documented as [`Parameters`](../../components/parameters), or as links to other identifiers.
- The linguistic expressions of the meanings are collected in a [`FormTable`](../../components/forms).
- The functional equivalent parts between the linguistic expressions are encoded in a [`FunctionalEquivalentTable`](../../components/functionalequivalents), 
- possibly using an [`FunctionalEquivalentsetTable`](../../components/functionalequivalentsets) to specifiy more information about the functional equivalents.

The minimal specification of a Parallel Text Dataset consist of a `FormTable`.

As an example, take the following extract from the Parallel Bible Corpus:

## forms.csv

| ID | Language\_ID | Parameter_ID | Segments |
| --- | --- | --- | --- |
| aai_40001001 | aai | 40001001 | Iti i Jesu ana’a’agir wabih , aiwob ana efane i David ana rara’ane tufuw naatu omatanenane i Abraham ana rara’ane tufuw . Naatu iti i hai gin anayimih . |
| aai_40001002 | aai | 40001002 | Abraham natun i Isaac , naatu Isaac natun i Jacob , Jacob natun i Judah , Judah i taitin tuwahinah bairi hitufuw . |
| aai_40001003 | aai | 40001003 | Naatu Judah natunatun i Perez tain Zerah hairi hitufuw , hinah wabin Tamar . Naatu Perez natun i Hezron , Hezron natun i Ram , |
| aak_40001001 | aak | 40001001 | Xwɨyí̵á rɨpɨ í̵wiárí̵awé Jisasɨ Kiraisoyá nánɨrɨnɨ . Oyá í̵wiárí̵awé nimóga nurɨ áwɨnɨ e mɨxí̵ ináyí̵ Depitorɨnɨ . Depitoyá í̵wiárí̵awé nimóga nurɨ wigí̵ xiáwo írɨŋo Ebɨrí̵amorɨnɨ . |
| aak_40001002 | aak | 40001002 | Ebɨrí̵amo Aisakomɨ emeaŋɨnigɨnɨ . E dánɨ Aisako Jekopomɨ emeaŋɨnigɨnɨ . E dánɨ Jekopo Judaomɨ tí̵nɨ xegí̵ xexɨrí̵meáowamɨ tí̵nɨ emeaŋɨnigɨnɨ . |
| aak_40001003 | aak | 40001003 | E dánɨ Judáo xií̵áí Temaí tí̵nɨ í̵wí̵ ninɨri Pereso tí̵nɨ Serao tí̵nɨ emeaŋɨnigɨnɨ . E dánɨ Pereso Xesɨronomɨ emeaŋɨnigɨnɨ . E dánɨ Xesɨrono Ramomɨ emeaŋɨnigɨnɨ . |
| aau_40001001 | aau | 40001001 | Mamey okukwe Jisas Krais so nopwey-om me ma mey hok non . Jisas Krais hiykwe Devit so ney-nona . Devit hiykwe Abraham so ney-nona . |
| aau_40001002 | aau | 40001002 | Abraham hiykwe Aisak so orih . Aisak hiykwe Jekop so orih . Jekop hiykwe Juda o , hyo nay-ih-nayh o , hmo orih-nawp . |
| aau_40001003 | aau | 40001003 | Juda hiykwe Peres , Sera leys so orih . Hoho pouh kokwe Tamar . Peres hiykwe Hesron so orih . Hesron hiykwe Ram so orih . |

## parameters.csv

| ID | Name | Description |
| --- | --- | --- |
| 40001001 | Matthew 1:1 | The book of the lineage of Jesus Christ, the son of David, the son of Abraham. |
| 40001002 | Matthew 1:2 | Abraham conceived Isaac. And Isaac conceived Jacob. And Jacob conceived Judah and his brothers. |
| 40001003 | Matthew 1:3 | And Judah conceived Perez and Zerah by Tamar. And Perez conceived Hezron. And Hezron conceived Ram. |

## functionalEquivalents.csv

| ID | Form_ID | Segment_Slice | FunctionalEquivalentset_ID |
| --- | --- | --- | --- |
| fe_1 | aai_40001001 | 3 | fes_678 |
| fe_2 | aak_40001001 | 4:5 | fes_678 |
| fe_3 | aau_40001001 | 3:4 | fes_678 |
| fe_4 | aai_40001002 | 2:3 | fes_5263 |
| fe_5 | aak_40001002 | 3 | fes_5263 |
| fe_6 | aau_40001002 | 2 4:5 | fes_5263 |

## functionalEquivalentsets.csv

| ID | Description |
| --- | --- |
| fes_678 | Jesus Christ |
| fes_5263 | conceived |
