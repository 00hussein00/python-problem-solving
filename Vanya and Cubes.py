#https://codeforces.com/problemset/problem/492/A


def summation(x):
    return (x * (x+1)) // 2


num = int(input())
i = 1
while True:
    temp = num - summation(i)   
    if temp >= 0:
        num = temp
        i+=1
    else:
        i-=1
        break
    
    
    
print(i)























