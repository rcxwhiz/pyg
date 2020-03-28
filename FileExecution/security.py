import re

package_whitelist = ['numpy',
                     'matplotlib',
                     'scipy']
phrase_blacklist = ['input(',
                    'input (']
import_checker1 = re.compile(r'(from[ ]+[^ \n;]+[ ]+)?(import[ ]+)([^ \n;.]+)')
import_checker2 = re.compile(r'(from[ ]+)([^ \n;.]+)([ ]+import)')


def security_check(source_code):
    # will run the source code as a string through the security checkers and return a list of issues
    issues = []
    for issue in check_packages(source_code):
        issues.append(f'Illegal package imported: {issue}')
    for issue in check_phrases(source_code):
        issues.append(f'Contained illegal phrase: {issue}')
    return issues


def check_packages(source_code):
    # use the regex to detect a set of the pakages imported
    bad_packages = set()

    for match in re.findall(import_checker1, source_code):
        if match[0] == '' and match[2] not in package_whitelist:
            bad_packages.add(match[2])
    for match in re.findall(import_checker2, source_code):
        if match[1] not in package_whitelist:
            bad_packages.add(match[1])

    return bad_packages


def check_phrases(source_code):
    # check for bas strings inside the source code
    bad_phrases = set()
    for phrase in phrase_blacklist:
        if phrase in source_code:
            bad_phrases.add(phrase)
    return bad_phrases
