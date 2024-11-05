def longest_alternate_pattern(inputt):
    if not inputt:
        return ""

    ans = inputt[0]
    temp = inputt[0]
    for i, j in zip(inputt , inputt[1:]):
        # breakpoint()
        if i == j:
            if len(ans) < len(temp):
                ans = temp
                temp = j
            else: 
                ans = ans
        else:
            temp += j
    else:
        if len(ans) < len(temp):
                ans = temp
                temp = j

    return f"Longest ulternate pattern is  : {ans}"

inputt = input("Enter a pattern (It should contain only 0's and 1's) :  ")
print(longest_alternate_pattern(inputt))