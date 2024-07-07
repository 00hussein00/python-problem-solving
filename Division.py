# https://codeforces.com/problemset/problem/1669/A

# just find the Division
ntest = int(input()) # number of test case
out = [] # output lest
for i in range(ntest):
    z = int(input())
    if z <= 1399 :
        out.append("Division 4")
    elif 1400 <= z <= 1599:
        out.append("Division 3")
    elif 1600 <= z <= 1899:
        out.append("Division 2")
    else:
        out.append("Division 1")
        
print(*out ,sep = "\n")

















