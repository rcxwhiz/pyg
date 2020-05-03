import re
from typing import List, Set

import Config as cfg

package_whitelist = ['numpy',
                     'matplotlib',
                     'scipy',
                     'math']

import_checker1 = re.compile(r'(from[ ]+[^ \n;]+[ ]+)?(import[ ]+)([^ \n;.]+)')
import_checker2 = re.compile(r'(from[ ]+)([^ \n;.]+)([ ]+import)')

# other things you might want to block are open and savetxt, etc.
phrase_blacklist = [re.compile(r'\\'),
                    re.compile(r'/')]

# built in functions that you want to disable ex. open
function_blacklist = ['open',
                      'input']


def security_check(source_code: str) -> List[str]:
    # will run the source code as a string through the security checkers and return a list of issues
    issues = []
    for issue in check_packages(source_code):
        issues.append(f'Illegal package imported: {issue}')
    for issue in check_phrases(source_code):
        issues.append(f'Contained illegal phrase: {issue}')
    num_lines = source_code.count('\n')
    if num_lines > cfg.max_student_code_lines:
        issues.append(f'Code was too long: {num_lines} lines')
    return issues


def check_packages(source_code: str) -> Set[str]:
    # use the regex to detect a set of the pakages imported
    bad_packages = set()

    for match in re.findall(import_checker1, source_code):
        if match[0] == '' and match[2] not in package_whitelist:
            bad_packages.add(match[2])
    for match in re.findall(import_checker2, source_code):
        if match[1] not in package_whitelist:
            bad_packages.add(match[1])

    return bad_packages


def check_phrases(source_code: str) -> Set[str]:
    # check for bad strings inside the source code
    bad_phrases = set()
    for phrase in phrase_blacklist:
        match = re.match(phrase, source_code)
        if match:
            bad_phrases.add(str(match))
    return bad_phrases
