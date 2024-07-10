#https://codeforces.com/problemset/problem/1294/A

def equality(a,b,c,n):
    Max = max(a,b,c)
    #This equation is to find the values ​​you need to make the numbers equal
    temp = n - ((Max - a) + (Max - b) + (Max - c)) 
    if temp % 3 == 0 and temp >= 0:
        return True
    else :
        return False



ntest = int(input()) #number of test case
out = []
for i in range(ntest): # for get x test case
    a,b,c,n = map(int, input().split())
    if equality(a,b,c,n) :
        out.append("YES")
    else:
        out.append("NO")
        
print(*out , sep="\n")
