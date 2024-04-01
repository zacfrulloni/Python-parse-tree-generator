import pprint
import numpy

derivations= [
    ['S'],
    ['X', 'U'],
    ['a', 'U'],
    ['a', 'T', 'Y'],
    ['a', 'X', 'Y', 'Y'],
    ['a', 'a', 'Y', 'Y'],
    ['a', 'a', 'b', 'Y'],
    ['a', 'a', 'b', 'b']
]

# get max length of largest list in derivations variable
max_length = max(len(l) for l in derivations)

# create vertical lists
vertical_lists = []
for i in range(max_length):
    vertical_lists.append([l[i] if i < len(l) else None for l in derivations])

# we get the following:
[
    ['S', 'X', 'a', 'a', 'a', 'a', 'a', 'a'], 
    [None, 'U', 'U', 'T', 'X', 'a', 'a', 'a'], 
    [None, None, None, 'Y', 'Y', 'Y', 'b', 'b'], 
    [None, None, None, None, 'Y', 'Y', 'Y', 'b']
]

cleaned_lists = []

for l in vertical_lists:
    cleaned_list = [l[0]]
    for i in range(1, len(l)):
        if l[i] != l[i - 1]:
            cleaned_list.append(l[i])
        else:
            cleaned_list.append(None)
    cleaned_lists.append(cleaned_list)

converted_list = [
    ['S', 'X', 'a', None, None, None, None, None],
    [None, 'U', None, 'T', 'X', 'a', None, None],
    [None, None, None, 'Y', None, None, 'b', None],
    [None, None, None, None, 'Y', None, None, 'b']
]
# now if there are 'None' values after the first non None value in the list remove it and move all values to the left
for list in converted_list:

    index = next((i for i, value in enumerate(list) if value is not None), None)

    if index is not None:
        # Remove subsequent None values
        list = list[:index+1] + [value for value in list[index+1:] if value is not None]

    print(list)

# rotate the list and convert to tuples
parse_tree = list(zip(*converted_list[::1]))

# remove None values to clean up list:
parse_tree = [[val if val is not None else '' for val in row] for row in parse_tree]

# remove empty string values if 
# rotate the list and we get the following
pprint.pprint(parse_tree)
