"""
Check the spec for consistency
"""
from clldutils.path import walk
from clldutils.jsonlib import load

from cldfspec.util import REPO_DIR, read_terms, ns

#
# FIXME: check cols in metadata for consistency with ontology!
#

def iterproperties(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield k, v
            for prop in iterproperties(v):
                yield prop
    elif isinstance(obj, list):
        for v in obj:
            for prop in iterproperties(v):
                yield prop


def run(args):
    terms = []
    for e in read_terms().iter():
        if ns('rdf:about') in e.attrib:
            terms.append(e.attrib[ns('rdf:about')])

    # Make sure all term URIs in default metadata are defined in the Ontology:
    for d in ['components', 'modules']:
        for f in walk(REPO_DIR.joinpath(d)):
            if f.suffix == '.json':
                md = load(f)
                for k, v in iterproperties(md):
                    if k in ['propertyUrl', 'dc:conformsTo'] and v not in terms:
                        print(f)
                        print(v)
