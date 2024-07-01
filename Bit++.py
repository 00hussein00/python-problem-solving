#https://codeforces.com/problemset/problem/282/A
total = 0

for i in range(int(input())):# # check number of operation 
    x = input().lower()
    if x == "x++" or x== "++x":
        total+=1
        
    elif x == "--x" or x == "x--":
        total-=1
    
    else:
        continue
    
    

    
    
print(total)
