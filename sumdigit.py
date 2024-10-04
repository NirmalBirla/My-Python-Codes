m = int(input("Enter a number  :   "))

while m > 9:
    sum1 = 0
    for i in str(m):
        sum1 += int(i)
        m = sum1
print(m)
