from operator import truediv


loop = True

while loop:
    print("Dice Roll Simulator Menu")
    print("\n1: Roll Dice Once")
    print("2: Roll Dice 5 Times")
    print("3: Roll Dice 'n' times")
    print("4: Roll Dice until Snake eye")
    print("5: exit")
    selection  = input("enter Selection (1-5): ")
    import random
    if selection =="1": 
        #Stop the loop
        loop = False
        #process of choosing the value of both dice
        dice1 = random.randrange(1,7)
        dice2 = random.randrange(1,7)
        #adding them together
        sum = dice1 + dice2
        #output
        print(str(dice1) +"," + str(dice2) + " " + "(" + "sum: "  + str(sum) + ")")


    elif selection == "2":
        loop = False

        n = 1
        while n<=5:
            dice1 = random.randrange(1,7)
            dice2 = random.randrange(1,7)
            sum = dice1 + dice2
            print(str(dice1) +"," + str(dice2) + " " + "(" + "sum: "  + str(sum) + ")")
            n +=1


    elif selection =="3":
        loop = False
        rolls = float(input("\nHow many Rolls would you like?  "))
        n=1
        while n <= rolls:
            dice1 = random.randrange(1,7)
            dice2 = random.randrange(1,7)
            sum = dice1 + dice2
            print(str(dice1) +"," + str(dice2) + " " + "(" + "sum: "  + str(sum) + ")")
            n +=1


    elif selection =="4":
        loop = False
        snakeloop = True
        count = 0

        while snakeloop:
            dice1 = random.randrange(1,7)
            dice2 = random.randrange(1,7)
            sum = float(dice1 + dice2)
            print(str(dice1) +"," + str(dice2) + " " + "(" + "sum: "  + str(sum) + ")")
            count = count + 1
            if sum ==2:
                snakeloop = False
                print("SNAKE EYES!! It took " + str(count) + " to get snake eye.")


               
    elif selection =="5":
        print("\nEXIT")
        loop = False
