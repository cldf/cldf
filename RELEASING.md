Releasing a new version of the CLDF spec
========================================

- Update CHANGELOG.md
- Run the tests `cldfspec test`
- Create the component READMEs `cldfspec component_readmes` 
- Create the module defaults `cldfspec make_module_defaults` 
- Create a release of https://github.com/cldf/cldf
- Make sure the release is picked up by ZENODO
- Copy the DOI from ZENODO and add it to the release notes
- Create cldf.github.io/<version>/index.html, with the selected content from `CHANGELOG.md`:
  ```shell
  $ cldfspec update_site
  $ cd ../cldf.github.io
  $ git add ...
  ```
- Adapt landing page, then  
  ```shell
  $ git commit -a -m"release v..."
  $ git push origin
  ```
- Update `pycldf`:
  ```shell
  $ cldfspec update_pycldf
  $ cd ../pycldf
  $ git status
  ```
