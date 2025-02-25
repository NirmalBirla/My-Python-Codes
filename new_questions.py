# inputt = '001101'

# 0 - False
# 1 - False
# 2 - True
# 3 - True
# 4 - False
# 5 - True

inputt = input("Enter a pattern (It should contain only 0's and 1's) :  ")
for i in enumerate(inputt):
    print(i[0], bool(int(i[1])))