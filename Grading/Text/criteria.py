import re


def find_parts(out_files):
    part_re = re.compile(r'([P|p][A|a][R|r][T|t][ ]*[:]?[-]*[ ]*)([a-zA-Z]|[0-9]+)')
    found_parts = {}
    for file in out_files:
        hits = re.findall(part_re, open(file, 'rt', encoding='utf-8').read())[:][1]
        found_parts[file] = list(zip(hits))
        for item in range(len(found_parts[file])):
            found_parts[file][item] = found_parts[file][item][0]
    return found_parts
