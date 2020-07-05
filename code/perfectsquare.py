#to find the perfect square between two numbers N and # %% [markdown]
import math

M = int(input("Give me value of M: "))
N = int(input("Give me value of N: "))

if N > M:
    exit(1)
else:
    print("value of N is less than M.")
#if int(root + 0.5) ** 2 == number:
for x in range(N, M + 1):
    for y in range(N, M + 1):
        if(x/y>1 and  int((math.sqrt(x / y)) + 0.5) ** 2 == x / y):
            print(x, y, int(x / y))
