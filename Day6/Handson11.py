import re
"""string1 = ("assembl ehe orld for the inal EsistanC towards IhK coming era and step in to the new world").split()
""""('assemble the world', 'for the final resistance','towards the coming','era and step','in to the','new world')""""
result = re.match(r'\b[aeouiAEOUI]\w*[bcdfghjklmnpqrstvwxzyzBCDFGHJKLMNPQRSTVWXYZ]\b',string1)
print(result)"""
#string2 = ("11,1a,22,22b,33,3c,44,4d")
result1 = re.match(r'[d]+[^/d]',string2)
print(result1)