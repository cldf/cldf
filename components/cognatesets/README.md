# Cognate sets

In historical linguistics cognate judgements have often been postulated as complete set,
not based on justifications for invidual cognates. Thus, the requirement arises to 
encode data related to cognate sets, such as a source or explanation.

The default description of the cognateset table is available in 
[`CognatesetTable-metadata.json`](CognatesetTable-metadata.json).
## [CognatesetTable](http://cldf.clld.org/v1.0/terms.rdf#CognatesetTable): `cognatesets.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | unspecified | <div> <p>A description for an entity.</p> </div> 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | multivalued | <div> <p>List of source specifications, of the form &lt;source_ID&gt;[], e.g. http://glottolog.org/resource/reference/id/318814[34], or meier2015[3-12] where meier2015 is a citation key in the accompanying BibTeX file.</p> </div> 