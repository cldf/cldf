# coding: utf8
from __future__ import unicode_literals, print_function, division
from xml.etree import ElementTree

from clldutils.path import walk, Path
from clldutils.jsonlib import load

REPO_DIR = Path(__file__).resolve().parent.parent


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


def run():
    terms = []
    for e in ElementTree.parse(REPO_DIR.joinpath('terms.rdf').as_posix()).iter():
        if '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about' in e.attrib:
            terms.append(e.attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about'])

    for d in ['components', 'modules']:
        for f in walk(REPO_DIR.joinpath(d)):
            if f.suffix == '.json':
                md = load(f)
                for k, v in iterproperties(md):
                    if k in ['propertyUrl', 'dc:conformsTo'] and v not in terms:
                        print(f)
                        print(v)


if __name__ == '__main__':
    run()
