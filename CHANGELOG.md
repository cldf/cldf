
# Changes

All notable changes to the CLDF specification will be documented in this file.
The CLDF specification adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).


## [1.3] - 2024-01-21

### Added

- New component `ParameterNetwork` and associated properties.
- New module `TextCorpus` and associated properties.
- New property `treeReference` to relate data to objects in `TreeTable`
- New language property `parentLanguageGlottocode`
- New language property `speakerArea`


## [v1.2] - 2022-11-22

### Added

New component `TreeTable` and associated properties.

New properties
- parameter property `columnSpec`
- media property `pathInZip`

Added three CLDF extension specifications.


## [v1.1.3] - 2022-07-06

Fixed valueUrl property for Glottocode column, making sure the default name is used as variable.

## [v1.1.2] - 2021-05-25

Losened overly strict cardinality specification for `parameterReference` in `FormTable`.

## [v1.1.1] - 2021-04-30

Fixed regular expression pattern for `cltsReference` property, to include the "unknown"
sound.

## [v1.1] - 2021-04-28

### Added

New components
- `MediaTable`
- `ContributionTable`

with corresponding reference properties
- `mediaReference`
- `contributionReference`

and new properties
- `mediaType`
- `downloadUrl`
- `contributor`
- `citation`

Two new properties to reference catalogs:
- `gbifReference`
- `cltsReference`


### Backward Incompatibilities

Expected cardinalities for some properties have been put in concrete terms in the
Ontology and the component metadata. While this should be regarded largely as a bug fix,
i.e. spelling out assumptions that were already implicit in the specification, this may
lead to incompatibilities for datasets violating these assumptions.


## [v1.0] - 2017-12-18

### Added

New module
- `ParallelText`

New components
- `CognateTable`


## [v1.0rc1] - 2017-07-27

First release in the 1.0 series.
