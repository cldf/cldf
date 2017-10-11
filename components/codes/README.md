## Codes

Often cross-linguistic data contains data for 
[categorical variables](https://en.wikipedia.org/wiki/Categorical_variable),
e.g. [WALS feature 27A](http://wals.info/feature/27A) categorizes languages
according to their strategy for reduplication into
- Productive full and partial reduplication
- Full reduplication only
- No productive reduplication

Specifying the full range of valid categories for a given parameter is useful for
error checking, and also if subsets of the data do not exhibit all possibilities.
This can be done by adding a codes table with the default description
[`CodeTable-metadata.json`](CodeTable-metadata.json).

In a structure dataset's `ValueTable` the codes can be refernced using a foreign
key `Code_ID`.