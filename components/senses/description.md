# Senses

When dictionaries or lexicons are encoded using CLDF's `Dictionary` module,
each entry may be related to multiple senses (lemon's [LexicalSense](http://lemon-model.net/lemon#LexicalSense)) stored as rows in the `SenseTable`.


## Example

See https://github.com/dictionaria/iquito/blob/main/cldf/senses.csv

```csv
ID,Description,Entry_ID,Anthropology_Note,Grammar_Note,Scientific_Name,Sociolinguistics_Note
SN000001,"play a trick on someone, joke with someone by deceiving them or deliberately lying to them",LX000001,,,,
SN000002,play with,LX000001,,,,
SN000003,alone,yaajaa,,,,
SN000004,the.same,yaajaa,,,,
SN000005,thigh,LX000002,,Poss.pref,,
SN000006,leg,LX000002,,"In this sense, ‘thigh’ serves as a metonym for the entire limb. Poss.pref",,
SN000007,"his, her, or its thigh",LX000003,,,,
SN000008,"his, her, or its leg",LX000003,,,,
SN000009,vulva,LX000004,,Poss.pref,,
...
```