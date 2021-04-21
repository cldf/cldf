# Entries

When dictionaries or lexicons are encoded using CLDF's `Dictionary` module,
each entry (a.k.a. headword, lemma, lemon's [LexicalEntry](http://lemon-model.net/lemon#LexicalEntry)) is stored as a row in the `EntryTable`.


## Example

See https://github.com/dictionaria/daakaka/blob/master/cldf/entries.csv

```csv
ID,Language_ID,Headword,Part_Of_Speech,1st_Person_Singular,2nd_Person_Singular,3rd_Person_Dual,3rd_Person_Singular,Dialectal_Variant,Encyclopedic_Information,Entry_IDs,Etymological_Source,Etymology,Lexical_Citation_Form,Paradigm,Reduplicated_Form,Usage
a,bpa,a,dem,,,,,,,,,,,,,
a_1,bpa,a,gram,,,,,,,,,,,,,
a_2,bpa,a,intj,,,,,,,,,,,,,
aa,bpa,aa,poss.pron,,,,,,,,,,,,,
```

