from addition import add
from subtraction import sub
from multiplication import mul
from division import div

a = int(input('Enter 1st no: '))
op = input('Enter +, -,*, / : ')
b = int(input('Enter 2nd no: '))

if op == '+':
    print('Addition:', add(a, b))
elif op == '-':
    print('Subtraction:', sub(a, b))
elif op == '*':
    print('Multiplication:', mul(a, b))
elif op == '/':
    print('Division:', div(a, b))
else:
    print('Invalid operation')
