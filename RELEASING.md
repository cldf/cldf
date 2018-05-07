Releasing a new version of the CLDF spec
========================================

- Update CHANGELOG.md
- Update all ontology URIs to the new version number
- Recreate default descriptions of components and modules via `scripts/make_defaults.py`
- Run the tests `scripts/test.py`
- Create a release of https://github.com/glottobank/cldf
- Make sure the release is picked up by ZENODO
- Copy the DOI from ZENODO and add it to the release notes
- Copy terms.rdf to a new version directory in the gh-pages branch
- Push the gh-pages branch
