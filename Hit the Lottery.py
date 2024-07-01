
#https://codeforces.com/problemset/problem/996/A
amount = int(input())
B = [1,5,10,20,100]
lenB = len(B) - 1
cBay = 0

while amount >0 and lenB >=0 :
    x = amount // B[lenB]
    
   # print("X : ",x)
    
    if x.__class__() == 0 and x !=0:
        amount -= B[lenB] * x
        cBay+= 1  * x
        #print("new amount " , amount , " - ", B[lenB] * x)

    else:
        lenB-=1
    
    #print("B: ",B[lenB])

 
print(cBay)
    

