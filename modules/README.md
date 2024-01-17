# CLDF Modules

CLDF Modules are used to model complex cross-linguistic datatypes, which typically comprise
multiple [components](../components) - and may give the contained components particular semantics.
E.g. an [`ExampleTable`](../components/examples) in a [`StructureDataset`](StructureDataset) typically holds 
examples, illustrating particular feature codings in the dataset, whereas an `ExampleTable` in a `TextCorpus` holds the annotated
text of the corpus.

CLDF consumers can use the additional semantics conveyed through the module choice to inform
processing. For example a line of glossed text may be formatted as IGT example, including number, source
language and reference, if it is used as example in a `StructureDataset`. But the same line may be
just formatted as running text if it is used in a `TextCorpus`.

Datasets are marked as CLDF modules by adding a top-level property `dc:conformsTo`
in the CLDF metadata file, having one of the [module ULRs](https://cldf.clld.org/v1.0/terms.html#modules)
as value.
