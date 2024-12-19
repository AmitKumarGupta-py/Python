import re
line1 = "Note Apple pie is delicious! under the bed, there is A CAT!"
#result = re.match(r'^[Note].*[!]$',line1)
result = re.match(r'^Note.*!$',line1)
print(result)

## aNSWER  r'^Note.*!$'