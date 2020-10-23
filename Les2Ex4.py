string = input("Enter a string of several words: ")
words = string.split()
for ind, el in enumerate(words):
    print(f"The word in the string is: {ind} - {el[0:10]}")