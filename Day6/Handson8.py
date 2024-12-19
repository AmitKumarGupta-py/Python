import re
result = re.findall(r'^Start.*End$','Start of a line begin with the End')
"""regex = r'^The'
regex1 = r'dog$'
strings = ('The quick brown fox', 'jumps over', 'the lazy dog')
for string in strings:
    if re.match(regex, string) and  re.match(regex1,string):
        print(f'Matched: {string}')
    else:
        print(f'Not matched: {string}')"""
print(result)