try:
    age=int(input("enter your age pls"))
    print(age)
except ValueError as e:
    print(e)