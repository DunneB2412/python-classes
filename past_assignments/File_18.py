q=input("Hello fellow adventurer! Imagine you are trapped in a cell with three exits. Please type left, right, or middle!")
if q=="left":
    print("You go through the left exit and find youself in a different dimension. I mean you got out now get back to earth quickly")
elif q=="middle":
    print("You open the middle door. In that moment a panther jumps straight on to you and tares you to pieces. Try again...")
elif q=="right":
    print("You open the right door and there are two other doors. Which one will you choose? Right or Left?")
    q=input("What door will you choose?")
    if q=="Right":
        print("After a while you come across two new doors. Are you going to choose RIGHT or LEFT?")
        q=input("LEFT or RIGHT?")
        if q=="LEFT":
            print("You made it! You open the door and find yourself on the surface. Good job!")
        elif q=="RIGHT":
            print("You fool you were so close to victory but failed!!!")
    elif q=="Left":
            print("I am very sorry but you just got teleported into outer space try again!")
