# Contributions

Often, CLDF datasets are aggregations of data similar to [edited volumes](https://en.wikipedia.org/wiki/Edited_volume).
In this case, individual "chapters" should be citeable; thus, the CLDF dataset should provide
sufficient information to determine these citeable units and construct proper citations.

This information should be supplied in the `ContributionTable`, making use of suitable
properties of the [DCMI Metadata Terms vocabulary](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/).


## Example

See https://github.com/lexibank/wold/blob/v4.0/cldf/contributions.csv


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
