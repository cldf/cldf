# Borrowings

Lexical borrowings or loanwords provide an interesting object of study by themselves
(see for example [The World Loanword Database](http://wold.clld.org/)), but they
are of great importance for historical linguistics and computational approaches 
where it is important to distinguish between cognates due to borrowing and cognates due to inheritance.

Conceptually, borrowings are the 
[associative entity](https://en.wikipedia.org/wiki/Associative_entity) 
linking two rows in the [`FormTable`](../forms) of a [`Wordlist`](../../modules/Wordlist).
Thus, CLDF provides a borrowing table, with the default description
[`BorrowingTable-metadata.json`](BorrowingTable-metadata.json).

While ideally a particular source form in a particular donor language would be specified for each
borrowing, this can often not be done. In these cases
a `null` value for the `sourceFormReference` marks missing knowledge about the source word
(or donor language). A `comment` property SHOULD be used to describe the available knowledge.

Often datasets will add a column specifying reliability levels of the loan assessment
(e.g. WOLD's ["borrowed score"](http://wold.clld.org/terms#borrowed_score)),
but no common encoding scheme for such levels has been conventionalized yet.


## Example

[WOLD](https://wold.clld.org)'s `BorrowingTable` is described here: https://github.com/lexibank/wold/blob/v4.0/cldf/cldf-metadata.json#L533-L638

## [BorrowingTable](http://cldf.clld.org/v1.0/terms.rdf#BorrowingTable): `borrowings.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
[Target_Form_ID](http://cldf.clld.org/v1.0/terms.rdf#targetFormReference) | `string` | unspecified | References the loanword, i.e. the form as borrowed into the target language<br>References <code>FormTable</code>
[Source_Form_ID](http://cldf.clld.org/v1.0/terms.rdf#sourceFormReference) | `string` | unspecified | References the source word of a borrowing<br>References <code>FormTable</code>
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | unspecified | <div> <p> A human-readable comment on a resource, providing additional context. </p> </div> 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | multivalued | <div> <p>List of source specifications, of the form &lt;source_ID&gt;[], e.g. http://glottolog.org/resource/reference/id/318814[34], or meier2015[3-12] where meier2015 is a citation key in the accompanying BibTeX file.</p> </div> 