def get_continue_odds(list_input):
    for i in range(len(list_input)-2):
        if list_input[i] % 2 == 1 and list_input[i+1] % 2 == 1 and list_input[i+2] % 2 == 1:
            return list_input[i], list_input[i+1], list_input[i+2]

given_input = [2,3,4,5,4,3,9,7,6,7,9,8]
print(get_continue_odds(given_input))