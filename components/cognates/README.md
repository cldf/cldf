# Cognates

A major use case of wordlists in historical linguistics is for identifying and assembling
cognate sets. Assigning forms to cognate sets is itself a (rather large) step
in analyzing the wordlist data, but also serves as intermediate step before
feeding the cognate sets into further analyses e.g. to determine language relatedness.
Thus, being able to exchange data on cognate judgements related to wordlists
is important, and covered by CLDF. 

It is recommended that columns or other metadata describing the method used
for the cognacy judgements and the alignments are added, but as yet no clear standard
for these has evolved.

## Partial Cognates

Like cognates, partial cognates refer to a form in a wordlist. But to make it
possible to annotate parts of a form, the segmentation of the form
**must** contain morpheme boundaries,
i.e. the `FormTable` must contain a column with `propertyUrl`
`http://cldf.clld.org/v1.0/terms.rdf#segments` where the secondary separator
is used to delimit morphemes, e.g.
```json
{
    "name": "Segments",
    "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#segments",
    "separator": "+"
}
```
Then, the scope of a partial cognate judgement can be annotated by
enumerating the relevant morphemes, e.g. `1 2 3` to
indicate the first three morphemes of a form are assigned to a cognate set,
optionally using shortcut notation for ranges like `1:3`.

The default description of the cognate
table is available in [`CognateTable-metadata.json`](CognateTable-metadata.json).

## [CognateTable](http://cldf.clld.org/v1.0/terms.rdf#CognateTable): `cognates.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Form_ID](http://cldf.clld.org/v1.0/terms.rdf#formReference) | `string` | singlevalued | References the form which is judged to belong to a cognate set.<br>References FormTable
[Cognateset_ID](http://cldf.clld.org/v1.0/terms.rdf#cognatesetReference) | `string` | singlevalued | References the cognate set a form is judged to belong to.<br>References CognatesetTable
[Segment_Slice](http://cldf.clld.org/v1.0/terms.rdf#segmentSlice) | list of `string` (separated by ` `) | multivalued | Specifies the slice of morphemes of the form in case of partial cognacy.
[Alignment](http://cldf.clld.org/v1.0/terms.rdf#alignment) | list of `string` (separated by ` `) | multivalued | The segments of the form aligned with respect to all other forms in the cognate set
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | multivalued | <div> <p>List of source specifications, of the form &lt;source_ID&gt;[], e.g. http://glottolog.org/resource/reference/id/318814[34], or meier2015[3-12] where meier2015 is a citation key in the accompanying BibTeX file.</p> </div> 