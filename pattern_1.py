# 1 2 3 4 5
# 2 3 4 5 1
# 3 4 5 1 2
# 4 5 1 2 3
# 5 1 2 3 4

n = int(input("Enter number : "))   
for i in range(1,n+1):
    k = i
    for j in range(1,n+1):
        if k > n:
            k = k - n
        print(k,end=" ")
        k += 1
    print()