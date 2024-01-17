# Codes

Often cross-linguistic data contains data for 
[categorical variables](https://en.wikipedia.org/wiki/Categorical_variable) that categorise the 
variable into a set of distinct states. For example [WALS feature 27A](http://wals.info/feature/27A) 
partitions languages according to their strategy for reduplication into
- A. Productive full and partial reduplication
- B. Full reduplication only
- C. No productive reduplication

Specifying the range of possible category states (e.g. "A", "B", and "C" in the example above) 
for a given parameter is useful for error checking. Or if a subset of the data do not exhibit 
all possibilities, then this provides a way to document the full range of possibilities.

This specification can be done by adding a codes table with the default description
[`CodeTable-metadata.json`](CodeTable-metadata.json).

In a [`StructureDataset`'s](../../modules/StructureDataset) [`ValueTable`](../values) the codes can be referenced using a foreign
key with `propertyUrl` `http://cldf.clld.org/v1.0/terms.rdf#codeReference`.


## Example

WALS' [`CodeTable`](https://github.com/cldf-datasets/wals/blob/v2020.2/cldf/codes.csv) is described
here https://github.com/cldf-datasets/wals/blob/v2020.2/cldf/StructureDataset-metadata.json#L214-L275

It contains a custom (i.e. non-CLDF) column `icon` which is used to relay information on how to display a certain
code to the WALS web application.
