## Interlinear glossed text

[Interlinear glossed text](http://en.wikipedia.org/wiki/Interlinear_gloss) can be encoded using columns

- `Primary_text`: tab-separated words.
- `Gloss`: tab-separated words.
- `Translation`
- `Translation_language_ID`

where words may be further split into morphemes and clitics using `-` and `=` as separators according to the 
[Leipzig Glossing Rules](http://www.eva.mpg.de/lingua/resources/glossing-rules.php).

Thus, glossed examples can be added to CLDF datasets by adding a file 
`examples.csv` or a table ẁith `"dc:type": "cldf:examples"` where the default
metadata looks like
```python
{
	"url": "examples.csv",
	"tableSchema": {
		"columns": [
			{
				"name": "ID",
				"datatype": "string"
			},
			{
				"name": "Primary_text",
				"datatype": "string",
				"separator": "\t"
			},
			{
				"name": "Gloss",
				"datatype": "string",
				"separator": "\t"
			},
			{
				"name": "Translation",
				"datatype": "string"
			},
			{
				"name": "Translation_language_ID",
				"datatype": "string"
			},
		],
		"primaryKey": "ID"
	}
}
```
