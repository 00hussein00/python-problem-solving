#https://codeforces.com/problemset/problem/1829/A


rcf = "codeforces" # real code-forces
out = []
nc = int(input()) # number of case
for i in range(nc):
    test = str(input()) # test case
    c = 0 # counter
    for j in range(len(rcf)):
        try:
            if rcf[j] == test[j]:
                continue
            else:
                c+=1
                
        except Exception:
            c = len(rcf) - len(test)
            
        
    out.append(c)

print(*out ,sep="\n")