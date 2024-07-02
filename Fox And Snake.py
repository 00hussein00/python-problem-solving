# -*- coding: utf-8 -*-

coul,row = map(int,input().split())

for i in range((coul // 2) +1):
    print("#" * row)
    #print(" i : " , i , " ((coul // 2) +1) : " , ((coul // 2) +1))
    if i % 2 == 0 and i != ((coul // 2)):      
        print(f"{'.'*(row - 1)}#")
    elif i % 2 == 1 and i != ((coul // 2)) :
        print(f"#{'.'*(row - 1)}") 

#print(f"coul : {coul} , row : {row}")
