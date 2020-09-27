r = int(input("Enter the revenue value of the company: "))
c = int(input("Enter the value costs of the company: "))
if r >= c:
    p = r - c
    ren = p / r
    print("The financial result is profit ", p)
    print("The profitability is ", ren)
    e = int(input("Enter the number of employees of the company: "))
    print("Firm's profit per employee", p / e)
else:
    print("The financial result is loss")