x = { 'apple': 1, 'banana': 2 }
y = { 'banana': 10, 'pear': 11 }
for k, v in y.items():
    if k in x.keys():
        x[k] += v
    else:
        x[k] = v