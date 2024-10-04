def make_alternate_pattern(given_str):

    count_dot = given_str.count('.')
    count_b = given_str.count('b')
    result_needed = "Alternate Form Is Not Possible !!"

    alternate_str = []
    alternate_str1 = []
    alternate_str2 = []
    result_needed = ""
    result_needed1 = ""
    result_needed2 = ""

    if count_b == 0 or count_dot == 0 or count_b > count_dot + 1:
        return result_needed, -1
    
    elif count_b == 1 and given_str[-1] != 'b' and given_str[-2] != 'b':
        return ('.'*count_dot+'b'), 2
    
    elif count_b == 1 and (given_str[-1] == 'b' or given_str[-2] == 'b'):
        return given_str, 0
    
    elif count_b == count_dot + 1:
        for _ in range(count_b-1):
            alternate_str.append('b.')
        alternate_str.append('b')
        result_needed1 += "".join(alternate_str)
        result_needed2 += "".join(alternate_str)

    elif count_b == count_dot:
        for _ in range(count_b):
            alternate_str1.append('b.')
        result_needed1 += "".join(alternate_str1)

        for _ in range(count_b):
            alternate_str2.append('.b')
        result_needed2 += "".join(alternate_str2)

    elif count_b < count_dot:
        front_dots1 = (['.'] * (count_dot-(count_b)))
        for _ in range(count_b):
            alternate_str1.append('b.')
        front_dots1.extend(alternate_str1)
        result_needed1 += "".join(front_dots1)

        front_dots2 = (['.'] * (count_dot - count_b))
        for _ in range(count_b):
            alternate_str2.append('.b')
        front_dots2.extend(alternate_str2)
        result_needed2 += "".join(front_dots2)

    def count_difference(given_str, result_needed1, result_needed2):
        shift_count1 = sum(1 for a, b in zip(given_str, result_needed1) if a != b)
        shift_count2 = sum(1 for c, d in zip(given_str, result_needed2) if c != d)
        if shift_count1 <= shift_count2:
            result_needed = result_needed1
            counts = shift_count1
        else:
            result_needed = result_needed2
            counts = shift_count2
        return result_needed, counts
    return count_difference(given_str, result_needed1, result_needed2)
your_input = input("\nEnter Your Input String   :    ")
your_input_clean = ''
for i in your_input:
    if i == '.' or i == 'b':
        your_input_clean+=i
final_pattern, counts = make_alternate_pattern(your_input_clean)
print(your_input_clean)
print(final_pattern)
print(counts)
print()