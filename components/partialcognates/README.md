## Partial cognates

Like cognates, partial cognates refer to a form in a wordlist. But to make it
possible to annotate parts of a form, the segmentation of the form
**must** contain morpheme boundaries,
i.e. the `FormTable` must contain a column with `propertyUrl` 
`http://cldf.clld.org/v1.0/terms.rdf#soundSequence` where the secondary separator
is used to delimit morphemes, e.g.
```
{
    "name": "Segments",
    "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#soundSequence",
    "separator": "+"
}
```
Then, the scope of a partial cognate judgement can be annotated using 
[slice notation](https://stackoverflow.com/a/24713353), e.g. `0:3` to
indicate the first three morphemes of a form are assigned to a cognate set.
