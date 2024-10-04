def get_second_largest_element(input_list):
    largest = second_largest = 0
    for i in input_list:
        if largest < i:
            second_largest = largest
            largest = i
    return second_largest

input_list = []
second_largest = get_second_largest_element(input_list)
print(second_largest)
