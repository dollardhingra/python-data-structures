def add(a, b):
    print(locals()) # {'a': 1, 'b': 2}
    return a+b


add(1,2)
