# CLDF Dataset discovery

This extension of the CLDF specification makes recommendations about how to specify (locations of) CLDF datasets
in an unambiguous way that is **both, human- and machine-readable**.

While datasets in the local filesystem can be located via the path of the metadata file (or the single table of the 
dataset in case of metadata-free datasets), this is more difficult for locations on the web, e.g. a zipped GitHub 
repository release, or a dataset archived on Zenodo. In these cases,
- an HTTP URL will typically lead to a "bunch of files" (e.g. https://doi.org/10.5281/zenodo.7322688 will lead to
  the landing page for the corresponding deposit on Zenodo, where the user - or software that knows its way
  around Zenodo like [cldfzenodo](https://github.com/cldf/cldfzenodo/blob/d533be125559d10dfc53de60dc3b8eb5fe0caebe/src/cldfzenodo/record.py#L175-L183) -
  will locate a zip-file containing a snapshot of a GitHub repository)
- and some additional knowledge is needed to locate the CLDF data in the extracted content.


## Specification

This two-step process can be described with a URL of the form `URL#key=value`, i.e. a URL including a [fragment identifier](https://en.wikipedia.org/wiki/URI_fragment)
of the form `key=value`, where `key` and `value` match a (key, value) pair in a dataset's [common properties](https://www.w3.org/TR/tabular-metadata/#common-properties).
We call such URLs *dataset locators*.

If the URL part of the locator is resolved to a (download in a) local directory, the dataset MUST be located by
searching through the contained files for a matching CLDF metadata file.

A missing value, i.e. a fragment of the form `#key` matches a dataset, if the dataset's common properties contain
a key `key`.


## Example

The dataset locator `https://doi.org/10.5281/zenodo.7322688#rdf:ID=wacl` can be resolved as follows:
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


## Notes for implementors

Implementations must provide a function or service which accepts a dataset locator
as specified above, and returns
- a local path to the metadata file of the requested dataset
- or a platform-specific object representing the dataset (such as a `pycldf.Dataset` instance for a Python implementation).

Implementations of the Dataset discovery specification may support just a subset of possible URLs, e.g. for
a particular archiving provider. If a URL is not supported, this MUST be signaled with an appropriate error
code.
