A WALS Chapter as CLDF dataset
==============================

- [core data file](wals-chapter-1.csv)
- [metadata file](wals-chapter-1.csv-metadata.json)
- [bibliography](wals-chapter-1.bib)

Thes files have been created using `pycldf` from within a script operating within the WALS clld app:

- [cldf export script](cldf.py)


Notes
-----

- The metadata file explicitely declares the [csv dialect](https://github.com/glottobank/cldf/blob/master/examples/wals/wals-chapter-1.csv-metadata.json#L18-L22) and the [CLDF version](https://github.com/glottobank/cldf/blob/master/examples/wals/wals-chapter-1.csv-metadata.json#L10).
- [Information about publisher, license, etc. is specified](https://github.com/glottobank/cldf/blob/master/examples/wals/wals-chapter-1.csv-metadata.json#L8-L17) using the [Dublin Core](http://dublincore.org/documents/2012/06/14/dcmi-terms/?v=terms) and [DCAT](https://www.w3.org/TR/vocab-dcat/) vocabularies.
- While the core data file does only list local identifiers for datapoints, languages and features, the [metadata specifies how to expand these to full URLs](https://github.com/glottobank/cldf/blob/master/examples/wals/wals-chapter-1.csv-metadata.json#L38).
- Additional data about the possible values for the WALS feature are given in an [additional csv file](wals-chapter-1-domain.csv), linked using the [foreignKeys property](https://github.com/glottobank/cldf/blob/master/examples/wals/wals-chapter-1.csv-metadata.json#L67-L100).
- [Putting together the `Source` values](https://github.com/glottobank/cldf/blob/master/examples/wals/cldf.py#L20-L23) in the script highlights the price to pay for a format that specifies intra-cell markup: Creators of data must take care to adhere to the spec, without much help by tools.
- A [`Contribution`](https://github.com/glottobank/cldf/blob/master/examples/wals/cldf.py#L89) - in [`clld` terms](https://github.com/clld/clld/blob/master/clld/db/models/contribution.py#L28) - is the most appropriate unit in a `clld` database to be packaged as separate CLDF dataset, because it aggregates all datapoints sharing the same provenance information.


Open Questions
--------------

- Should we include (more) information about the domain (i.e. available values) for a WALS feature? If so, how? [W3 recommends a separate csv file and `foreign keys`](https://github.com/w3c/csvw/issues/212#issuecomment-74439980). But this may be a bit clunky? How would applications want to use this data? Maybe a flag `binary` would be sufficient to mark features with only two values?
