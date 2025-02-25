def sum_one_to_n(number):
    s1 = ''
    summ = 0

    for i in range(1, num+1):
        s1 += str(i) if len(s1) < 1 else ("+" + str(i))
        summ += i
        print(s1, "=", summ)

num = int(input("Enter a number : "))
sum_one_to_n(num)


# def sum_one_to_n(num, s1, summ, start = 1):
#     if start == 1:
#         print("1 = 1")
#     else:
#         s1 += ("+" + str(num))
#         summ += num
#         print(f"{s1} = {summ}")
#         start += 1
#         return sum_one_to_n(num,s1,summ, start)

# s1 = ''
# summ = 0
# num = int(input("Enter a number : "))
# print(sum_one_to_n(num, s1, summ))