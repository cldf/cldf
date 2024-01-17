# Senses

When dictionaries or lexicons are encoded using CLDF's [`Dictionary`](../../modules/Dictionary) module,
each entry may be related to multiple senses (lemon's [LexicalSense](http://lemon-model.net/lemon#LexicalSense)) stored as rows in the `SenseTable`.


## Example

The `SenseTable` of the [Diidxazá Lexico-Botanical Dictionary](https://dictionaria.clld.org/contributions/diidxaza)
is described here: https://github.com/dictionaria/diidxaza/blob/v1.2/cldf/cldf-metadata.json#L110-L187

> [!NOTE]
> Since the senses in this dictionary often reflect botanical species, a [`gbifReference`](https://cldf.clld.org/v1.0/terms.html#gbifReference)
> property could be added. Thus, the sense [Arnica](https://dictionaria.clld.org/units/diidxaza-E0110) could be
> assigned a `gbifReference` value of `5396557`, linking it to https://www.gbif.org/species/5396557

## [SenseTable](http://cldf.clld.org/v1.0/terms.rdf#SenseTable): `senses.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | unspecified | <div> <p>A description for an entity.</p> </div> 
[Entry_ID](http://cldf.clld.org/v1.0/terms.rdf#entryReference) | `string` | unspecified | <div> <p> An identifier referencing a dictionary entry by providing a foreign key to <code>EntryTable</code>. </p> </div> <br>References <code>EntryTable</code>