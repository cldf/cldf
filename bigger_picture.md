# The Bigger Picture

One of the main goals of the **cldf** specification is a useful delineation of data and tools. Using a `csv` 
based format makes it really easy to use this data in a 
[UNIX-style pipeline](https://en.wikipedia.org/wiki/Pipeline_%28Unix%29) of data transformation commands.
This pipeline-style of data transformation and analysis seems to be at the core of typical workflows e.g. in 
historical linguistics, e.g. [LingPy](http://lingpy.org/tutorial/workflow.html), [QLC](https://github.com/cysouw/qlcPipe).

If suitable text- and line-based formats are available, this pipeline-style does also allow for easy extensibility;
E.g. a workflow for automatic cognate judgements based on LingPy functionality could be extended with phylogenetic
analysis and post-processing via [phyltr](https://github.com/lmaurits/phyltr), which processes sets of phylogenetic trees represented in the newick format, or [ete](http://etetoolkit.org/documentation/tools/).

If cross-linguistic comparisons procede in the footsteps of bioinformatics, workflows based UNIX pipelines may at some point be formalized using a [common workflow language](http://common-workflow-language.github.io/).
