n = int(input("Enter seconds: "))
h = n // 3600
if h < 10:
    h = "0" + str(h)
n = n % 3600
m = n // 60
if m < 10:
    m = "0" + str(m)
s = n % 60
if s < 10:
    s = "0" + str(s)
print(f"The time is: {h} : {m} : {s}")