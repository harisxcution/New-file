a = int(input("Enter a number: "))
i = 0
while i <= a:
    if i % 2 == 0:
        print("Even", i)
    else:
        print("Odd", i)
    i += 1