print("Welcome to Python roller coster")
height = input("Is your height is greater then 120m, pls enter y/n : ")
cost = 0
if height == 'y':
    age = int(input("Enter your age : "))
    
    if age < 12:
        cost += 10
        print(f"The ticket cost will be ${cost}.")
    elif age >=12 and age <=18:
        cost += 15
        print(f"The ticket cost will be ${cost}.")
    elif 24 >age >18 or age ==  25:
        cost += 25
        print(f"The ticket cost will be ${cost}.")

    else:
        print("Try to enter age in range of 12 - 25")
    
else:
    print("Sorry, you can't rider is coster \nGrow bigger next time !!!!")