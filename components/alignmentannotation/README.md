# Alignment Annotation

In the CLDF, we use space-separated strings for alignments, e.g. for [cognates](..\cognates) and possibly for [parallel texts](../../modules/ParallelText) in [FunctionalEquivalentsTable](../functionalequivalents).

Such alignments are actually secondary tables within the CSV structure of the CLDF data, i.e. there are columns **inside** one such column. To be able to refer to such 'secondary' columns we use an `alignmentAnnotationTable`. One line in such a table includes the name of the table that holds an alignment column (this name goes in the column `Alignment_ID`). Note that this is not a foreign key to a row in another table, but to a **column** in another table. The column does not have to be named, because the referenced table should only have a single column of the type [`#alignment`](http://cldf.clld.org/v1.0/terms.rdf#alignment).

Within such an alignment column we assume that the strings are aligned, so we can refer to a single column by a [`segmentSlice`](http://cldf.clld.org/v1.0/terms.rdf#segmentSlice") of an enumeration of the columns. For example, a reference to columns 3 and 4 of the alignments is simply `3:4` or `3 4`.

Any annotation can be specified in the `Annotation` column. In some cases, it is practical to name what type of annotation it is, which can be specified by using the secondary separator ":".

# Example

Consider a `cognates.csv` with a column `Alignment` like this:

```
Alignment
s x o: l -
s k u: l -
ʃ - u: l ə
```

We can now make annotation like

```
Segment_Slice Annotation
1 2           MERGE
5             IGNORE
1 2           German orthography:sch
3             German orthography:u
4             German orthography:l
5             German orthography:e
```