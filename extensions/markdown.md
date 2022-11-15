# CLDF Markdown

CLDF is designed to maximize re-usability of linguistic data. Often, though, reuse of linguistic data does not
mean feeding it into analysis tools, but using it in descriptions as examples. To pave the path for supporting
this usage scenario, using CLDF Markdown to add references to CLDF data objects to text is recommended.

CLDF Markdown specifies how to insert references to CLDF data in markdown documents in much the same way that
the `\cite` command functions in LaTeX. (And just like a piece of software - `bibtex` - is required to actually
provide replacements for the references when rendering a LaTeX document, CLDF Markdown becomes really useful with
a suitable renderer.)


## Syntax

CLDF Markdown is [regular markdown](https://commonmark.org/) where URLs specified in [markdown links](https://www.markdownguide.org/basic-syntax/#links)
may be interpreted as references to objects in a CLDF dataset.

The link syntax to reference a single object, i.e. a row in a CLDF table looks as follows:
```
[An arbitrary label](some/path/<component-name-or-csv-filename>#cldf:<obect-id>)
```

To reference all rows in a table, use
```
[An arbitrary label](some/path/<component-name-or-csv-filename>#cldf:__all__)
```


### Component name or CSV filename

Only the last component of the URL path is used to determine a CLDF component or table of the dataset, while
the first part is ignored. This allows using URLs that are even somewhat functional in the unrendered
document. E.g.
```
[Meier 2020](cldf/sources.bib#cldf:Meier2020)
```
will render as `Meier 2020`, linking to the BibTeX file when the document is simply rendered as markdown by
a service like GitHub, while the enhanced document created from a CLDF Markdown renderer may replace the link with
the reference data expanded to a full citation according to the Unified Stylesheet for Linguistics.

So whether to use the somewhat more transparent CLDF component names for CLDF Markdown references or
the respective filenames of the "data on disk" is up to the author of a CLDF Markdown document.


### Referencing data from multiple datasets

To reference objects in multiple datasets, the fragment identifier must start with `cldf-dsid:`, where `dsid` is
an identifier that can be mapped to a dataset by the processing application. To avoid ambiguities due to the dataset
identifier being used as part of a URL, it is limited to contain only ASCII alphanumerical characters and `_`.


### Passing additional info to processors

CLDF Markdown processors may accept input to customize rendering of CLDF objects. This additional information can
be passed in the [query string](https://en.wikipedia.org/wiki/Query_string) of the URL. CLDF Markdown processors MUST ignore
unknown parameters (to make CLDF Markdown documents renderable with multiple processors) - but may issue a warning about this
(to give the user feedback about accepted parameters).


### Metadata

CLDF datasets may come with rich metadata, serialized as JSON. To reference (and insert) bits and pieces of this
metadata in CLDF markdown documents, the special component name `Metadata` (or the name of the JSON metadata
file) may be used in the URL. The particular piece of metadata must be selected using [JMESPath](https://jmespath.org/)
syntax.

So in the simplest case this could be `[](Metadata#cldf:"dc:license")`. A more complex example would be
```
[](Metadata#cldf:tables[?"dc:conformsTo"=='http://cldf.clld.org/v1.0/terms.rdf#LanguageTable'].url | [0])
```
to select the filename used for the `LanguageTable` component of the dataset.


## Dataset mappings in YAML frontmatter

In addition to the CLDF Markdown link syntax, a text document may provide a mapping of prefixes to dataset specifications
(see [dataset discovery](discovery.md)) - in analogy to [XML namespaces](https://en.wikipedia.org/wiki/XML_namespace#Namespace_declaration) - as 
`cldf-datasets` key of a [YAML frontmatter](https://jekyllrb.com/docs/front-matter/) block. The value of this key may
be a single string in case a single dataset is referenced, or a [YAML mapping](https://yaml.org/spec/1.2.2/#21-collections) of 
prefixes to dataset specifications.


## References

- [Presentation introducing CLDF markdown](https://pad.gwdg.de/kRxjETnhQqqQ0LESDyTlOg)
