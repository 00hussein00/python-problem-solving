#https://codeforces.com/problemset/problem/41/A

t = str(input())
s = str(input())
if(t == s[::-1]):
    print("YES")
else:
    print("NO")