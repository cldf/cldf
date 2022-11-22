Releasing a new version of the CLDF spec
========================================

- Update 
  - `CHANGELOG.md`
  - version info in `terms.rdf`
- Run the tests
  ```shell
  cldfspec test
  ```  
- Create the component READMEs
  ```shell
  cldfspec component_readmes
  ```
- Create the module defaults
  ```shell
  cldfspec make_module_defaults
  ```
- Commit and tag the repos
  ```shell
  git commit -a -m"v<version>"
  git tag -a v<version> -m"v<version>"
  git push origin --tags
  ```
- Create a release of https://github.com/cldf/cldf
- Make sure the release is picked up by ZENODO
- Copy the DOI from ZENODO and add it to the release notes
- Create cldf.github.io/<version>/index.html, with the selected content from `CHANGELOG.md`:
  ```shell
  cldfspec update_site
  cd ../cldf.github.io
  git add ...
  ```
- Adapt landing page, then  
  ```shell
  git commit -a -m"release v..."
  git push origin
  ```
- Update `pycldf`:
  ```shell
  cd ../cldf
  cldfspec update_pycldf
  cd ../pycldf
  git status
  ```
