"""
Update the pycldf package
"""
import shutil

from clldutils.clilib import PathType

from cldfspec.util import REPO_DIR


def register(parser):
    parser.add_argument(
        '--pycldf-repos',
        type=PathType(type='dir'),
        default=REPO_DIR.parent / 'pycldf')


def run(args):
    pkg = args.pycldf_repos / 'src' / 'pycldf'
    for p in REPO_DIR.joinpath('components').glob('*/*.json'):
        shutil.copy(p, pkg / 'components' / p.name)
    for p in REPO_DIR.joinpath('modules').glob('*/*.json'):
        shutil.copy(p, pkg / 'modules' / p.name)
    shutil.copy(REPO_DIR / 'terms.rdf', pkg / 'terms.rdf')
