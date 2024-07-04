#https://codeforces.com/problemset/problem/9/A

import math

L = {1:1,2:2,3:3,4:4,5:5,6:6}
out = []
def Roll(x): 
    while x <= len(L):
        out.append(L[x])
        x+=1
    

Roll(max(map(int,input().split())))
z = math.gcd(len(out), 6) 
print(f"{len(out)//z}/{6//z}")

