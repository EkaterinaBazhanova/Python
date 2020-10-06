def int_func(y="text"):
    """Делает прописной первую букву слова, состоящего из маленьких латинских букв."""
    l = list(y)
    m = len(l) - 1
    i = 0
    while i <= m:
        if ((ord(l[i]) >= 1040) & (ord(l[i]) <= 1103)) or ((ord(l[i]) >= 65) & (ord(l[i]) <= 90)):
            print("Error: The word must include only lowercase Latin letters!")
            return
        else:
            i = i + 1
    return y.capitalize()


mw = input("Еnter a string of words consisting of small Latin letters: ")
s = mw.split()
for j in range(len(s)):
    s[j] = int_func(s[j])
result = " ".join(s)
print(f"Result: {result}")
