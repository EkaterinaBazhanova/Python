string = input("Enter list items using the space bar: ")
list = string.split()
n = len(list)
print(f"Your list is: {list}")
i = 0
while i < n - 1:
    list[i], list[i+1] = list[i+1], list[i]
    i = i + 2
print(list)
