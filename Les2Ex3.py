#Решение через список
month = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
seasons = ["winter", "spring", "summer", "autumn"]
n = int(input("Enter the number of month: "))
for i in range(len(month)):
    if n in month[i]:
        print(f"The season is {seasons[i]}")
        break

#Решение через словарь
season = {12:"winter", 1:"winter", 2:"winter", 3:"spring", 4:"spring", 5:"spring", 6:"summer", 7:"summer", 8:"summer", 9:"autumn", 10:"autumn", 11:"autumn"}
n = int(input("Enter the number of month: "))
print(f"The season is {season.get(n)}")
