## Structure Dataset

Structure datasets are lists of values measured/coded/determined for a language and a (often typological) feature.
Typical examples are WALS datasets, e.g. the [list of coded values for the language Abau](http://wals.info/languoid/lect/wals_code_aba).

Structure datasets require only one data file `values.csv` or a table with
`"dc:type": "cldf:values"`. This table must contain columns
- `ID`
- `Language_ID`
- `Parameter_ID`: An identifier of a feature (a.k.a. parameter) the `Value` is associated with.
- `Value`


### Multi-dimensional features

Multi-dimensional features are useful to model data like paradigms. 
To support multi-dimensional features, we specify a standard separator for 
`Parameter_ID` components: `~`. 
I.e. a local feature ID for a multi-dimensional feature can be coded as
```
Language_ID Feature_ID Value
deu         Sg~1P     ich
deu         Pl~1P     wir
