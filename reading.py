x1 = int(input('x1'))
x2 = int(input('x2'))
x3 = input('x1+x2')
if x3 == '+':
    x3 = x1+x2
elif x3 == '-':
    x3 = x1-x2
elif x3 == '*':
    x3 = x1*x2
elif x3 == '/':
    x3 = x1/x2
print(x3)
