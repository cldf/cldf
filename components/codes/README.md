## Codes

Often cross-linguistic data contains data for 
[categorical variables](https://en.wikipedia.org/wiki/Categorical_variable) that categorise the 
variable into a set of distinct states. For example [WALS feature 27A](http://wals.info/feature/27A) 
categorizes languages according to their strategy for reduplication into
- A. Productive full and partial reduplication
- B. Full reduplication only
- C. No productive reduplication

Specifying the range of possible category states (e.g. "A", "B", and "C" in the example above) 
for a given parameter is useful for error checking. Or if a subset of the data do not exhibit 
all possibilities, then this provides a way to document the full range of possibilities.

This specification can be done by adding a codes table with the default description
[`CodeTable-metadata.json`](CodeTable-metadata.json).

In a structure dataset's `ValueTable` the codes can be referenced using a foreign
key `Code_ID`.
