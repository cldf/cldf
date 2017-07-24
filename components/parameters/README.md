## Parameter Metadata

Obviously, cross-linguistic data often compares languages using comparative concepts,
e.g. typological features like in WALS, or Swadesh terms as in many wordlists.

While it may sometimes be enough to refer to such a concept by ID, e.g.
using a value like `http://wals.info/feature/116A` for the `Parameter_ID` column
in a [Structure Dataset](../../modules/StructureDataset/), often additional metadata
must be provided. This should be done in CLDF datasets by including a
data file `parameters.csv` or a table with `"dc:conformsTo": "http://cldf.clld.org/v1.0/terms.rdf#ParameterTable"`, and pointing to rows in this table
using the `Parameter_ID` column, appropriately described with a [`ForeignKey` definition](http://w3c.github.io/csvw/metadata/#dfn-foreign-key-definition).
