#https://codeforces.com/problemset/problem/1873/A

def diff(A) -> bool:
    c  = 0
    B = A.copy()
    B.sort()
    for i in range(3):
        if A[i] == B[i]:
            continue
        else:
            c+=1
    if c == 2 or c == 0:
        return True
    else:
        return False
    
        
        
ntest = int(input()) # number of test case
A = [] # output list 
for i in range(ntest):
    x = list(str(input()))
    if diff(x) : 
        A.append("YES")
    else :
        A.append("NO")
    


print(*A,sep="\n" )






