A WALS Chapter as CLDF dataset
==============================

- [core data file](wals-chapter-1.csv)
- [metadata file](wals-chapter-1.csv-metadata.json)
- [bibliography](wals-chapter-1.bib)

Thes files have been created using `pycldf` from within a script operating within the WALS clld app:

- [cldf export script](cldf.py)


Notes
-----

- The data file explicitely declares the [csv dialect](https://github.com/glottobank/cldf/blob/master/examples/wals/wals-chapter-1.csv-metadata.json#L2-L6).
- [Information about publisher, license, etc. is specified](https://github.com/glottobank/cldf/blob/master/examples/wals/wals-chapter-1.csv-metadata.json#L7-L16) using the [Dublin Core](http://dublincore.org/documents/2012/06/14/dcmi-terms/?v=terms) and [DCAT](https://www.w3.org/TR/vocab-dcat/) vocabularies.
- While the core data file does only list local identifiers for datapoints, languages and features, the [metadata specifies how to expand these to full URLs](https://github.com/glottobank/cldf/blob/master/examples/wals/wals-chapter-1.csv-metadata.json#L24).
