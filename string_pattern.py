def string_pattern(str_input):
    ans = ""
    c = ""
    for i in str_input:
        try:
            a = int(i)
        except ValueError:
            c = c + i
        else:
            ans += c * a
            c = ""
    return ans

given_str = input("Enter a string (For Example: a2b3nirmal5$%2) : ") #'aabbbnirmalnirmalnirmalnirmalnirmal$%$%'

print(f"The output is : {string_pattern(given_str)}")