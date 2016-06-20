## Word Lists

### Prior art

- http://lingpy.org/tutorial/formats.html#wordlist-format-basic-format-for-storing-large-datasets
- http://lemon-model.net/
- http://www.lexicalmarkupframework.org/

### Word Lists from the Perspective of LingPy and EDICTOR

With [LingPy](http://lingpy.org) and the [EDICTOR](http://edictor.digling.org),
there are two tools that accept word list data and allow for further automatic
or semi-automatic manipulation. These two tools also offer a couple of
solutions for certain problems of modeling historical relations between words
in wordlists. It is further intended that both tools will fully support the
CLDF word list standard. Since many questions of how to handle specific cases
of word list annotations in detail are not yet solved, it may be useful to have
a look at the specifications underlying the two tools.

#### Minimal Word List Format 
  
In word list data, we are dealing with words and morphemes which are displayed
in data sets containing usually more than one language (multi-lingual word
lists). We can basically follow [Saussure (1916)](:bib:Saussure1916) in
constituting that a word has a form (*signifiant*) and a meaning
(*signifié*), but we need to add the language in which the word is used as a
third aspect.  With existing databases like [Glottolog](http://glottolog.org)
and the [CLLD Concepticon](http://concepticon.clld.org), two of the three
aspects of *language*, *concept*, and *form* are cross-linguistically covered,
and all three aspects constitute the minimal requirement for a word list in
CLDF format. Along with an identifier for each record, our minimal word list
format thus requires four fields (columns) in the CSV file:

* ID: (line, word) identifier
* Language_ID: the language identifier (e.g.m unique name or glottocode, if available)
* Concept_ID: the concept identifier (e.g., concepticon concept_set, if available)
* Word_form: the word form, the main value, for the given language and the
  given concept 

Language and concept labels may drastically vary across datasets, although the
same entities are referenced. Given the purpose of CLDF, we therefore encourage
the use of Glottolog and the CLLD Concepticon as basic sources for
standardization of language and concept identifiers. We should note, however,
that a Glottolog_ID and a Concept_ID as provided by Glottolog and the
Concepticon are not necessarily enough. First, if dialects are the object of
investigation, or different sources of a given language variety, we will want
to keep the data distinct, and additional identifiers for specific language
varieties or sources will be needed. Second, when dealing with specific
questionnaires, there may well be distinctions which do not (yet) find a
counterpart in the concepticon. We may also encounter situations where we only find
concept sets in the Concepticon that are too broad for a given dataset and
would cover two or more concepts. In all these cases, one needs to keep the
original data distinct.
 
In order to handle these cases, one could either modify the Language_ID and the
Concept_ID, or, one adds two more columns in which the data is represented as
originally intended and collected, with Language_ID and Concept_ID then serving
as a cross-linguistic reference, and the language and the concept column
serving for the original data. This would yield a new structure of a basic
dataset, with:

* ID
* Language (arbitrary unique identifier, usually the name that is used to
  denote the variety)
* Concept (arbitrary unique identifier, usually the original concept label)  
* Word_Form
* Language_ID
* Concept_ID

Note that, since we allow for additional meta-data in JSON-format, the
information regarding the cross-linguistic identifiers could as well be
provided in the meta-data and would thus reduce redundancy. 
 
The minimal form of ID, Language, Concept, and Word Form is generally accepted
by LingPy and EDICTOR. When passed additional columns named CONCEPTICON_ID and
GLOTTOLOG, the EDICTOR further automatically creates a hyperlink to the entries
in the two databases. For future versions of LingPy, a Concepticon
integration is planned, while a Glottolog integration was not yet discussed.
 
#### Handling Word Forms (Transcriptions)

LingPy and EDICTOR distinguish different degrees of phonetic transcriptions. A
valid phonetic transcription in LingPy is one that can be converted to sound
classes. Since sound classes reduce the space of IPA, this is less rigid than
real IPA, since LingPy tolerates many phonetic symbols which would not be
tolerated by IPA, like /č/ instead of /ʧ/, but also accepts different forms of
diacritics. The most recent version of LingPy even adds the possibility to
define semi-diacritics, that is, letters which occur often ambiguously in
diacritic position, such as /s/ and /h/, for example in /ts/ and /th/. These
specifications play an important role in the segmentation in LingPy, which is
handled by a specific function which is basically also used in the EDICTOR (but
in a less complex form). 

One extremely important requirement in LingPy and EDICTOR is that the level of
the original transcription is generally separated from the level of segmented
transcription, and that the segmented transcription is treated as the one that
is passed to machines. Segmentation is handled by adding spaces:

```text
word form: tʰɔxtər
segments: tʰ ɔ x t ə r
```

The use of spaces requires that spaces in original transcriptions are replaced
by other symbols. Here, LingPy and EDICTOR usually propagate the use of the
underscore:

```text 
segments: tʰ ɔ x t ə r _ o n tʰ _ m ʊ tʰ ə r
```

But due to compatibility with other projects, the hash-symbol is also accepted:

```text 
segments: tʰ ɔ x t ə r # o n tʰ # m ʊ tʰ ə r
```

A relatively new idea is to establish a cross-linguistic phonetic alphabet
(CLPA) which allows to rate whether a given transcription fulfills a certain
standard. In this alphabet, aliases for symbols which transcribe identical
pronunciations are defined (like /th/ being identical with /tʰ/ and /ts/
being identical with /ʦ/ and /t͡s/), but only one form is considered as the
representative version in CLPA. As a result, CLPA is more restrictive than IPA,
allowing, for example, only /ts/, and requiring space-segmented transcriptions,
as currently defined in LingPy and EDICTOR, but it will come along with a
conversion service that helps to convert given phonetic transcriptions to the
CLPA standard.  A proto-type of CLPA has been already created and is accessible
at [http://github.com/glottobank/clpa](http://github.com/glottobank/clpa).  A
JavaScript-application that tests whether the text inserted is in concordance
with CLPA is accessible at
[http://glottobank.org/clpa/clpa.html](http://glottobank.org/clpa/clpa.html).
The advantage of a CLPA is that all sounds in cross-linguistic datasets, once
conforming regularly to the given standard, can be mapped to additional
meta-data, including feature systems and more. The CLPA currently uses a
non-binary features system that is based on the IPA system employed by the
[PBase](http://pbase.phon.chass.ncsu.edu) project, but expands it by adding
tones and sound lacking in the original PBase project.

Segmentation adds at least one more possible column to the word list format
specification. LingPy usually calls this column "tokens", and so does EDICTOR,
but in the most recent versions, both tools have adopted the column name
"segments", since "tokens" turned out to be confusing for many users. 

#### Morphological Segmentation

As a further transcription layer, morphological segmentation plays an important
role in language comparison and a word list standard should allow for it.
LingPy and EDICTOR handle morphological segmentation with specific morpheme
separators which are added in the segmented phonetic transcriptions in the
"SEGMENTS" column of a word list. The symbols which are currently used are the
plus-symbol "+" and the dot-symbol "◦", which is often used as a morpheme
separator in South-East Asian languages:

```python
>>> from lingpy import *
>>> rc('morpheme_separators')
>>> '◦+'
```

The current handling of morpheme segmentation in LingPy and EDICTOR does not
allow for the distinction between prefixes and suffixes. For this reason,
additional symbols have been discussed, but are not yet supported. The most
straightforward solution for the annotation of suffixes seems to be the usage
of arrow symbols, like "→" and "←", since these would express that a given
morpheme is attached to another part of the word, such as a prefix:

```text
a n → k ɔ m ə n
```

and a suffix (here: verb-ending in German *ankomm-en*):

```text
a n → k ɔ m ← ə n
```

For both LingPy and EDICTOR, adding the arrow symbols would be easy to
implement and straightforward, and even infixes could be displayed as elements
which attach to two segments to the left and the right.

#### Handling Cognate Sets

Both LingPy and EDICTOR took their initial inspiration from
[STARLING](http://starling.rinet.ru). As a result, integer identifiers in a
specific column usually called COGID were used to indicate that two words are
cognate. Unlike the current version of the STARLING system in which cognate
identifiers are locally definied with respect to a concept, LingPy and EDICTOR
always treated cognate identifiers as *global*, as it was also done in the
earlier STARLING system. There are many good reasons to treat cognate
identifiers as global:

* global cognate identifiers are completely compatible with local annotations,
  while the opposite is not true, 
* global cognate identifiers can be used for local, within concept-set
  annotation of cognacy, as well as for global, cross-semantic etymological
  dictionaries, and
* global cognate identifiers correspond directly to the classical style of
  cognate set coding used for most phylogenetic analyses.

While LingPy has a pre-defined set of names for cognate identifiers, the
EDICTOR potentially treats all column names ending in `*`ID as identifiers for
cognate words, or, more specifically, as identifiers with integer keys.
LingPy-2.5 still retains this behaviour but now also allows for non-integer
identifiers for cognate sets, and the EDICTOR allows any column
can be specified as a column containing cognate identifiers, while assuming as
a default that COGID and column names ending in ID are the best candidates.

Given the fact that we might want to handle different kinds of cognate
judgments in our data, it is essential that we do not restrict the namespace too
rigidly in the general format, but allow for a lot of flexibility. Only when we
allow for this, we will be able to handle, for example, multiple cognate
judgments, in the same file.

#### Beyond Cognacy

It is clear that cognacy is in its core not a binary concept (word X is cognate with Y or not), but rather a concept of "degree". Depending on our perspective, words can exhibit different degrees of cognacy, and in all these cases, morphological change plays a crucial role. When dealing with compounding patterns, for example, we could talk of "partial cognacy", and in this way, we could say that English *fingernail* is partially cognate with Russian *nogot'*, since the *nail* in English is cognate with *nogot'* in Russian (albeit not completely, as can be seen from the *l* in English which misses a counterpart in Russian, or the *t'* in Russian, missing a cognate sound in English).

LingPy and EDICTOR allow for a rough handling of partial cognacy, which is represented as a sequence of integer IDs separated by a space which describes the cognate relations of each morpheme in a word. Our example of English and Russian would thus be displayed as:

Language | Word Form | Segments | Cognate IDs |
--- | --- | --- | --- |
English | fingernail | f i ŋ ə r + n æi l | 1 2 |
Russian | nogot' | n o g o tj | 2 |

This format requires that the field for SEGMENTS contains as many morphemes as the field for COGNATE IDs. As a general convention, elements which are not assigned to anything else (or not yet inspected by anybody), are represented with a 0 in LingPy and EDICTOR. This distinction is important, since there is a different quality between annotating that one has not really looked at a word, or does not know whether it has cognate elements in other words, or that one knows that it has no reflex in any other language. If we did not know what to do with the *finger* in English, we could thus also simply annotated it as a "0".

While LingPy has automatic ways to infer partial cognates in datasets, EDICTOR provides ways to specifically annotated partial cognates. The current system of annotation has thus already been sufficiently tested, and was even very successful in allowing us to quickly annotate large amounts of data in this way.





=======

### The data file

In addition to the core column names required in each row of the data file, the following columns are required in wordlists:

- `Word_form`: the entry as it occurs in the source.
- `IPA`: IPA transcription (in phonological segmentation with help of space separators, allowing also for morphemic segmentation, full format description pending) 
- `Concept_ID`: concepticon concept set URL or ID

Recognized optional columns:

- `Cognateset_ID`: e.g. http://ielex.mpi.nl/cognate/2549/
- Space-separated list of tags to allow filtering, etc.
- `Inventory_ID`: [PHOIBLE inventory ID](http://phoible.org/inventories/view/1617) specifying the symbol set used for the IPA transcription
- `Gloss_in_source`: The gloss as it appeared in the source.


### Specific design features

For the computer-human interface and the interaction between various software tools (be they based on purely computer-based or computer-assisted frameworks), we need to define certain aspects of data representation, including a representation of multiple alignments, cognate sets, and the like.

So far, it seems that the following specific features of wordlists, we can basically distinguish two major aspects, namely the aspect of *sequence representation* and the aspect of *sequence relations*. Note that in this context, a *sequence* is primarly understood as some kind of a phonetic string which denotes a concept in some language. So in order to specify a phonetic sequence, we will always need to identify it with some language (doculect) and some concept.

#### Sequence Representation

In order to represent sequences, we will need to distinguish different levels of analysis. Depending on the computational approach we use, we may require a specific representation, and computational approaches should ideally indicate what kind of sequence representation they need. So far, the following representation types seem to be useful for cross-linguistic data formats:

* raw sequence (*entry_in_source*): this refers to the way we find the phonetic entry in text-books and the like. It may be an orthographic representation, some high-quality narrow IPA string, but also an ugly quasi-IPA which contains additional comments in brackets (as we will find it in many sources), etc. What is important, is, that this representation won't serve as input for any computational analysis, and that it also won't be directly used in computations and analyses. It just serves to trace back to the original source where it was first published.
* IPA string (*IPA*): this should be rather self-explaining. We can discuss whether we wish to restrict IPA strings (if we label them as such) to a specific version of IPA, like, e.g., PHOIBLE, or Chinese dialectology IPA, or African linguistics IPA, or even SAMPA (which can be seen as a narrower dialect than normal IPA (?), since it only allows the use of characters that are officially defined and it reduces certain ambiguities (my intuition tells me that this is the case, but I can't think of examples)). If we decide to do so, we should add the corresponding IPA-dialect in some meta-information file.
* segmentized IPA string (*TOKENS*, or *SEGMENTS*): this refers to a segmentized variant of the *IPA* string in which space characters are used to indicate the segmentation of IPA characters into phonological units. While the use of space characters is straightforward, we need to define an additional character that is used instead of a space if multiple words are encoded as one entry. Thus, a phrase like German "der Garten" could then be represented as "deR gaRt@n" (using sampa for convenience here) and would be segmentized as "d e R _ g a R t @ n", with an underscore indicating the further segmentation into two words. We thus need to specify additionally, which characters we allow to indicate the space in the normal *IPA* representation (could think of "#" and "_", both being treated identically in LingPy)
* morpheme-segmentized IPA string (*MORPHEMES* (?)): Cannot think of a better name right now, but the main idea is to allow for an even narrower representation of phonetic sequences by adding an additional layer of morphological segmentation, which will be important in many language families which make extensive use of morphological suffixes but also of compounding. So far, it seems that it is enough to define only one character for morphological segmentation, that is, one character that indicates that the units it segmentizes all code for a specific meaning. Here, we need to decide which characters to use (lingpy currently allows to use both "+" and "◦" (used in some Sino-Tibetan studies) to indicate morphological segmentation). As an example, we could segmentize German "laufen" as "l au f + @ n", with "+" indicating morphological boundaries. We should keep in mind that it may be useful to indicate further information, like what is the "main root" of a given word, but it seems that this information should be added in an additional column, where it could then be explicitly marked (probably also in terms of traditional glossing), like, for example "{WALK} + INFINITIVE". In this way, we only need one character for morpheme segmentation.  

#### Sequence Relations

Here, we define relations between sequences. The important pre-condition is that we allow to cluster sequences in sets, using some kind of ID. So everything starts from some kind of "cognate set ID" (an integer in LingPy), but we should be aware that we may have different layers of clustering and will thus need multiple possible cognate IDs both to reflect different degrees of cognacy, but also to reflect different opinions regarding cognacy. So the following columns seem to be useful:

* cognate identifier (*COGID*, but also further layers, basically "arbitrary", we could decide that they all should and on "ID" or something else indicating that this indicates a historical relations among words)
* alignment (*ALIGNMENT*, but probably something that is more expressive): an aligned representation of the phonetic sequence, which follows its basic segmentation and differs from it in so far, as it may contain gap characters, for which we use the dash as a default "-". Note that alignments are always defined for one specific "cognate ID", so we might want to indicate this already in the column name, giving the same basic name to both the cognate ID column and the alignment column, maybe with different prefixes (e.g., "LEXSTAT_COG", "LEXSTAT_ALM", but this is just a thought). Alignments are further specified by:
  * unalignable parts, indicated by adding brackets, thus German "laufen" and English "leap" could be represented as 
    - `l i: p ( - - )` and
    - `l au f ( e n )`
  * contextually dependend parts can be indicated by adding squared bracets, which is useful for metathesis, like for Bulgarian "jabelka" and Russian "jabloko" (we need to see whether this is enough for metathesis, it is definitely enough for palatalization and the like:
    - `j a b [ e l - ] k a`
    - `j a b [ - l o ] k a`
* partial cognacy: it may be useful to indicate partial cognacy for related compound words. Here, we could again use identifiers for each morpheme, separated by a space and following the morpheme structure. Thus, English "husband" and German "Hausmeister" could be rendered as:
  - `1 2` for "hus+band", and
  - `1 3` for "Haus+meister",
  indicating that the first part of the compound words is cognate.

