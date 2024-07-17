#https://codeforces.com/problemset/problem/584/A





def oAndR (x,y)-> int : # Olesya and rodion
    for i in range(10):
        r = "1" + "0" * int(x-2) + str(i) # format for result
        if int (r) % y ==  0 and len(r) == x: 
            return(r)
        elif len(r) > x and len(str(y)) == x:
            return y
    return -1

        
    

a,b = map(int, input().split())
    
print(oAndR(a,b))