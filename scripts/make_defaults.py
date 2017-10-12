# coding: utf8
from __future__ import unicode_literals, print_function, division
from collections import OrderedDict
from json import loads

from clldutils.jsonlib import dump

from util import REPO_DIR, ns, read_terms

MODULES = {
    'Generic': [],
    'Wordlist': ['forms'],
    'StructureDataset': ['values'],
    'Dictionary': ['entries', 'senses'],
}

COMPONENTS = {
    'borrowings': {
        'table': 'BorrowingTable',
        'columns': [
            ('id', True),
            ('targetFormReference', True),
            ('sourceFormReference', False),
            ('comment', False),
            ('source', False),
        ]
    },
    'codes': {
        'table': 'CodeTable',
        'columns': [
            ('id', True),
            ('parameterReference', True),
            ('name', False),
            ('description', False),
        ]
    },
    'cognates': {
        'table': 'CognateTable',
        'columns': [
            ('id', True),
            ('formReference', True),
            ('cognatesetReference', True),
            ('alignment', False),
            ('source', False),
        ]
    },
    'cognatesets': {
        'table': 'CognatesetTable',
        'columns': [
            ('id', True),
            ('description', False),
            ('source', False),
        ]
    },
    'examples': {
        'table': 'ExampleTable',
        'columns': [
            ('id', True),
            ('languageReference', True),
            ('primaryText', True),
            ('analyzedWord', False),
            ('gloss', False),
            ('translatedText', False),
            ('metaLanguageReference', False),
            ('comment', False),
        ]
    },
    'languages': {
        'table': 'LanguageTable',
        'columns': [
            ('id', True),
            ('name', False),
            ('macroarea', False),
            ('latitude', False),
            ('longitude', False),
            ('glottocode', False),
            ('iso639P3code', False),
        ]
    },
    'parameters': {
        'table': 'ParameterTable',
        'columns': [
            ('id', True),
            ('name', False),
            ('description', False),
        ]
    },
    'partialcognates': {
        'table': 'PartialCognateTable',
        'columns': [
            ('id', True),
            ('formReference', True),
            ('cognatesetReference', True),
            ('slice', True),
            ('alignment', False),
            ('source', False),
        ]
    },
    'entries': {
        'table': 'EntryTable',
        'columns': [
            ('id', True),
            ('languageReference', True),
            ('headword', True),
            ('partOfSpeech', False),
        ]
    },
    'senses': {
        'table': 'SenseTable',
        'columns': [
            ('id', True),
            ('description', True),
            ('entryReference', True),
        ]
    },
    'values': {
        'table': 'ValueTable',
        'columns': [
            ('id', True),
            ('languageReference', True),
            ('parameterReference', True),
            ('value', False),
            ('codeReference', False),
            ('comment', False),
            ('source', False),
        ]
    },
    'forms': {
        'table': 'FormTable',
        'columns': [
            ('id', True),
            ('languageReference', True),
            ('parameterReference', True),
            ('lexicalUnit', True),
            ('soundSequence', False),
            ('comment', False),
            ('source', False),
        ]
    },
}


def csvw_prop(e, lname):
    if e.find(ns('csvw:{0}'.format(lname))) is not None:
        return loads(e.find(ns('csvw:{0}'.format(lname))).text)


def make_table(e):
    res = OrderedDict()
    res['url'] = csvw_prop(e, 'url')
    res['dc:conformsTo'] = e.attrib[ns('rdf:about')]
    res['tableSchema'] = OrderedDict([('columns', [])])
    return res


def make_column(e, required):
    res = OrderedDict()
    res['name'] = csvw_prop(e, 'name') or e.find(ns('rdfs:label')).text
    res['required'] = required
    res['propertyUrl'] = e.attrib[ns('rdf:about')]
    res['datatype'] = csvw_prop(e, 'datatype') or 'string'
    for k in ['separator', 'null', 'valueUrl']:
        v = csvw_prop(e, k)
        if v:
            res[k] = v
    return res


def make():
    tables = {}
    columns = {}

    for e in read_terms().iter():
        if ns('rdf:about') in e.attrib:
            lname = e.attrib[ns('rdf:about')].split('#')[-1]
            if e.tag == ns('rdfs:Class') and lname.endswith('Table'):
                tables[lname] = e
            elif e.tag == ns('rdf:Property'):
                columns[lname] = e

    comps = {}
    for subdir, spec in COMPONENTS.items():
        table = make_table(tables.pop(spec['table']))
        for c, req in spec['columns']:
            table['tableSchema']['columns'].append(make_column(columns[c], req))
        comps[subdir] = table
        dump(
            table,
            REPO_DIR.joinpath(
                'components', subdir, '{0}-metadata.json'.format(spec['table'])),
            indent=4)

    for subdir, comprefs in MODULES.items():
        dump(
            OrderedDict([
                ("@context", ["http://www.w3.org/ns/csvw", {"@language": "en"}]),
                ("dc:conformsTo",
                 "http://cldf.clld.org/v1.0/terms.rdf#{0}".format(subdir)),
                ("dialect", {
                    "doubleQuote": False,
                    "commentPrefix": None,
                    "trim": True,
                }),
                ("tables", [comps[ref] for ref in comprefs]),
            ]),
            REPO_DIR.joinpath('modules', subdir, '{0}-metadata.json'.format(subdir)),
            indent=4)


if __name__ == '__main__':
    make()
