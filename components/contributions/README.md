# Contributions

Often, CLDF datasets are aggregations of data similar to [edited volumes](https://en.wikipedia.org/wiki/Edited_volume).
In this case, individual "chapters" should be citeable; thus, the CLDF dataset should provide
sufficient information to determine these citeable units and construct proper citations.

This information should be supplied in the ContributionTable, making use of suitable
properties of the [DCMI Metadata Terms vocabulary](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/).


## Example

https://github.com/lexibank/wold/blob/master/cldf/vocabularies.csv


## Linking to contributions

Which objects in a CLDF dataset are linked to contributions can vary. Whereas in WALS Online
chapters (i.e. sets of features or parameters) are regarded as citeable units, contributions
to the World Loanword Database are aligned with languages. Thus, for WALS Online one
would add a column with `propertyURL` http://cldf.clld.org/v1.0/terms.rdf#contributionReference
to the ParameterTable, for WOLD it would be added to the LanguageTable.
## [ContributionTable](http://cldf.clld.org/v1.0/terms.rdf#ContributionTable): `contributions.csv`

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | 
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Contributors](http://purl.org/dc/terms/creator) | `string` | 
[Citation](http://purl.org/dc/terms/bibliographicCitation) | `string` | 