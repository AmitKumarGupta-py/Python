from django.db.models.expressions import result
from sympy import limit,sqrt,pprint
from sympy.abc import x
expression = (x - 2)/(x**2 + x -6)
result=limit(expression,x,2)

print("Limit of ")

pprint(expression)

print("at x=2 is ",result)