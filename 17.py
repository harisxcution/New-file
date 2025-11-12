try:
    age = int(input("enter the age"))
    if age > 18:
        print("You are good to vote")
    else:
        print("You are not good to vote")
except ValueError:
    print("unvalid input")