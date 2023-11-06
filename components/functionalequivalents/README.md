# Functional Equivalents

Given some linguistic strings in different languages, this component allows for the annotation of functional equivalents, i.e. parts between the two strings that have express a similar function. This can be used for all kinds of resources, but the typical use-case will be the annotation of parallel texts. Given a collections of strings (e.g. sentences) that express the same content in different languages, this component can be used to express the insight that a part of one string is functionally equivalent to a part of another string. 

Such a functional alignment is in principle similar to a cognacy alignment (see the component [cognates](../cognates)), but it is very often a many-to-many mapping, and the ordering is often very irregular. This component allows for two different ways to encode such functional equivalents:

- a very general method that can deal with any criss-crossing many-to-many alignment, using explicit stand-off reference
- a simpler method using parallel columns like with sound alignment, which will only be useful for highly similar languages where there is not much crossing of ordering and mostly one-to-one alignment.

## Explicit stand-off reference

In this method, the string ('sentence'), encoded as a link to a [`FormTable`](../forms) in the column `Form_ID`, is assumed to be separated by spaces. Using the column `Segment_Slice` any set of such elements ('words') can be specified by their order-count (i.e. elements "3:5 7", referring to the third to fifth and seventh 'word'). One line in the `FunctionalEquivalentTable` specifies such a group of words, and assigns it to a `FunctionalEquivalentsSet_ID`, i.e. a group of lines in the table that express a similar function. Further information about these sets can be specified in the [`functionalEquivalentsetTable`](../functionalequivalentsets).

Note that this approach cannot deal with subparts of words. If you want to refer to, say, the first two letters of a word, then this part has to be separated separately. This means that first a new [`FormTable`](../forms) has to be made with a new separation (e.g. a morpheme separation). This can of course also be done via the [examples component](../examples).

## Implicit reference ("Alignment")

In some cases the strings ('sentences') to be aligned are so similar that it is possible to make a more simple direct alignment by adding additional spaces into the string, similar to how alignments are encoded in [cognates](../cognates). Such an alignment (i.e. the original string with extra spaces added) can be specified in the column `Alignment`. Now there is no explicit encoding of a `FunctionalEquivalentsSet` because the functional equivalents are encoded by being in the same column of the Alignment.

Note that there will be recurring cases of crossing alignments (i.e. the order of elements is reversed) in such alignments. This is similar to the problem of metathesis in sound alignment, and the same solution is proposed for both situations. If elements 'A B C D' from one language has to be aligned to elements 'A C B D' in another language, an extra 'virtual' column is added, leading to 'A  B C D' and 'A C B  D' To indicate that the columns 2 and 4 are actually the same element, an `AlignmentAnntoationTable` can be used.

## [FunctionalEquivalentTable](https://cldf.clld.org/v1.0/terms.rdf#FunctionalEquivalentTable): `functionalEquivalents.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](https://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Form_ID](https://cldf.clld.org/v1.0/terms.rdf#formReference) | `string` | unspecified | <div> <p> An identifier referencing a form by providing a foreign key into the FormTable. </p> </div> <br>References FormTable
[FunctionalEquivalentset_ID](https://cldf.clld.org/v1.0/terms.rdf#functionalEquivalentsetReference) | `string` | unspecified | <div> <p> A functional equivalent set is a group of strings from different languages that express similar function. This is an identifier referencing a cognateset either <ul> <li>by providing a foreign key into the FunctionalEquivalentsetTable or</li> <li>by using a known encoding scheme.</li> </ul> </p> </div> <br>References FunctionalEquivalentsetTable
[Segment_Slice](https://cldf.clld.org/v1.0/terms.rdf#segmentSlice) | list of `string` (separated by ` `) | multivalued | <div> <p> List of segment indices or segment ranges forming the target of a partial cognacy judgement. </p> </div> 
[Alignment](https://cldf.clld.org/v1.0/terms.rdf#alignment) | list of `string` (separated by ` `) | multivalued | <div> <p>An alignment represents <a href="http://linguistics-ontology.org/gold/2010/Segment">segments</a> which are grouped into a common <a href="#cognatesetReference">cognate set</a> as a matrix in which cognate segments are placed in the same column while gap characters are introduced in those sound sequences missing a certain counterpart.</p> </div> 
[Source](https://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | multivalued | <div> <p>List of source specifications, of the form &lt;source_ID&gt;[], e.g. http://glottolog.org/resource/reference/id/318814[34], or meier2015[3-12] where meier2015 is a citation key in the accompanying BibTeX file.</p> </div> 