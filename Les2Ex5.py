rating = [7, 5, 3, 3, 2]
print("There is a rating: ", rating)
n = int(input("Add a new item to the rating (natural number): "))
rating.append(0)
for i in range(len(rating)):
    if n > rating[i]:
        rating.insert(i, n)
        rating.remove(0)
        print(rating)
        break
