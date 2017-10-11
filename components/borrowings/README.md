## Borrowings

Lexical borrowings or loanwords provide an interesting object of study by themselves
(see for example [The World Loanword Database](http://wold.clld.org/)), but they
also play a role for cognate detection algorithms, where it is typically important
to distinguish between cognates due to borrowing and cognates due to inheritance.

Conceptually, borrowings are the 
[associative entity](https://en.wikipedia.org/wiki/Associative_entity) 
linking two rows in the `FormTable` of a [wordlist](../../modules/Wordlist).
Thus, CLDF provides a borrowing table, with the default description
[`BorrowingTable-metadata.json`](BorrowingTable-metadata.json).

A `null` value for the `sourceFormReference` marks missing knowledge about the source word
(or donor language). In this case, a `Comment` should be used to describe the available
knowledge.

Often datasets will add a column specifying reliability levels of the loan assessment
(e.g. WOLD's ["borrowed score"](http://wold.clld.org/terms#borrowed_score)),
but no common encoding scheme for such levels has been conventionalized yet.
