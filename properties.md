# CLDF properties

This is a easily readable, but non-normative list of properties as defined in the CLDF Ontology (see [`terms.rdf`](terms.rdf)). Please note that this file is just for easier reference, but is not normative: in case of discrepancy, the description in `terms.rdf` holds. The `rdf:label` is given in boldface and the `csvw:name` in brackets.

* Generic properties

    * **ID** (ID): A unique identifier for a row in a table. To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen.
    * **Name** (Name): A title, name or label for an entity.
    * **Description** (Description): A description for an entity.
    * **Slice** (Slice): Slice specification following Python's slice notation
    * **Source** (Source): Semicolon-separated source specifications, of the form 'source_ID[]', e.g. http://glottolog.org/resource/reference/id/318814[34], or meier2015[3-12] where meier2015 is a citation key in the accompanying BibTeX file.
    * **Comment** (Comment): A human-readable comment on a resource, providing additional context.

---

* Reference properties (aka foreign keys)

    * **Language Reference** (Language_ID): An identifier referencing a language either
        - by providing a foreign key into the LanguageTable or
        - by using a known encoding scheme.
    * **Meta-language Reference** (Language\_ID_Meta): An identifier referencing the meta language - e.g. of the translation of an example - either
        - by providing a foreign key into the LanguageTable or
        - by using a known encoding scheme.
    * **Parameter Reference** (Parameter_ID): An identifier referencing a parameter either
        - by providing a foreign key into the ParameterTable or
        - by using a known encoding scheme.
    * **Code Reference** (Code_ID): An identifier referencing a code (aka category) description by providing a foreign key into the CodeTable.
    * **Example Reference** (Example_ID): An identifier referencing an example by providing a foreign key into the ExampleTable.
    * **Entry Reference** (Entry_ID): An identifier referencing a dictionary entry by providing a foreign key into the EntryTable.
    * **Form Reference** (Form_ID): An identifier referencing a form by providing a foreign key into the FormTable.
    * **Source Form Reference** (Form\_ID_Source): An identifier referencing the source form of a loanword by providing a foreign key into the FormTable.
    * **Target Form Reference** (Form\_ID_Target): An identifier referencing a loanword by providing a foreign key into the FormTable.
    * **Cognateset Reference** (Cognateset_ID): An identifier referencing a cognateset either
        - by providing a foreign key into the CognatesetTable or
        - by using a known encoding scheme.

---

* Language properties 

    * **ISO 639-3 code** (Iso): An ISO 639-3 language code, i.e. a three-letter code denoting a valid ISO 639-3 language or macrolanguage.
    * **Glottocode** (glottocode): A Glottolog code denoting a languoid.
    * **Macroarea** (Macroarea): A macroarea as defined by Glottolog.
    * **Latitude** (Latitude): A latitude in the WGS 84 standard coordinate system, specified as decimal number of degrees.
    * **Longitude** (Longitude): A longitude in the WGS 84 standard coordinate system, specified as decimal number of degrees.

---

* IGT example properties 

    * **Primary Text** (Primary): The primary text of an example.
    * **Analyzed Word** (Analyzed): The morpheme-pattern analysis of a word in an example.
    * **Gloss** (Gloss): A gloss corresponding to the morpheme-pattern analysis of a word in an example.
    * **Translated Text** (Translation): The translated text of an example.

---

* Dictionary entry properties

    * **Headword** (Headword): The headword of a dictionary entry.
    * **Part of speech** (Part\_Of_Speech): The part-of-speech of dictionary entry.

---

* Value properties
    
    * **Value** (Value): The value (a.k.a. datapoint or measurement) of a language for a structural feature. For features with a limited, discrete set of valid values (a.k.a. categorical variables) it is recommended to relate items of a ValueTable to the respective code in the CodeTable.

---

* Cognate properties
        
    * **Alignment** (Alignment): An alignment represents segments which are grouped into a common cognate set as a matrix in which cognate segments are placed in the same column while gap characters are introduced in those sound sequences missing a certain counterpart.

---

* Form properties

    * **Concept Set** (Concepticon_ID): A concept set groups a number of concept labels which are used in different questionnaires and were judged to denote the same concept despite potential differences among the concrete concept labels (be it their spelling, or the language in which they were originally created).
    * **Lexical Unit** (Form): A lexical unit is any collection of word forms corresponding to a certain meaning which can be found in comparative datasets. Ideally, a lexical unit would just present itself as one single form. However, in practice, scholars often list speech variants and at times even non-cognate alternatives for their preferred form.
    * **Motivation Structure** (Motivation): The motivation structure of a word form gives glosses for each of its morphemes. In this it is similar to an instance of interlinear glossed text which describes the underlying semantic motivation for a given word form. As an example, consider Chinese shùpí 'bark (of a tree)' which is a compound consisting of shù 'tree' and pí 'skin', and whose motivation structure could be rendered as 'tree bark'.
    * **Prosodic Structure** (Prosody): The prosodic structure of a word form labels similar prosodic contexts which may recur even within the same word. Prosodic structures for a given language may have an underlying template that describes which syllables are possible. In Chinese dialects, for example, one could describe the basic template of most syllables as consisting of initial, medial, nucleus, coda, and tone, of which the nucleus and the tone as a suprasegmental element are usually the only required elements.
    * **Root** (Root): The root of a word form is an abstract basic unit from which several stems can be derived.
    * **Stem** (Stem): A stem is a concrete word form in a language which has been derived as such from a given root.
    * **Sound Sequence** (Segments): A sound sequence is understood as the strict segmental representation of a form unit of a language, which is usually given in phonetic transcription. Suprasegmental elements, like tone or accent, of sound sequences are usually represented in a sequential form, although they are usually co-articulated along with the segmental elements of a sound sequence. Alternatively, suprasegmental aspects could also be represented as part of the prosodic structure of a word form.
    * **Subsequence** (Segments): Word forms can often be subdivided into smaller functional units (usually corresponding to a morpheme). A subsequence of a sound sequence, however, does not necessarily need to represent a true morpheme, but rather a unit that is determined by scholars to serve as the basis for historical comparison.
