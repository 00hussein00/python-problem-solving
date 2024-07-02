#https://codeforces.com/problemset/problem/339/A


nums = input().split("+")
cnums = nums.copy()  #copy

nums.sort()

#if (cnums.__eq__(nums)):
#    nums.sort(reverse = True)


print(*nums,sep="+")