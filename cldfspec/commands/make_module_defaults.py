"""
Create the module default metadata files by plugging the appropriate component table
descriptions into a TableGroup.
"""
from collections import OrderedDict

from clldutils.jsonlib import dump, load

from cldfspec.util import REPO_DIR


MODULES = {
    'Generic': [],
    'Wordlist': ['forms'],
    'StructureDataset': ['values'],
    'Dictionary': ['entries', 'senses'],
    'ParallelText': ['forms'],
    'TextCorpus': ['examples'],
}


def read_comp(name):
    return load(list(REPO_DIR.joinpath('components', name).glob('*.json'))[0])


def run(args):
    for subdir, comprefs in MODULES.items():
        dump(
            OrderedDict([
                ("@context", ["http://www.w3.org/ns/csvw", {"@language": "en"}]),
                ("dc:conformsTo",
                 "http://cldf.clld.org/v1.0/terms.rdf#{0}".format(subdir)),
                ("dialect", {
                    "commentPrefix": None,
                }),
                ("tables", [read_comp(ref) for ref in comprefs]),
            ]),
            REPO_DIR.joinpath('modules', subdir, '{0}-metadata.json'.format(subdir)),
            indent=4)
