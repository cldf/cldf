# Parameter network

Parameters, i.e. the objects described in a CLDF `ParameterTable`, and relations between them
are often objects of cross-linguistic analysis themselves:
- [Implicational universals](https://www.oxfordreference.com/display/10.1093/oi/authority.20110803095959399) 
  can be formulated as dependency graph of grammatical features - the typical parameters of a CLDF `StructureDataset`.
- [CLICS](https://clics.clld.org/) - the Database of Cross-Linguistic Colexifications - computes a network of colexified 
  concepts - the typical parameters of a CLDF `Wordlist`.

Similar to language trees, networks or graphs are hard to inspect without special software. While trees
(or at least their topology) are almost universally serialized using the Newick format, such a clear standard
format is not available for networks. Thus, to make this kind of data available for analysis and reuse in a
standardized way, networks of parameters in a CLDF dataset can be stored in a `ParameterNetwork` table as 
list of edges.

If a `mediaReference` is used to link to networks or graphs serialized in one of the many file formats
for this, a format that allows discovery of this intent should be prefered. E.g. 
[GraphML](http://graphml.graphdrawing.org/) - being namespaced XML - can easily be detected from a 
`mediaType` of `text/xml`, and the namespace declaration in the XML, while GraphViz' DOT files do not 
have such a transparent discovery mechanism (see https://forum.graphviz.org/t/mime-type-for-downloading-dot-files/877).

A `parameterEdgeReference` property can be used to link rows in CLDF tables to particular edges in
a `ParameterNetwork`. E.g. a custom table listing individual colexifications, i.e. pairs of word counterparts
for different meanings in a `Wordlist`, could link each colexification to the edge in the concept network
that is corroborated by the colexfication.

## [ParameterNetwork](http://cldf.clld.org/v1.0/terms.rdf#ParameterNetwork): `parameter_network.csv`

Rows in this table describe edges in a network of parameters.

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | unspecified | <div> <p>A description for an entity.</p> </div> 
[Target_Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#targetParameterReference) | `string` | unspecified | References the target node of the edge.<br>References Parameter
[Source_Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#sourceParameterReference) | `string` | unspecified | References the source node of the edge.<br>References Parameter
[Edge_Is_Directed](http://cldf.clld.org/v1.0/terms.rdf#edgeIsDirected) | `boolean` | unspecified | Flag signaling whether the edge is directed or undirected.