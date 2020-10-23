my_list = [2, 2.5, "string", True, [1, 2, 3], {1, 2, 3}, (1, 2, 3)]
print(f"Types of elements in {my_list} are: ")
for i in my_list:
    print(type(i), end=" ")