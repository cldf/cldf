# Cognate sets

In Historical Linguistics cognate sets are often annotated with additional information, e.g.
a justification for a reconstruction (see for example https://iecor.clld.org/cognatesets/5007).
Similarly, [etyma](https://de.wikipedia.org/wiki/Etymon)
in etymological (or comparative) dictionaries can be modeled as sets of "cognate" words with additional
annotations, e.g. a link to a form in `FormTable`. Thus, the need arises to encode data related to 
cognate sets, such as a source or explanation or the link to a root form.

The default description of the cognateset table is available in 
[*CognatesetTable-metadata.json*](CognatesetTable-metadata.json).


## Example

[IE-CoR](https://iecor.clld.org/)'s `CognatesetTable` is described here: https://github.com/lexibank/iecor/blob/v1.0/cldf/cldf-metadata.json#L463-L552

[ACD' etyma](https://acd.clld.org/cognatesets) are described here:
https://github.com/lexibank/acd/blob/main/cldf/cldf-metadata.json#L443-L505
The `description` property is used for the reconstructed gloss of a proto-form,
and a custom (i.e. non-CLDF) column `Proto_Language` is used for the name of the associated proto-language.

## [CognatesetTable](http://cldf.clld.org/v1.0/terms.rdf#CognatesetTable): `cognatesets.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | unspecified | <div> <p>A description for an entity.</p> </div> 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | multivalued | <div> <p>List of source specifications, of the form &lt;source_ID&gt;[], e.g. http://glottolog.org/resource/reference/id/318814[34], or meier2015[3-12] where meier2015 is a citation key in the accompanying BibTeX file.</p> </div> 