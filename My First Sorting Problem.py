#https://codeforces.com/problemset/problem/1971/A



# print with format 
def printF(A):
    for i in A:
         print(" ".join(map(str, i)))
    
out = [] #output list 
ntest = int(input()) # number of test case 

for i in range(ntest):
    x,y = map(int, input().split()) 
    out.append([min(x,y),max(x,y)])

printF(out)