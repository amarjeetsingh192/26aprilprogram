a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))
d=  int(input('Enter third number  : '))
l = 0

if a > b and a > c and a>d:
    l = a
if b > c and b > d:
    l = b
if c > d:
    l = c
else:
    l= d

print(l, "is the largest of three numbers.")