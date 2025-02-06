print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
direction = input("You're at a cross road. Where do you want to go? Type left or right")

if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    decision = input("Type 'wait' to wait for the boat. Type 'swim' to swim across: ")
    if decision == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors")
        color = input("One red,one yellow and one blue. Which color do you choose")
        if color == "red":
            print("It's a room full of fire. Game over")
        elif color == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over")
