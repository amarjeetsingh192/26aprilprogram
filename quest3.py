"""
3.sum of Numbers from M to N using for loop
given two integers M and N write a program to print thr sum of the numbers from M to N

sample input
2
6

output
20
"""
M=int(input("enter a value :"))
N=int(input("enter a value :"))
sum=0
for i in range(M,N+1):
    sum+=i
print(sum)


