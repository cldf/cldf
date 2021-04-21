# Parameters

Obviously, cross-linguistic data often compares languages using comparative concepts,
e.g. typological features like in WALS, or Swadesh terms as in many wordlists.

While it may sometimes be enough to refer to such a concept by ID, e.g.
using a value like `116A` as 
[`parameterReference`](http://cldf.clld.org/v1.0/terms.rdf#parameterReference)
to refer to [WALS feature 116A](http://wals.info/feature/116A)
in a [Structure Dataset](../../modules/StructureDataset), often additional metadata
must be provided. This should be done in CLDF datasets by including a
`ParameterTable`, i.e. a table with `"dc:conformsTo": "http://cldf.clld.org/v1.0/terms.rdf#ParameterTable"`, and pointing to rows in this table
using the [`parameterReference`](http://cldf.clld.org/v1.0/terms.rdf#parameterReference)
property.


## Example

See https://github.com/intercontinental-dictionary-series/lindseyende/blob/master/cldf/parameters.csv
for an example of a `ParameterTable` in a `Wordlist`.

```csv
ID,Name,Concepticon_ID,Concepticon_Gloss
1-100,world,965,WORLD
1-210,"earth, land",626,LAND
1-212,"earth=ground, soil",1228,EARTH (SOIL)
1-213,dust,2,DUST
1-214,mud,640,MUD
1-215,sand,671,SAND
1-220,"mountain, hill",2118,MOUNTAIN OR HILL
...
```