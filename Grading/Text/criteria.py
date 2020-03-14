import re


def find_parts(out_files):
    part_re = re.compile(r'([P|p][A|a][R|r][T|t][ ]*[:]?[-]*[ ]*)([a-zA-Z]|[0-9]+)')
    found_parts = {}
    for file in out_files:
        hits = re.findall(part_re, open(file, 'rt', encoding='utf-8').read())[:][1]
        found_parts[file] = zip(hits)
    print(found_parts)
