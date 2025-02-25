inp = "['abc', 'xyz']"

temp = inp[1:-1]
temp1 = temp.replace("'", '')
temp2 = temp1.split(', ')

print(temp2)
print(len(temp2))