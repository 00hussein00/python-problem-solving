#https://codeforces.com/problemset/problem/1985/A

def swap(A,B) -> str: #swap the 1st element
    A = list(A)
    B = list(B)
    temp = B[0]
    B[0] = A[0]
    A[0] = temp
    A = ''.join(A)
    B = ''.join(B)
    return A,B

def Print(A): # print with format 
    c = 0    
    while c < len(A):
        print(A[c],A[c+1])
        c+=2
        
ntest = int(input())
out = []
for i in range(ntest):
    str1,str2 = map(str,input().split())
    str1,str2 = swap(str1,str2)
    out.append(str1)
    out.append(str2)
    
      
Print(out)

