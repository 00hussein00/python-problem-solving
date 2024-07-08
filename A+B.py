#https://codeforces.com/problemset/problem/1772/A

out = [] # output list
ntest = int(input()) # number of test case
for i in range(ntest):
    x, y = map(int, input().split("+"))
    out.append(x+y)
print(*out,sep="\n")

