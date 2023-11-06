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
`https://cldf.clld.org/v1.0/terms.rdf#segments` where the secondary separator
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
