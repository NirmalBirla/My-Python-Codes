
def check(input_str,open,close):
    temp_str = ''
    for i in input_str:
        if len(temp_str) == 0  and i in close:
            return False
        elif i in open:
            temp_str+=i
        elif (i == "]" and temp_str[-1] != "["):
            return False
        elif (i == ")" and temp_str[-1] != "("):
            return False
        elif (i == "}" and temp_str[-1] != "{"):
            return False
        else:
            temp_str = temp_str[:-1]
            print("Temp_string",temp_str)
    if len(temp_str) == 0:
        return True
         
input_string = input("Enter your testcase :   ")
open = "[({"
close = "]})"

print(check(input_string,open,close))


