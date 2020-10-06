def my_func(x=0):
    s = input("Enter a string of numbers separated by a space: ")
    l = s.split()
    if ord(l[len(l) - 1]) != 113:
        for i in range(len(l)):
            l[i] = int(l[i])
        s_1 = sum(l)
        s_2 = x + s_1
        print(f"The sum is {s_1} ({s_2})")
        my_func(x=s_2)
    else:
        m = len(l)-1
        l.pop(m)
        n = len(l)
        for i in range(len(l)):
            l[i] = int(l[i])
        s_1 = sum(l)
        s_2 = x + s_1
        print(f"The sum is {s_1} ({s_2})")
        return


print("Attention! if you want to end the program, enter 'q' at the end of the line")
my_func()
