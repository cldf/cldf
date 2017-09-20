## Partial cognates

Like cognates, partial cognates refer to a form in a wordlist. But to make it
possible to annotate parts of a form, a segmentation of the form **must** be available,
i.e. the `FormTable` must contain a column with `propertyUrl` `http://cldf.clld.org/v1.0/terms.rdf#soundSequence`.

Then, the scope of a partial cognate judgement can be annotated using 
[slice notation](https://stackoverflow.com/a/24713353), e.g. `0:3` to
indicate the first three segments of a form are assigned to a cognate set.
