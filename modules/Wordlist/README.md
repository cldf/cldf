# Wordlist Module

In CLDF wordlists are marked by a common property `dc:conformsTo` with value
[`http://cldf.clld.org/v1.0/terms.rdf#StructureDataset`](http://cldf.clld.org/v1.0/terms.rdf#StructureDataset)
on a `TableGroup`.

In the simplest case, a wordlist is just a list of triples *(language, concept, word)*,
thus in CLDF only a [`FormTable`](../../components/forms) is required.


## Introduction

Providing support for the handling of lexical data is one of the core goals of CLDF. By now, many examples on how to handle certain kinds of data have been presented in talks but also implemented in different tools, including [LingPy](http://lingpy.org) and [EDICTOR](http://edictor.digling.org). Lexical data is to a large extent much more amenable to strict cross-linguistic formalization than other types of linguistic data, but it is obvious that not all language-specific problems can be handled at once. A general idea behind CLDF is to not be intimidated by apparent complexity but instead to try to amplify the power of standards step by step.

The framework for lexical specifications, appropriate for word list data, is roughly oriented toward the model of the linguistic sign (which can be a word but also a morpheme) which consists of a **language** in which the sign is expressed, a **meaning** that the sign expresses, and a **form** that denotates the meaning. 
- Language specification should be done by linking to reference catalogs like Glottolog, but specifications of linguistic varieties may need to be more fine-grained than e.g. Glottolog allows at the moment. 
- Meaning specifications again should use reference catalogs like Concepticon. This may not be possible, though, in very specific dialect datasets where many cultural terms are of interest when studying language variation.

It should be noted that both, Glottolog and Concepticon, offer ways to add new language varieties or concepts via contributions to the respective database. 

Handling of the linguistic form is more complex and requires different layers of detail, starting from rough orthographic representations, up to sound sequence specifications which are cross-linguistically comparable.
While efforts to address this problem are under way (see for example the specification of orthography profiles in the [Unicode Cookbook for Linguists](https://github.com/unicode-cookbook/cookbook)), no commonly used standard has evolved so far.

In addition to the trias of language, form, and meaning, the word list specification of CLDF also handles **relations** between the entities. Relations come in two general flavors: relations across languages, and relations within one language. The former are reflected in detailed specifications for the handling of different kinds of **cognacy** in a broader sense (akin to the concept of **homology** in biology, thus including borrowings, [List 2016](:bib:List2016i)). Language-internal relations point to language-internal cognacy, that is, form-associations within one language across different meanings, ranging from simple cases of **colexifications** up to fine-grained accounts on **internal reconstruction**. Language-internal relations require additional markup that indicates relations of forms within one language using different kinds of specification.  

## Forms in Word Lists

See [FormTable](../../components/forms/).


## Form Relations across Languages

### General Specifications

Cognate annotation is usually handled by grouping word forms in a given word list into clusters. Words in one cluster are usually supposed to be cognate in the one or the other sense. Apart from this coarse cognate relation, however, examples for more fine-grained analyses are available, and will be supported by `cldf`. Often, word lists use the same identifiers for unrelated words, pre-supposing that cognacy is only defined within one concept. This is the current practice in the [Global Lexicostatistical Database](http://starling.rinet.ru), but given that cognacy may easily also be defined across meanings, `cldf` favors a strict coding in which the implicit assumption of not annotating cognates within more than one concept is made explicit by using different identifiers. The conversion is usually trivial, but it should be kept in mind when preparing datasets, and our `cldf` checks test automatically, whether a dataset annotates cognates across concepts (*cross-semantic cognates*). In addition to abstract cognate relations, distinct relations between sound segments, the supposed cognacy of sounds, are handled in *alignments*, which are added as a separate column and represent the homology of sounds across languages within one cognate set by adding gap-characters (a simple dash: "-") in those positions where a sound in one language corresponds to no sound in another language. An important addition to the currently common annotation of full cognacy are partial cognates. Partial cognates require a morphological segmentation of the respective **Segments** in the form representation, and allow to define which parts of a common word form are cognate across languages. 

All in all this, gives us the following additional columns currently supported by `cldf`:

COLUMN | TYPE | NOTE
--- | --- | ---
Cognate_Set | string or integer (LingPy, EDICTOR) | An identifier that is used to group word forms across languages. As a minimum, this requires a non-empty **Value** field in the word list.
Alignment | space-separated string | All cognate sets grouped by an identifier can be represented as alignments, if valid **Segments** are specified. All alignments of a given cognate set need to have the same length, and when removing gap symbols and brackets (indicating unalignable parts), they need to be identical with the corresponding value in **Segments**
Cognate_Sets | space-separated string or integers (LingPy, EDICTOR) | If the value in **Segments** separates morphemes, each morpheme needs to be assigned a cognate set identifier. In LingPy and EDICTOR, where only integers are allowed, the identifier 0 indicates that the form is unassigned to any other cognate set, but in general, we recommend to use unique identifiers here. Cognate sets for the representation of partial cognates follow the order of the morphemes into which the form in **Segments** can be split. This allows us to handle also those relations, where cognate parts have been swapped. 
Alignments | space-separated string | In order to represent alignments for partial cognate sets, all cognate sets are again aligned, following the same specification as for the "normal" alignments, with the exception that the order follows the order of morphemes in **Segments**. This may yield a form that is difficult to read in a plain text file or a spreadsheet editor, but it guarantees that alignments can be read in by a machine. For the editing of the alignments, the EDICTOR offers a convenient solution, and also a useful interactive representation.

A note on protoforms: So far, we have not yet decided how to handle proto-forms, and adding proto-forms in an extra column would be quite redundant. A workaround would be to allow protoforms empty, so that it would be enough to add one protoform. Another possibility would be to include the proto-language as a separate language.

**General Suggestions:** If we allow for annotations for cluster data that the relevant information is stored in a single cell of any of the relevant rows in the table, we could easily handle cases like proto-forms without being forced to add this information in a separate row that would anyway be incomplete. Computationally, this would be feasible, as it would require at most a second parse of the data after pre-parsing them initially. Even simpler, in tools like LingPy and EDICTOR, this parse could be done dynamically, if the information is needed.

**Additional Note:** Cognate sets and alignments are information that may be given not only in one version, but in many different versions, especially when contrasting different analyses, or maybe an automatic versus a manual annotation. Therefore, the **Cognate_Sets** and the **Cognate_Set** are elements which default to this interpretation, but additional columns can be added in free form. The metadata should specify the basic type (e.g., **Alignment**, or **Alignments**), and a source for the basic type should ideally be added in the metadata. We suggest to use the original names, like **Alignment** as suffixes for the column names. For example, for alignments retrieved by the SCA algorithm, one could write **SCA_Alignments**, and for cognate sets retrieved by the LexStat algorithm, one could write **LexStat_Cognate_Sets**. 

### Specific Handling of Roots and Stems

Roots and stems cause difficult problems for alignments, as they do not directly allow to align words, e.g., in situations where we have a cognate root but the analysis of main-stream linguistics assumes that the stems differ (ablaut, suffixes, and related phenomena). In order to account for this, once could either use the specific annotation for unalignable parts in sequences, but this will render hierarchical relations problematic. As an alternative, users could add root and stem information on top of a partial cognate annotation. The root-form is a form that should allow the derivation of the stem, following a set of rules which needs to be stored in the metadata (**not yet implemented, since more examples are needed**). The root form here serves to combine the words under a single cognate set, while the stem is the proto-form that will be fed into the alignment and from which the reflexes in the daughter languages should be derivable. Currently, no algorithms to retrieve this kind of data automatically exist, but if data is encoded in this way, it is straightforward to apply sanity checks to test consistency. In terms of cognate coding, we would have effectively two layers: one layer defining root cognacy, for which the **Cognate_Set** column should be used, and one layer defining partial cognacy, for which the **Cognate_Sets** column should be used. Common prefixes would here receive the same partial cognate set identifier, but roots which are derived via processes modifying the basic root structure, and which are thus unalignable, should receive different identifiers. 

COLUMN | TYPE | NOTE
--- | --- | ---
Root | space-segmented string | The root element from which a **Stem** can be derived.
Stem | space-segmented string | The stem derived from the root and which may have morphological segmentation. It will link to the reflexes in the **Segments** via the **Cognate_Sets** specifiers.


## Annotation of Language-Internal Relations

An important and new aspect of annotation in `cldf` which is implemented by EDICTOR and analysable within LingPy are language-internal cognate sets. The basic idea is to add a new column specifying the conceptualization of a word form. This is important in derived word forms and compounds. For example, the compound *sunflower* is effectively built from two words, *sun* and *flower*. If morphemes are segmented in the **Segments** of a word list, one can add a new column called **Morphemes** in order to specify the conceptualization. This is a space-segmented string in which each part annotates the original meaning of one of the morphemes. For *sunflower* it would just be `sun flower`. When comparing inside the English words of a given word list, one would then be able to retrieve that the word *sunflower* is partially cognate with *sun* and with *flower*. This also allows for an automatic annotation of cross-semantic relations across languages, since, if one language colexifies two concepts, like, e.g., "arm" and "hand" one could annotate this as `arm-hand` (one morpheme) in both semantic slots, and compare both the "arm" and the "hand" slot with other languages for cognacy. In this way, one can also handle dependencies in word lists resulting from lexicostatistical data encoding which separates cognate sets due to their meaning.

COLUMN | TYPE | NOTE
--- | --- | ---
Morphemes | space-segmented string | Requires morpheme segmented **Segments** and allows for a free annotation by the user, using short glosses for elements of a word form that recur across a language (and should not contain a space!).


