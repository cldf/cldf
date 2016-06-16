from __future__ import unicode_literals
from sqlalchemy.orm import joinedload, contains_eager, joinedload_all

from pycldf.dataset import Dataset
from pycldf.sources import Source
from clld.scripts.util import parsed_args, ExistingDir
from clld.db.meta import DBSession
from clld.db.models.common import (
    Parameter, ValueSet, Language, ValueSetReference, Contribution, Identifier,
)
from clld.web.util.helpers import text_citation


def bibrecord2source(req, src):
    rec = src.bibtex()
    rec['wals_url'] = req.resource_url(src)
    return Source(rec.id, rec.genre.value if rec.genre else 'misc', **dict(rec.items()))


def cldf_pages(pages):
    if pages:
        return '[%s]' % pages.replace(';', '.').replace('[', '{').replace(']', '}')
    return ''


def format_refs(req, obj):
    sources = []
    refs = []
    for r in obj.references:
        if r.source:
            refs.append('%s%s' % (r.source.id, cldf_pages(r.description)))
            sources.append(bibrecord2source(req, r.source))
    return ';'.join(refs), sources


def url_template(req, route, variable):
    tmpl = req.route_url(route, id='__s__%s__e__' % variable)
    return tmpl.replace('__s__', '{').replace('__e__', '}')


def write_cldf(req, contrib, valuesets, features, outdir):
    ds = Dataset('wals-chapter-%s' % contrib.id)
    ds.fields = (
        'ID',
        'Language_ID',
        'Language_name',
        'Parameter_ID',
        'Value',
        'Source',
        'Comment')
    ds.metadata['tableSchema']['aboutUrl'] = url_template(req, 'valueset', 'ID')

    ds.metadata['tableSchema']['columns'][1]['valueUrl'] = Identifier(
        type='glottolog', name='{Language_ID}').url()
    ds.metadata['tableSchema']['columns'][3]['valueUrl'] = url_template(
        req, 'parameter', 'Parameter_ID')
    ds.metadata['tableSchema']['columns'][5]['datatype'] = 'anyURI'

    ds.metadata['dc:bibliographicCitation '] = text_citation(req, contrib)
    ds.metadata['dc:publisher'] = '%s, %s' % (
        req.dataset.publisher_name, req.dataset.publisher_place)
    ds.metadata['dc:license'] = req.dataset.license
    ds.metadata['dc:issued'] = req.dataset.published.isoformat()
    ds.metadata['dc:title'] = contrib.name
    ds.metadata['dc:creator'] = contrib.formatted_contributors()
    ds.metadata['dc:identifier'] = req.resource_url(contrib)
    ds.metadata['dc:isPartOf'] = req.resource_url(req.dataset)
    ds.metadata['dcat:accessURL'] = req.route_url('download')

    for vs in valuesets:
        refs, sources = format_refs(req, vs)
        ds.sources.add(*sources)
        row = [
            vs.id,
            vs.language.glottocode or req.resource_url(vs.language),
            vs.language.name,
            features[vs.parameter_pk].id,
            vs.values[0].domainelement.name,
            refs,
            vs.source or '',
        ]
        ds.add_row(row)
    ds.write(outdir)


def main(args):
    features = {
        p.pk: p for p in DBSession.query(Parameter).options(joinedload(Parameter.domain))}

    for contrib in DBSession.query(Contribution):
        valuesets = DBSession.query(ValueSet)\
            .join(Language)\
            .filter(ValueSet.contribution_pk == contrib.pk)\
            .order_by(Language.name)\
            .options(
                contains_eager(ValueSet.language),
                joinedload(ValueSet.values),
                joinedload_all(ValueSet.references, ValueSetReference.source))
        write_cldf(args.env['request'], contrib, valuesets, features, args.outdir)


if __name__ == '__main__':
    main(parsed_args((('outdir',), dict(action=ExistingDir)), bootstrap=True))
