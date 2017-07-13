
## Frequently asked questions

### All my data is about the same language, do I still have to specify a `Language_ID` for each row?

No, you can use a [virtual column](http://w3c.github.io/csvw/metadata/#use-of-virtual-columns) to supply
the same `Language_ID` for all rows via metadata; append a [column description](http://w3c.github.io/csvw/metadata/#columns) as follows to the `tableSchema.columns` of the relevant table:
```python
    {
        "name": "Language_ID",
        "virtual": true,
        "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#glottocode",
        "valueUrl": "abcd1234"
    }
```
