arr1 = [0, 1, 2, 3, 4, 5]
memory_arr1 = []

for element in arr1:
    memory_arr1.append(id(element))

print(memory_arr1)

print(memory_arr1[1] - memory_arr1[0])
print(memory_arr1[2] - memory_arr1[1])
print(memory_arr1[3] - memory_arr1[2])
print(memory_arr1[4] - memory_arr1[3])


def some_func():
    return "a func"


arr2 = [
    1,
    "one",
    (
        "a",
        "tuple",
    ),
    ["nested", "list"],
    some_func,
]

print(arr2)
