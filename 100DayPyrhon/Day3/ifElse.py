print("Welcome to the treasure hunt challenge")
print("You will go left or right?")
direction = input()
if direction.upper() == "LEFT" or direction.upper() == "RIGHT":
    if direction.upper() == "LEFT":
        print("You came at a river, and you need to cross him, would you swim or await for a boat")
        direction = input()
        if direction.upper() == "SWIM" or direction.upper() == "AWAIT":
            if direction.upper() == "SWIM":
                print("You crossed the river and see three doors, witch one you select(1, 2, 3)?")
                direction = input()
                if direction.upper() == "1":
                    print("Congrats, you won!")
                else:
                    print("You select a wrong door and die suddenly")
            else:
                print("You await, but the boat never came, you DIE!")
                exit()
    else:
        print("Wrong select, you die")
else:
    print("Wrong select, you die")



