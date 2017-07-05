# Word Lists in CLDF

In this example, I want to show how CSV with Metadata can be used to 
parse the most important datastructures which are currently handled in wordlists in LingPy and EDICTOR. 

## Basic Values

* Language: A free identifier for a language, can also be used to distinguish different varieties of a given language if Glottolog does not yet distinguish them properly.
* Language_ID: The Glottocode of the language, if it is available.
* Concept: A free identifier for a concept, like the typical concept labels one often finds in datasets.
* Paramter_ID: The corresponding Concepticon Concept Set, if it is available.
* Value: The value (the word form) as it can be found in the original dataset.
* Form: A cleaned variant of the value in which multiple entries separated by comma or similar have been resolved by either taking only one of multiple forms in the same value, or by splitting the value into several forms, each with their own ID, placed in their own row.
* Source: The source or the sources for the given row in the file, usually given as a comma-separated list of BibTex-Keys.
* Comment: Free field for adding comments, only in human-readable form, but they could potentially contain markup (like MarkDown, etc.)

## Sequences

## Cognates

## Alignments

## Morphemes, Partial Cognate Sets, and Partial Alignments




