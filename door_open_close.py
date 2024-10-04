list1 = [0] * 10

for i in range(1,11):
    for j in range(i,11):
        if j % i == 0:
            if list1[j-1] == 0:
                list1[j-1] = 1
            elif list1[j-1] == 1:
                list1[j-1] = 0
    print(f"{i} --> {list1}")
print()
print(list1)
print()