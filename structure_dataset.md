## Structure Dataset

Structure datasets are lists of values measured/coded/determined for a language and a (often typological) feature.
Typical examples are WALS datasets, e.g. the [list of coded values for the language Abau](http://wals.info/languoid/lect/wals_code_aba).


### The data file

In addition to the core column names required in each row of the data file, the following columns are required in structure datasets:

- `Feature_ID`: An identifier of a feature (a.k.a. parameter) the `Value` is associated with.


### Multi-dimensional features

Multi-dimensional features are useful to model data like paradigms. To support multi-dimensional features, we specify a standard separator for feature ID components: `~`. I.e. a local feature ID for a multi-dimensional feature can be coded as
```
Language_ID Feature_ID Value
deu         Sg~1P     ich
deu         Pl~1P     wir
```
