"""

7.Right angled triangle
write a program that reads a number N and prints a right angled triangle of N rows using stars (*) and pluses(+)
input
4

output
*
* *
* * *
+ + + +
"""
n=int(input("enter a value :"))

for i in range(1,n):
    print(i*"* ")
print(n*"+ ")