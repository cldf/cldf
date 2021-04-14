"""
Update the CLDF website
"""
import re
import pathlib

from markdown import markdown

INDEX_TEMPLATE = """\
<html>
    <head>
        <title>CLDF {0}</title>
        <link rel="stylesheet" 
              href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" 
              integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" 
              crossorigin="anonymous">
        <link rel="stylesheet" 
              href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" 
              integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" 
              crossorigin="anonymous">
        <meta name="viewport" content="width=device-width">
    </head>
    <body>
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-12">
                    <h1>CLDF {0}</h1>
                    {1}
                </div>
            </div>
        </div>
    </body>
</html>"""


def iter_changes():
    section_pattern = re.compile(r'## \[(?P<version>[^]]+)]')
    agg, version = [], None
    print(pathlib.Path(__file__).parent.parent.resolve())
    for line in pathlib.Path(__file__).parent.parent.resolve().joinpath('CHANGELOG.md').read_text(
            encoding='utf8').splitlines():
        m = section_pattern.match(line)
        if m:
            if version:
                yield version, '\n'.join(agg)
            version, agg = m.group('version'), []
        elif version:
            agg.append(line)
    yield version, '\n'.join(agg)


def main(p):
    assert p.exists() and p.is_dir() and p.joinpath('v1.0').exists()

    for v, text in iter_changes():
        if v != 'Unreleased':
            d = p.joinpath(v)
            assert not d.exists(), 'Directory {}/ exists already!'.format(d)
            d.mkdir()
            d.joinpath('index.html').write_text(
                INDEX_TEMPLATE.format(v, markdown(text)),
                encoding='utf8')
            break


if __name__ == '__main__':
    import sys
    main(pathlib.Path(sys.argv[1]))
