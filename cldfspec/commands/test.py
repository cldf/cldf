"""
Check the spec for consistency
"""
from clldutils.path import walk
from clldutils.jsonlib import load

from cldfspec.util import REPO_DIR
from pycldf.terms import Terms


def iterproperties(obj, valueUrl=False):
    if isinstance(obj, dict):
        if valueUrl:
            if 'valueUrl' in obj:
                yield obj
        else:
            if 'propertyUrl' in obj:
                yield 'propertyUrl', obj['propertyUrl'], obj.get('dc:extent'), obj.get('separator')
            elif 'dc:conformsTo' in obj:
                yield 'dc:conformsTo', obj['dc:conformsTo'], None, None
        for v in obj.values():
            for prop in iterproperties(v, valueUrl=valueUrl):
                yield prop
    elif isinstance(obj, list):
        for v in obj:
            for prop in iterproperties(v, valueUrl=valueUrl):
                yield prop


def run(args):
    ontology = Terms(REPO_DIR / 'terms.rdf')

    # Make sure all term URIs in default metadata are defined in the Ontology:
    for d in ['components', 'modules']:
        for f in walk(REPO_DIR.joinpath(d)):
            if f.suffix == '.json':
                md = load(f)
                for col in iterproperties(md, valueUrl=True):
                    if col['name'] not in col['valueUrl']:
                        args.log.error('{}:{}:{}: invalid valueUrl'.format(
                            f, col['name'], col['valueUrl']))
                for k, v, extent, separator in iterproperties(md):
                    if v not in ontology.by_uri:
                        args.log.warning('{}:{}:{}'.format(f, k, v))
                    else:
                        t = ontology.by_uri[v]
                        try:
                            if extent:  # Cardinality specified via column descriptor's dc:extent.
                                if extent == 'multivalued':
                                    assert separator
                                else:  # singlevalued
                                    assert not separator

                            if t.cardinality:  # Cardinality specified in the ontology.
                                if t.cardinality == 'multivalued':
                                    assert separator and extent != 'singlevalued'
                                else:  # singlevalued
                                    assert (not separator) and extent != 'multivalued'
                        except AssertionError:
                            args.log.error('{}:{}:{}: cardinality mismatch'.format(f, k, v))