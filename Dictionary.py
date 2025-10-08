def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

data = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3}
print(sort_dict_by_value(data))
# Output: {'banana': 2, 'date': 3, 'apple': 5, 'cherry': 8}
