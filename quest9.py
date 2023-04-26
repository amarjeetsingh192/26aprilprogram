"""
9.rectangle -3
write a program that reads two numbers M and N and prints a rectangle m rows and N columns using number

input:
2
3
output:
1 1 1
2 2 2
"""

M=int(input("enter a row value :"))
N=int(input("enter a coloum values :"))

for i in range(1,M+1):
    for j in range (1,N+1):
      print(i,end="")
    print()