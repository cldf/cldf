# Trees

Describing language families using classification trees has a long history in linguistics.
More recently phylogenetic methods started to be used to compute phylogenies of language families,
providing meaningful branch length in contrast to purely topological classification trees.

With more and more of these trees being available, they have become an object of analysis themselves.
But using such trees in analyses together with other language data requires a mapping of tree taxa to
languages.

CLDF's `TreeTable` provides a way to represent appropriately mapped trees and connect them with descriptions
of the tree taxa in a `LanguageTable`.


## Tree files

Representing tree structures as content in CSV files would not make much sense, in particular if reuse is
to be maximized. Thus, the `TreeTable` only references tree data represented using the [Newick format](https://en.wikipedia.org/wiki/Newick_format)
either in
- *Newick files* (i.e. as lines of newick trees in a text file) or in
- a tree block in a [*Nexus files*](https://plewis.github.io/nexus/).

These files are referenced from `TreeTable` using a [Media_ID](https://cldf.clld.org/v1.0/terms.rdf#mediaReference) column,
and the referenced row in `MediaTable` MUST have [Media_Type](https://cldf.clld.org/v1.0/terms.rdf#mediaType) `text/x-nh` for Newick files.
If the media type is different from `text/x-nh`, the file MUST be a Nexus file.

CLDF consumers SHOULD look for a leading string `#NEXUS` in the content of files identified as Nexus files and MUST
report an error if none is found.


## Matching TreeTable items with newick trees

Both, Newick and Nexus files may contain multiple trees. The correct tree referenced from an item in
`TreeTable` is determined
- for Newick files by interpreting the value of the [Name](https://cldf.clld.org/v1.0/terms.rdf#name) column as
  1-based index into the list of lines in the file
- for Nexus files by matching the value of the [Name](https://cldf.clld.org/v1.0/terms.rdf#name) column against tree
  labels in the file. (In a Nexus tree line looking like `tree one = [&U] (1,2,(3,(4,5));`, `one` is the tree label.)

Note: We do not match trees with items in `TreeTable` based on ID, because CLDF object identifiers may be more
constrained than tree labels in Nexus.


## Matching Newick node labels with items in LanguageTable

Each named node in the Newick representation of a tree MUST be interpreted as foreign key into `LanguageTable`, i.e.
must match the [ID](https://cldf.clld.org/v1.0/terms.rdf#id) property of an item in `LanguageTable`.


## Validation

CLDF validators MAY choose to only implement CSVW validation for the `TreeTable`, but MUST issue a warning if run on
a dataset containing one. If full validation is implemented, a CLDF validator MUST retrieve and read associated tree
files and make sure that
- each item in `TreeTable` has a corresponding Newick representation in the tree file
- the node names in the Newick representation satisfy the constraint described [above](#matching-newick-node-labels-with-items-in-languagetable).

## [TreeTable](https://cldf.clld.org/v1.0/terms.rdf#TreeTable): `trees.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](https://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Name](https://cldf.clld.org/v1.0/terms.rdf#name) | `string` | unspecified | Name of tree as used in the tree file, i.e. the tree label in a Nexus file or the 1-based index of the tree in a newick file
[Description](https://cldf.clld.org/v1.0/terms.rdf#description) | `string` | unspecified | Describe the method that was used to create the tree, etc.
[Tree_Is_Rooted](https://cldf.clld.org/v1.0/terms.rdf#treeIsRooted) | `boolean` | unspecified | Whether the tree is rooted (Yes) or unrooted (No) (or no info is available (null))
[Tree_Type](https://cldf.clld.org/v1.0/terms.rdf#treeType) | `string` | unspecified | Whether the tree is a summary (or consensus) tree, i.e. can be analysed in isolation, or whether it is a sample, resulting from a method that creates multiple trees
[Tree_Branch_Length_Unit](https://cldf.clld.org/v1.0/terms.rdf#treeBranchLengthUnit) | `string` | unspecified | The unit used to measure evolutionary time in phylogenetic trees.
[Media_ID](https://cldf.clld.org/v1.0/terms.rdf#mediaReference) | `string` | unspecified | References a file containing a Newick representation of the tree, labeled with identifiers as described in the LanguageTable (the [Media_Type](https://cldf.clld.org/v1.0/terms.html#mediaType) column of this table should provide enough information to chose the appropriate tool to read the newick)<br>References MediaTable
[Source](https://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | multivalued | <div> <p>List of source specifications, of the form &lt;source_ID&gt;[], e.g. http://glottolog.org/resource/reference/id/318814[34], or meier2015[3-12] where meier2015 is a citation key in the accompanying BibTeX file.</p> </div> 