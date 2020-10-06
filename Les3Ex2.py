def human(n, s, yb, c, e, p):
    """Выводит данные пользователя одной строкой."""
    print(f"User data: {s} {n}, {yb} year of birth, {c} city, Email: {e}, phone number: {p}")


print("Enter the user's details: ")
human(n=input("Name: "),
      s=input("Surname: "),
      yb=int(input("Year of birth: ")),
      c=input("City: "),
      e=input("Email: "),
      p=input("Phone number: "))
