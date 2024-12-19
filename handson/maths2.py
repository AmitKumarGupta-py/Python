from idlelib.colorizer import prog_group_name_to_tag

from sympy import diff,pprint
from sympy.abc import x

from maths1 import expression

expression = x**2

result = diff(expression,x)
print("Derivative of ")
pprint(expression)