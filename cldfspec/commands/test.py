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
                yield obj, 'propertyUrl', obj['propertyUrl'], obj.get('dc:extent'), obj.get('separator')
            elif 'dc:conformsTo' in obj:
                yield obj, 'dc:conformsTo', obj['dc:conformsTo'], None, None
        for v in obj.values():
            for prop in iterproperties(v, valueUrl=valueUrl):
                yield prop
    elif isinstance(obj, list):
        for v in obj:
            for prop in iterproperties(v, valueUrl=valueUrl):
                yield prop


def check_col(t, col, f, prop, val, extent, separator, log):
    if t.type == 'Property' and t.csvw_prop('name') != col['name']:
        # Column name must be the one recommended as csvw:name in the ontology.
        log.error('{}:{}:{}: name mismatch "{}" vs "{}"'.format(
            f, prop, val, t.csvw_prop('name'), col['name']))

    if t.csvw_prop('separator') and t.csvw_prop('separator') != separator:
        log.error('{}:{}:{}: separator mismatch "{}" vs "{}"'.format(
            f, prop, val, t.csvw_prop('separator'), separator))

    if t.csvw_prop('datatype') and t.csvw_prop('datatype') != col.get('datatype'):
        log.error('{}:{}:{}: datatype mismatch "{}" vs "{}"'.format(
            f, prop, val, t.csvw_prop('datatype'), col.get('datatype')))

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
        log.error('{}:{}:{}: cardinality mismatch'.format(f, prop, val))


def run(args):
    ontology = Terms(REPO_DIR / 'terms.rdf')

    # Make sure all term URIs in default metadata are defined in the Ontology:
    for d in ['components', 'modules']:
        for f in walk(REPO_DIR.joinpath(d)):
            if f.suffix == '.json':
                md = load(f)
                for col in iterproperties(md, valueUrl=True):
                    if col['name'] not in col['valueUrl']:
                        # Column name must be used (as template variable) in valueUrl.
                        args.log.error('{}:{}:{}: invalid valueUrl'.format(
                            f, col['name'], col['valueUrl']))
                for col, k, v, extent, separator in iterproperties(md):
                    if v not in ontology.by_uri:
                        args.log.warning('{}:{}:{}'.format(f, k, v))
                    else:
                        check_col(ontology.by_uri[v], col, f, k, v, extent, separator, args.log)
