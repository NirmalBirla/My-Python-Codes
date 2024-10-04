dict1 = {
    'A': [1, 2, 3, 4],
    'B': [2, 3, 4],
    'C': [3, 4, 5],
    'D': [2, 7]
}
dict2 = {}
for key1, val1 in dict1.items():
    for val2 in val1:
        if val2 not in dict2:
            dict2[val2] = []
        dict2[val2].append(key1)
print(dict2)