def digit_sum(m):
    while m > 9:
        sum1 = 0
        for i in str(m):
            sum1 += int(i)
            m = sum1
    return sum1

m = int(input("Enter a number  :   "))
print(digit_sum(m))