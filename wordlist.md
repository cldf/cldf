## Wordlists

### Prior art

- http://lingpy.org/tutorial/formats.html#wordlist-format-basic-format-for-storing-large-datasets
- http://lemon-model.net/
- http://www.lexicalmarkupframework.org/

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

