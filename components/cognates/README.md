## Cognates

A major use case of wordlists in historical linguistics is as basis for the assembling of
cognate sets. Assigning forms to cognate sets is itself a (rather large) step
in analyzing the wordlist data, but also serves as intermediate step before
feeding the cognate sets into further analyses e.g. to determine language relatedness.

Thus, being able to exchange data on cognate judgements related to wordlists
is important, and therefore covered by CLDF.

A cognate table, i.e. a table ẁhich `dc:conformsTo` `http://cldf.clld.org/v1.0/terms.rdf#CognateTable` has
the following columns:
- `Word_ID`: required; a foreign key to the `FormTable` of the wordlist
- `Cognate_set_ID`: required; an identifier of the cognate set a form is judged to belong to
- `Alignment`: optional; an [alignment](http://cldf.clld.org/v1.0/terms.rdf#alignment) of the segments of the form within its cognate set. Since alignments can make cognacy judgements more transparent and because they typically are somewhat expensive to compute, they should be stored and provided with a `CognateTable`
- `Cognate_source`: [source specification](http://cldf.clld.org/v1.0/terms.rdf#source) listing sources of the cognacy judgement
- `Alignment_source`: [source specification](http://cldf.clld.org/v1.0/terms.rdf#source) listing sources of the alignment

It is recommended to add columns or other metadata describing the method used
for the cognacy judgenments and the alignments, but no clear standard for these
has evolved yet.
