import array

arr = array.array("i", (1,2,3,4,5)) # b, B, u, h, H, i, I, l, L, q, Q, f or d

# https://docs.python.org/3/library/array.html

memory_arr1 = []

for element in arr:
    memory_arr1.append(id(element))

print(memory_arr1)

print(memory_arr1[1] - memory_arr1[0])
print(memory_arr1[2] - memory_arr1[1])
print(memory_arr1[3] - memory_arr1[2])
print(memory_arr1[4] - memory_arr1[3])