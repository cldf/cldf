# CLDF Dataset discovery

This extension of the CLDF specification makes recommendations about how to specify (locations of) CLDF datasets
in an unambiguous way that is **both, human- and machine-readable**.

While datasets in the local filesystem can be specified as path of the metadata file (or the single table of the 
dataset in case of metadata-free datasets), this is more difficult for locations on the web, e.g. a zipped GitHub 
repository release, or a dataset archived on Zenodo. In these cases,
- an HTTP URL will typically lead to a "bunch of files" (e.g. https://doi.org/10.5281/zenodo.7322688 will lead to
  the landing page for the corresponding deposit on Zenodo, where the user - or software that knows its way
  around Zenodo like [cldfzenodo](https://github.com/cldf/cldfzenodo/blob/d533be125559d10dfc53de60dc3b8eb5fe0caebe/src/cldfzenodo/record.py#L175-L183) -
  will locate a zip-file containing a snapshot of a GitHub repository)
- and some additional knowledge is needed to locate the CLDF data in the extracted content.

This two-step process can be described with a URL of the form `URL#key=value`, i.e. a URL including a [fragment identifier](https://en.wikipedia.org/wiki/URI_fragment)
of the form `key=value`, where `key` and `value` match a (key, value) pair in the dataset's [common properties](https://www.w3.org/TR/tabular-metadata/#common-properties).


## Example

The dataset specification `https://doi.org/10.5281/zenodo.7322688#rdf:ID=wacl` can be resolved as follows:
- Navigate to https://doi.org/10.5281/zenodo.7322688 (following redirects).
- Download https://zenodo.org/record/7322688/files/cldf-datasets/wacl-v1.0.0.zip?download=1
- Unzip the downloaded file.
- Search the contents for a JSON file containing an object with property
  ```json
  {
    ...  
    "rdf:ID": "wacl",
    ...
  }
  ```
