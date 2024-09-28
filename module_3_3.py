def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


print_params()
print_params(5)
print_params(9,'5')
print_params(1, '6mn5', False)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [5, 'k86h', 0.6]
values_dict = {'a': 7, 'b': 'str', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['jpf', 6585]

print_params(*values_list_2, 42)