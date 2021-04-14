Releasing a new version of the CLDF spec
========================================

- Update CHANGELOG.md
- Recreate default descriptions of components and modules via `scripts/make_defaults.py`
- Run the tests `scripts/test.py`
- Create a release of https://github.com/cldf/cldf
- Make sure the release is picked up by ZENODO
- Copy the DOI from ZENODO and add it to the release notes
- Create cldf.github.io/<version>/index.html, with the selected content from `CHANGELOG.md`.
