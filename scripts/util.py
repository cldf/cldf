# coding: utf8
from __future__ import unicode_literals, print_function, division
from xml.etree import ElementTree

from clldutils.path import Path

REPO_DIR = Path(__file__).resolve().parent.parent
NAMESPACES = {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dc": "http://purl.org/dc/terms/",
    "dctype": "http://purl.org/dc/dcmitype/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "owl": "http://www.w3.org/2002/07/owl#",
    "csvw": "http://www.w3.org/ns/csvw#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
}


def read_terms():
    return ElementTree.parse(REPO_DIR.joinpath('terms.rdf').as_posix())


def ns(qname):
    prefix, _, local_name = qname.partition(':')
    return '{%s}%s' % (NAMESPACES[prefix], local_name)


ONTOLOGY_URI = read_terms().find(
    './/%s' % ns('owl:Ontology')).attrib[ns('rdf:about')]


def term_uri(local_name):
    return '{0}#{1}'.format(ONTOLOGY_URI, local_name)
