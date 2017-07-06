from clldutils.csvw.metadata import TableGroup
from tabulate import tabulate
from collections import defaultdict

def split_segments(segments, sep="+"):
    """Function splits list of segments by separator"""
    out = []
    start = True
    for char in segments:
        if start:
            out += [[]]

        if char == sep:
            start = True
        else:
            start = False
            out[-1] += [char]
    return out


def validate_morphemes(item):
    """Simple function illustrating validation of morphemes"""
    morpheme_length = len(item['Morphemes'])
    for key in ['Segments', 'Alignments']:
        if not morpheme_length <= len(split_segments(item[key])):
            return False
    if not morpheme_length <= len(item['Cognate_Sets']):
        return False
    return True


def validate_alignments(item, base_chars='()-'):
    """Simple validator for alignments

    Note
    ----
    Make sure an alignment is not longer than its segments.
    """
    for alm in ['Alignments', 'Alignment']:
        derived_alignment = [x for x in item[alm] if x not in '()-']
        if len(derived_alignment) != len(item['Segments']):
            return False
    return True


def validate_structure(item):
    if len(item['Prosodic_Structure']) != len(item['Segments']):
        return False
    return True


def validate_cognate_and_alignment(table):
    """check if all alignments are of the same length"""
    etd = defaultdict(list)
    data = {}
    errors = []
    for item in table:
        data[item['ID']] = item
        etd[item['Cognate_Set']] += [item['ID']]
    for key, values in etd.items():
        alignments = [len(data[value]['Alignment']) for value in values]
        if len(set(alignments)) != 1:
            errors += [key]
    return errors


def validate_cognates_and_alignments(table):
    """check if all partial alignments are of same length"""
    errors = []
    data = {}
    etd = defaultdict(list)
    for item in table:
        data[item['ID']] = item
        for cog in item['Cognate_Sets']:
            etd[cog] += [item['ID']]
    for key, values in etd.items():
        try:
            alignments = [len(
                split_segments(data[value]['Alignment'])[data[value]['Cognate_Sets'].index(key)]
                ) for value in values]
            if len(set(alignments)) != 1:
                errors += [key]
        except IndexError:
            errors += [key]
    return errors


if __name__ == '__main__':

    tg = TableGroup.from_file('example.tsv-metadata.json')
    problems = []
    count = 1
    for item in tg.tables[0]:
        morphemes = validate_morphemes(item)
        alms = validate_alignments(item)
        struc = validate_structure(item)
        if not morphemes:
            problems += [[
                count,
                'morphemes',
                str(item['ID']), 
                item['Language'], 
                item['Concept'], 
                ' '.join(item['Segments']),
                ' '.join(item['Morphemes'])
                ]]
            count += 1
        if not struc:
            problems += [[
                count,
                'structure',
                str(item['ID']), 
                item['Language'], 
                item['Concept'], 
                ' '.join(item['Segments']),
                ' '.join(item['Prosodic_Structure'])
                ]]
            count += 1
        if not alms:
            problems += [[
                count,
                'alignment',
                str(item['ID']), 
                item['Language'], 
                item['Concept'], 
                ' '.join(item['Segments']),
                ' '.join(item['Alignment'])+' / '+' '.join(item['Alignments'])
                ]]
            count += 1
    

    print(
            tabulate(problems, ['NUMBER', 'ERROR', 'WORD_ID', 'LANGUAGE', 'CONCEPT',
                'SEGMENTS', 'PROBLEM'], tablefmt='markdown')
            )

    errors = validate_cognate_and_alignment(tg.tables[0])
    print(errors)
    perrors = validate_cognates_and_alignments(tg.tables[0])
    print(perrors)

