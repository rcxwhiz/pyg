import re


def find_parts(out_files):
    part_re = re.compile(r'([P|p][A|a][R|r][T|t][ ]*[:]?[-]*[ ]*)([a-zA-Z]|[0-9]+)')
    found_parts = []
    hits = re.findall(part_re, open(out_files[0], 'rt', encoding='utf-8').read())
    for hit in hits:
        found_parts.append([hit[0], hit[1]])
    return found_parts
