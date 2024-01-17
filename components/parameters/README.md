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
property in the `ValueTable`.


## Typed parameter values

Often, values for parameters are just text, e.g. word forms in the case of a CLDF [`Wordlist`](../../modules/Wordlist).
In this case, the text string representing the value in the CSV table can simply be interpreted "as is"
by CLDF consumers.


### Categorical or ordinal parameters

If a parameter represents a [categorical (or ordinal) variable](https://en.wikipedia.org/wiki/Categorical_variable),
It is recommended to provide the list of possible values in a [CodeTable](../codes) (possibly extended with a column
indicating the ordering of these values in the case of ordinal variables).
The [ValueTable](../values) should then include a [`codeReference`](http://cldf.clld.org/v1.0/terms.rdf#codeReference)
column, but **also** list the string value in the [`value`](http://cldf.clld.org/v1.0/terms.rdf#value) column. 
While this introduces some redundancy, it ensures compatibility with somewhat simplistic data access methods which may be
employed e.g. for data visualization.


### Numeric parameter values (or values of other types)

Sometimes typological surveys use [data binning](https://en.wikipedia.org/wiki/Data_binning) to transform values of
varying data types (often numeric) into categorical data. Ideally, though, this step should be left to data analysis,
unless the "bins" have some theoretical foundation. To make it possible to store string representations of typed data
in CSV while still specifying how this data should be interpreted, a
[`columnSpec`](http://cldf.clld.org/v1.0/terms.rdf#columnSpec) column can be added to the `ParameterTable`. CLDF
consumers SHOULD then consult the value of this column when reading values associated with the parameter.

As an example, we use the Python package [csvw](https://pypi.org/project/csvw) to obtain a reader for typed data as
specified by a [`columnSpec`](http://cldf.clld.org/v1.0/terms.rdf#columnSpec) value:
```python
>>> import json
>>> from csvw import Column
>>> # Read the datatype description from a string value of the columnSpec column:
>>> reader = Column.fromvalue(json.loads('{"datatype": {"base": "decimal", "minimum": "1", "maximum": "11"}}'))
>>> # Use this reader to interpret string values from the value column as appropriate Python objects:
>>> reader.read('3.4')
Decimal('3.4')
>>> reader.read('30')
...
ValueError: value must be <= 11
```

> [!TIP]
> This mechanism even allows list-valued parameter values. If for example a parameter's value for `columnSpec`
> is the string `{"datatype": "integer", "separator": " "}` values for the parameter can be read as follows:

```python
reader = Column.fromvalue(json.loads('{"datatype": "integer", "separator": " "}'))
reader.read('1 2 3')
[1, 2, 3]
```

See also the related discussion at https://github.com/cldf/cldf/issues/109


## Example

The `ExampleTable` of a `Wordlist` from the [Intercontinental Dictionary Series](https://ids.clld.org)
is described here: https://github.com/intercontinental-dictionary-series/lindseyende/blob/v2.0/cldf/cldf-metadata.json#L269-L300

Since the parameters in this `Wordlist` are the lexical concepts listed in the [IDS concept list](https://concepticon.clld.org/contributions/Key-2016-1310),
the corresponding [Concepticon concept sets](https://concepticon.clld.org/parameters) are specified
using the `concepticonReference` property.

## [ParameterTable](http://cldf.clld.org/v1.0/terms.rdf#ParameterTable): `parameters.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | unspecified | <div> <p>A title, name or label for an entity.</p> </div> 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | unspecified | <div> <p>A description for an entity.</p> </div> 
[ColumnSpec](http://cldf.clld.org/v1.0/terms.rdf#columnSpec) | `json` | singlevalued | <div> <p>A column specification given as JSON representation of a <a href="https://www.w3.org/TR/tabular-metadata/#columns">CSVW column description</a>. This column specification may be used by CLDF consumers to read a parameter's value as typed data.</p> <p>Note that a CSVW datatye description is not sufficient, because parsing a string value must also be informed by the column properties <code>null</code> and <code>separator</code>.</p> </div> 