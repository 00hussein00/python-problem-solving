#https://codeforces.com/problemset/problem/617/A

step = int(input()) # number of step 
foot = 5 # movment step
c = 0 # count number of movment 
while step > 0 and foot > 0:
    temp = step - foot
    if temp >= 0:
        c+=1
        step = temp
        #print("c : ",c , "foot : " , foot)
    elif temp < 0 :
        foot -=1

    #print("t : ",temp ," f : " , foot , " s : ", step)
    
print(c)
        
    