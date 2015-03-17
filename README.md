# Cross-linguistic Data Formats

To allow exchange of cross-linguistic data and decouple development of tools and methods from that of databases, standardized data formats are necessary.

The main types of cross-linguistic data we are concerned with here are wordlists and structure datasets which are used in historical linguistics.


## Design goals

- Data should be both editable "by hand" and amenable to reading and writing by software.
- UTF-8 encoded text files.


## Core format specification

Data file accompanied by metadata


### Identifiers

Following our design goal to reference rather than duplicate entities, identifiers should be used to reference existing entities (e.g. Glottolog languages, WALS features, etc.). To do so, identifiers must be formatted as resolvable HTTP(S) URLs.

Alternatively, identifiers may be used to reference dataset local entities which are defined in the datasets metadata (or not at all). In this case identiers must be composed of the characters defined by the regular expression `[a-zA-Z0-9\-_]`. This restriction makes sure that these identifiers can be used as path components of HTTP URLs (see [rfc3986](https://tools.ietf.org/html/rfc3986#section-2.3)).


### The data file

- `Language_ID`
- `Source`
- `Comment`


## Data types

- [Wordlists](wordlist.md)
- [Structure dataset](structure_dataset.md)
