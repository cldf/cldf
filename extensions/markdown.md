# CLDF Markdown

CLDF is designed to maximize re-usability of linguistic data. Often, though, reuse of linguistic data does not
mean feeding it into analysis tools, but using it in descriptions as examples. To pave the path for supporting
this usage scenario, CLDF Markdown specifies how to add references to CLDF data objects in text.

CLDF Markdown is supposed to work in much the same way that [BibTeX](http://www.bibtex.org/) functions for citations
in LaTeX documents. I.e.
- CLDF defines a file format for the data - like the [BibTeX format](http://www.bibtex.org/Format/).
- CLDF Markdown specifies how to reference data objects - like the `\cite` command in LaTeX.
- CLDF Markdown implementations *render* CLDF Markdown documents into target formats.


## Syntax

CLDF Markdown is [regular markdown](https://commonmark.org/) where appropriately formatted URLs specified in 
[markdown links](https://www.markdownguide.org/basic-syntax/#links)
are interpreted as references to objects in a CLDF dataset.

The link syntax to reference a single object, i.e. a row in a CLDF table looks as follows:
```markdown
[An arbitrary label](some/path/<component-name-or-csv-filename>#cldf:<obect-id>)
```
e.g.
```markdown
[Example 1](ExampleTable#cldf:ex1)
```

All rows in a table can be referenced using the special `__all__` identifier.
```
[An arbitrary label](some/path/<component-name-or-csv-filename>#cldf:__all__)
```


### Component name or CSV filename

Only the last component of the URL path is used to determine a CLDF component or table of the dataset, while
the first part is ignored. This allows using URLs that are even somewhat functional in unrendered
document. E.g.
```markdown
[Meier 2020](cldf/sources.bib#cldf:Meier2020)
```
will render as `Meier 2020`, linking to the BibTeX file when the document is simply rendered as markdown by
a service like GitHub (while the enhanced document created from a CLDF Markdown renderer may replace the link with
the reference data expanded to a full citation according to the Unified Stylesheet for Linguistics).

Whether to use the somewhat more transparent CLDF component names for CLDF Markdown references or
the respective filenames of the "data on disk" is up to the author of a CLDF Markdown document.


### Referencing data from multiple datasets

To reference objects in multiple datasets, the fragment identifier MUST start with `cldf-dsid:`, where `dsid` is
an identifier that can be mapped to a dataset by the processing application. To avoid ambiguities due to the dataset
identifier being used as part of a URL, it is limited to contain only ASCII alphanumerical characters and `_`.

The mapping of dataset identifiers to dataset locators (see [dataset discovery](discovery.md)) must be passed into
the processing application, or provided by the CLDF Markdown via [YAML frontmatter](#dataset-mappings-in-yaml-frontmatter).


### Passing additional info to processors

CLDF Markdown processors MAY accept input to customize rendering of CLDF objects. This additional information can
be passed in the [query string](https://en.wikipedia.org/wiki/Query_string) of the URL. CLDF Markdown processors MUST ignore
unknown parameters (to make CLDF Markdown documents renderable with multiple processors) - but MAY issue a warning about this
(to give the user feedback about accepted parameters).


### Metadata

CLDF datasets may come with rich metadata, serialized as JSON. To reference (and insert) bits and pieces of this
metadata in CLDF Markdown documents, the special component name `Metadata` (or the name of the JSON metadata
file) may be used in the URL of a CLDF Markdown link. The particular piece of metadata must be selected using 
[JMESPath](https://jmespath.org/) syntax.

So in the simplest case this could be `[](Metadata#cldf:"dc:license")`. A more complex example would be
```markdown
[](Metadata#cldf:tables[?"dc:conformsTo"=='http://cldf.clld.org/v1.0/terms.rdf#LanguageTable'].url | [0])
```
to select the filename used for the `LanguageTable` component of the dataset.


## Dataset mappings in YAML frontmatter

In addition to the CLDF Markdown link syntax, a text document may provide a mapping of prefixes to dataset specifications
(see [dataset discovery](discovery.md)) - in analogy to [XML namespaces](https://en.wikipedia.org/wiki/XML_namespace#Namespace_declaration) - as 
`cldf-datasets` key of a [YAML frontmatter](https://jekyllrb.com/docs/front-matter/) block. The value of this key may
be a single string in case a single dataset is referenced, or a [YAML mapping](https://yaml.org/spec/1.2.2/#21-collections) of 
prefixes to dataset specifications.

So a CLDF Markdown document referencing data from [WALS](https://wals.info) as well [APiCS](https://apics-online.info)
could declare this in frontmatter as follows:
```yaml
---
cldf-datasets: {
  wals: https://doi.org/10.5281/zenodo.6806407#rdf:ID=wals
  apics: https://doi.org/10.5281/zenodo.3823888#rdf:ID=apics
}
---
```


## References

- [Presentation introducing CLDF markdown](https://pad.gwdg.de/kRxjETnhQqqQ0LESDyTlOg)