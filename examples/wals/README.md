A WALS Chapter as CLDF dataset
==============================

- [core data file](wals-chapter-1.csv)
- [metadata file](wals-chapter-1.csv-metadata.json)
- [bibliography](wals-chapter-1.bib)

Thes files have been created using [`pycldf` version 0.2.1](https://github.com/glottobank/pycldf) from within a script operating within the WALS clld app:

- [cldf export script](cldf.py)


Notes
-----

- The metadata file explicitely declares the [csv dialect](https://github.com/glottobank/cldf/blob/master/examples/wals/wals-chapter-1.csv-metadata.json#L18-L22) and the [CLDF version](https://github.com/glottobank/cldf/blob/master/examples/wals/wals-chapter-1.csv-metadata.json#L10).
- [Information about publisher, license, etc. is specified](https://github.com/glottobank/cldf/blob/master/examples/wals/wals-chapter-1.csv-metadata.json#L8-L17) using the [Dublin Core](http://dublincore.org/documents/2012/06/14/dcmi-terms/?v=terms) and [DCAT](https://www.w3.org/TR/vocab-dcat/) vocabularies.
- While the core data file does only list local identifiers for datapoints, languages and features, the [metadata specifies how to expand these to full URLs](https://github.com/glottobank/cldf/blob/master/examples/wals/wals-chapter-1.csv-metadata.json#L38).
- [Putting together the `Source` values](https://github.com/glottobank/cldf/blob/master/examples/wals/cldf.py#L20-L23) in the script highlights the price to pay for a format that specifies intra-cell markup: Creators of data must take care to adhere to the spec, without much help by tools.
- A [`Contribution`](https://github.com/glottobank/cldf/blob/master/examples/wals/cldf.py#L122) - in [`clld` terms](https://github.com/clld/clld/blob/master/clld/db/models/contribution.py#L28) - is the most appropriate unit in a `clld` database to be packaged as separate CLDF dataset, because it aggregates all datapoints sharing the same provenance information.
- Additional data about the possible values for the WALS feature are given in an [additional csv file](wals-chapter-1-domain.csv), linked using the [foreignKeys property](https://github.com/glottobank/cldf/blob/master/examples/wals/wals-chapter-1.csv-metadata.json#L67-L100). This [foreign key](https://www.w3.org/TR/tabular-metadata/#foreign-key-reference-between-tables) description can be used to augment the core data file by joining the additional data, e.g. using [csvkit's `csvjoin` command](https://csvkit.readthedocs.io/en/0.9.1/scripts/csvjoin.html) as follows:
```
$ csvjoin -c DomainElement,ID wals-chapter-1.csv wals-chapter-1-domain.csv | csvstat
  1. ID
	<type 'unicode'>
	Nulls: False
	Unique values: 563
	Max length: 6
  2. Language_ID
	<type 'unicode'>
	Nulls: False
	Unique values: 561
	5 most frequent values:
		sanm1295:	2
		pitj1243:	2
		abkh1244:	1
		nucl1454:	1
		fasu1242:	1
	Max length: 8
  3. Language_name
	<type 'unicode'>
	Nulls: False
	Unique values: 563
	Max length: 32
  4. Parameter_ID
	<type 'datetime.time'>
	Nulls: False
	Values: 01:00:00
  5. Value
	<type 'unicode'>
	Nulls: False
	Values: Large, Small, Average, Moderately large, Moderately small
  6. DomainElement
	<type 'datetime.time'>
	Nulls: False
	Values: 01:00:00
  7. Source
	<type 'unicode'>
	Nulls: True
	Unique values: 557
	5 most frequent values:
		Tucker-and-Bryan-1966:	4
		Mazaudon-1973:	1
		Ferguson-and-Chowdhury-1960;Klaiman-1990:	1
		Henderson-1965:	1
		Burling-1961:	1
	Max length: 107
  8. Comment
	<type 'NoneType'>
	Nulls: True
	Values: 
  9. ID
	<type 'datetime.time'>
	Nulls: False
	Values: 01:00:00
 10. Name
	<type 'unicode'>
	Nulls: False
	Values: Large, Small, Average, Moderately large, Moderately small
 11. Numeric
	<type 'int'>
	Nulls: False
	Values: 1, 2, 3, 4, 5
 12. Description
	<type 'unicode'>
	Nulls: False
	Values: Large, Small, Average, Moderately large, Moderately small

Row count: 563

