n = int(input("Enter an positive integer"))
r = n % 10
while n // 10 > 0:
    n = n // 10
    if n % 10 > r:
        r = n % 10
print("The maximal digit in the number is: ", r)