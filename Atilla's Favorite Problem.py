#https://codeforces.com/problemset/problem/1760/B

# ord => a =  97
# ord => z =  122
out = [] # output list
ntest = int(input()) #number of test case
for i in range(ntest):
    size = int(input())
    str1 = str(input())
    #this equation to find the asce for the letter 
    x = 121 - ord(max(list(str1)))
    #limit the range of number 
    out.append(25 - x)

print(*out,sep="\n")
    






















