#https://codeforces.com/problemset/problem/1950/A

ntest = int(input())#number of test case
out = []
for i in range(ntest) : 
    a,b,c = map(int, input().split())
    if a<b<c :
        out.append("STAIR")
    elif a<b>c :
        out.append("PEAK")
    else:
        out.append("NONE")
        
print(*out , sep= "\n")



