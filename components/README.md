# CLDF Components

CLDF components are tables which model (cross-linguistically meaningful) datatypes.

More complex, cross-linguistic datatypes, such as dictionariescan be modeled as [CLDF modules](../modules).

Tables are marked as CLDF component by adding a `dc:conformsTo` property to the table description
in the CLDF metadata file, having one of the [component ULRs](https://cldf.clld.org/v1.0/terms.html#components)
as value.
