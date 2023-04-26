"""
5.square-2
write a program that reads a number M and print square of M rows and M columns using number

sample input
4

output
1111
2222
3333
4444
"""

M=int(input("enter a value :"))
for i in range(1,M+1):
   print(M*str(i))