a = float(input("Enter the result of the first day: "))
b = float(input("Enter the planned result: "))
d = 1
while a < b:
    a = a + 0.1 * a
    d = d + 1
print(d)
