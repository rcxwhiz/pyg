import re


def find_parts(out_files):
    part_re = re.compile(r'([P|p][A|a][R|r][T|t][ ]*[:]?[-]*[ ]*)([a-zA-Z]|[0-9]+)')
    found_parts = []
    import os
    print(os.path.isfile(out_files[0]))
    print(out_files[0])
    # TODO for some reason it literally won't let me read files like this if I run from a batch file
    with open(out_files[0], 'r') as file:
        print(file.read())
        print(file.tell())
    hits = re.findall(part_re, open(out_files[0], 'r', encoding='utf-8').read())
    for hit in hits:
        found_parts.append([hit[0], hit[1]])
    return found_parts
