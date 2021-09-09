arr1 = (0, 1, 2, 3, 4, 5)


memory_arr1 = tuple(id(element) for element in arr1)

print(memory_arr1)

print(memory_arr1[1] - memory_arr1[0])
print(memory_arr1[2] - memory_arr1[1])
print(memory_arr1[3] - memory_arr1[2])
print(memory_arr1[4] - memory_arr1[3])


def some_func():
    return "a func"


arr2 = (
    1,
    "one",
    (
        "nested",
        "tuple",
    ),
    ["a", "list"],
    some_func,
)

# arr2[1] = "changed value"
# del arr2[0]

# print(arr2)
#
# arr3 = ('some_string',) + arr2
# print(arr3)
#
#
# del arr2
