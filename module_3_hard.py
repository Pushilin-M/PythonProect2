data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    s = 0
    for n in data_structure:
        if isinstance(n, int or float):
             s += n
        elif isinstance(n, str):
            s += len(n)
        elif isinstance(n, dict):
            m = list(n.items())
            for i in m:
                data_structure.append(i)
        else:
            for j in n:
                data_structure.append(j)
    return s


result = calculate_structure_sum(data_structure)
print(result)

