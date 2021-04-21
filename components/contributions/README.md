# Contributions

Often, CLDF datasets are aggregations of data similar to [edited volumes](https://en.wikipedia.org/wiki/Edited_volume).
In this case, individual "chapters" should be citeable; thus, the CLDF dataset should provide
sufficient information to determine these citeable units and construct proper citations.

This information should be supplied in the ContributionTable, making use of suitable
properties of the [DCMI Metadata Terms vocabulary](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/).


## Example

See
https://github.com/lexibank/wold/blob/master/cldf/vocabularies.csv


## Linking to contributions

The specific objects in a CLDF dataset that link to contributions can vary according to the needs
of the dataset. For example, the [WALS Online](https://wals.info/) database is comprised of chapters
which contain sets of features or parameters. Each chapter is regarded as a citeable unit, e.g.

> It is important to cite the specific chapter that you are taking your information from, not just the
general work "The World Atlas of Language Structures Online" (Dryer, Matthew S. & Haspelmath, Martin
2013), unless you are citing data from more than 25 chapters simultaneously.

...therefore, in the CLDF dataset each chapter is linked to a specific contribution.

In contrast, the [World Loanword Database](https://wold.clld.org/) contains vocabularies
contributed by an expert on each language and its history. In this case, therefore,
the contributions are linked to each language.

Thus, for WALS Online one would add a column with `propertyURL` `http://cldf.clld.org/v1.0/terms.rdf#contributionReference`
to the ParameterTable, for WOLD it would be added to the LanguageTable.

## [ContributionTable](http://cldf.clld.org/v1.0/terms.rdf#ContributionTable): `contributions.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | unspecified | <div> <p>A title, name or label for an entity.</p> </div> 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | unspecified | <div> <p>A description for an entity.</p> </div> 
[Contributor](http://cldf.clld.org/v1.0/terms.rdf#contributor) | `string` | unspecified | <div> <p>Contributor(s) to a citeable unit of a dataset.</p> </div> 
[Citation](http://cldf.clld.org/v1.0/terms.rdf#citation) | `string` | unspecified | <div> <p>A full citation for a citeable unit of a dataset, preferably following the rules of the <a href="https://www.linguisticsociety.org/resource/unified-style-sheet">Unified Style Sheet for Linguistics Journals</a> or the best practices for <a href="https://site.uit.no/linguisticsdatacitation/">Linguistics Data Citation</a>. </p> </div> 