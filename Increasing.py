#https://codeforces.com/problemset/problem/1742/B

def checkRepeatNumbers(A , sA ) -> bool: #checking for repeating number 
    i = 0
    while i < sA -1 :
        if  A[i] != A[i+1]:
            i+=1
        else:
            return True       
    return False


ntest = int(input()) # number of test case
out = []
for i in range(ntest):
    sizet =int(input()) # size of each test case
    lt = list(map(int, input().split())) #list for test case
    scit = lt.copy() # sorted copy from list
    scit.sort()
    if not(checkRepeatNumbers(scit , sizet)) and min(scit) == scit[0] and max(scit) == scit[-1]:
        out.append("YES")
    else:
        out.append("NO")
        
print(*out,sep="\n")





























