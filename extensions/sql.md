# CLDF SQL

CLDF (like CSVW) provides all information necessary to load CLDF data into a [SQL](https://en.wikipedia.org/wiki/SQL) database.
[pycldf](https://pycldf.readthedocs.io/en/latest/ext_sql.html) has exploited this fact for some time to provide conversion of CLDF to
SQLite.

To make SQL queries acting on CLDF data reusable (modulo well-known [incompatibility issues between SQL databases](https://en.wikipedia.org/wiki/SQL#Reasons_for_incompatibility)), 
CLDF SQL specifies [database schema](https://en.wikipedia.org/wiki/Database_schema) conventions to apply when loading 
CLDF datasets into SQL databases.

CLDF SQL implementations MUST provide a function or service that accepts a CLDF dataset locator and creates an SQL database
loaded with the data from the dataset at a specified loaction.


## Table and column names

To make the resulting SQLite database useful without access to the datasets metadata, terms of the CLDF ontology
MUST be used for database objects, i.e.
- table names are component names (e.g. `ValueTable` for a table with `propertyUrl` http://cldf.clld.org/v1.0/terms.rdf#ValueTable),
- column names are property names, prefixed with `cldf_` (e.g. a column with `propertyUrl` http://cldf.clld.org/v1.0/terms.rdf#id 
  will have the name `cldf_id` in the database),
- non-component tables must have the last path component of their `url` property as table name,
- non-CLDF columns keep their name.


## Association tables

When a table specifies a list-valued foreign key, an association table must be created to implement this many-to-many relationship.
The name of the association table is the concatenation of
- the url properties of the tables in this relationship or of
- the component names of the tables in the relationship.

E.g. a list-valued foreign key from the `FormTable` to the `ParameterTable` must result in an association table

```sql
CREATE TABLE `FormTable_ParameterTable` (
    `FormTable_cldf_id` TEXT,
    `ParameterTable_cldf_id` TEXT,
    `context` TEXT,
    FOREIGN KEY(`FormTable_cldf_id`) REFERENCES `FormTable`(`cldf_id`) ON DELETE CASCADE,
    FOREIGN KEY(`ParameterTable_cldf_id`) REFERENCES `ParameterTable`(`cldf_id`) ON DELETE CASCADE
);
```

while a list-valued foreign key to a custom table `custom.csv` will result in
```sql
CREATE TABLE `FormTable_custom.csv` (
    `FormTable_cldf_id` TEXT,
    `custom.csv_id` TEXT,
    `context` TEXT,
    FOREIGN KEY(`FormTable_cldf_id`) REFERENCES `FormTable`(`cldf_id`) ON DELETE CASCADE,
    FOREIGN KEY(`custom.csv_id`) REFERENCES `custom.csv`(`id`) ON DELETE CASCADE
);
```


### Association table `context`

Since there may be multiple list-valued foreign keys defined between the same pair of tables, the association table
must have a column `context`, which stores the name of the foreign key column to which a row in the association table
belongs.


## Sources

Items in a dataset's [sources reference file](https://github.com/cldf/cldf#sources-reference-file) must be loaded
into a table called `SourceTable`, 
- with a column `id` for the BibTeX citekey of an item,
- a column `genre` for the BibTeX entry type
- columns for each BibTeX field type that appears for any item in the file.

```sql
CREATE TABLE `SourceTable` (
    `id` TEXT,
    `genre` TEXT,
    ...
    PRIMARY KEY(`id`)
);
```

The list-valued pseudo-foreign keys specified by columns with `propertyUrl` http://cldf.clld.org/v1.0/terms.rdf#source
must - as above - result in an association table `<component>_SourceTable`. In the case of association tables with
`SourceTable`, the `context` column stores the citation context.


## Constraints

CLDF to SQL converters SHOULD add `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, `UNIQUE`, `NOT NULL` constraints as
appropriate for the database, to make as much CLDF metadata as possible inferrable from the database schema.


## Example

With the conventions specified above, the following query can be run on any CLDF StructureDataset containing a
`LanguageTable` and a `ParameterTable` to retrieve (language, parameter, value) triples:
```sql
SELECT
    l.cldf_name, p.cldf_name, v.cldf_value
FROM
    LanguageTable AS l, ParameterTable AS p, ValueTable AS v
WHERE
    v.cldf_languageReference = l.cldf_id AND v.cldf_parameterReference = p.cldf_id
```
