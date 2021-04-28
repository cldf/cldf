
# Changes

All notable changes to the CLDF specification will be documented in this file.
The CLDF specification adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]


## [v1.1] -

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
