print("Welcome to Python roller coster")
height = input("Is your height is greater then 120m, pls enter y/n : ")
cost = 0
if height == 'y':
    age = int(input("Enter your age : "))
    
    if age < 12:
        cost += 10
        print(f"The ticket cost will be ${cost}.")
        print("You can also buy food ,\n what you want \nString cheese.= $30 press 1\nDried fruit = $40 press 2\nDried soda = $50 press 3")
        sanck = input("1,2,3 : ")
        if sanck == '1':
            s_cost=30
            stock = int(input("How much String cheese do you want : "))
            s_cost *= stock
            print(f"The snack cost will be ${s_cost}")
            print(f"The total amount : ${cost+s_cost}")
        elif sanck == '2':
            s_cost=40
            stock = int(input("How much String cheese do you want : "))
            s_cost *= stock
            print(f"The snack cost will be ${s_cost}")
            print(f"The total amount : ${cost+s_cost}")
        elif sanck == '3':
            s_cost=50
            stock = int(input("How much String cheese do you want : "))
            s_cost *= stock
            print(f"The snack cost will be ${s_cost}")
            print(f"The total amount : ${cost+s_cost}")
        else:
            print("Error")
    elif age >=12 and age <=18:
        cost += 15
        print(f"The ticket cost will be ${cost}.")
        print("You can also buy food ,\n what you want \nString cheese.= $30 press 1\nDried fruit = $40 press 2\nDried soda = $50 press 3")
        sanck = input("1,2,3 : ")
        if sanck == '1':
            s_cost=30
            stock = int(input("How much String cheese do you want : "))
            s_cost *= stock
            print(f"The snack cost will be ${s_cost}")
            print(f"The total amount : ${cost+s_cost}")
        elif sanck == '2':
            s_cost=40
            stock = int(input("How much String cheese do you want : "))
            s_cost *= stock
            print(f"The snack cost will be ${s_cost}")
            print(f"The total amount : ${cost+s_cost}")
        elif sanck == '3':
            s_cost=50
            stock = int(input("How much String cheese do you want : "))
            s_cost *= stock
            print(f"The snack cost will be ${s_cost}")
            print(f"The total amount : ${cost+s_cost}")
        else:
            print("Error")
    elif 24 >age >18 or age ==  25:
        cost += 25
        print(f"The ticket cost will be ${cost}.")
        print("You can also buy food ,\n what you want \nString cheese.= $30 press 1\nDried fruit = $40 press 2\nDried soda = $50 press 3")
        sanck = input("1,2,3 : ")
        if sanck == '1':
            s_cost=30
            stock = int(input("How much String cheese do you want : "))
            s_cost *= stock
            print(f"The snack cost will be ${s_cost}")
            print(f"The total amount : ${cost+s_cost}")
        elif sanck == '2':
            s_cost=40
            stock = int(input("How much String cheese do you want : "))
            s_cost *= stock
            print(f"The snack cost will be ${s_cost}")
            print(f"The total amount : ${cost+s_cost}")
        elif sanck == '3':
            s_cost=50
            stock = int(input("How much String cheese do you want : "))
            s_cost *= stock
            print(f"The snack cost will be ${s_cost}")
            print(f"The total amount : ${cost+s_cost}")
        else:
            print("Error")
    else:
        print("Try to enter age in range of 12 - 25")
else:
    print("Sorry, you can't rider is coster \nGrow bigger next time !!!!")

