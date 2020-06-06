import random
print("You are in front if dragon.")
print("1. In front of you, you see two caves.")
print("2.In one cave, the dragon is friendly and will share treasure with you.")
print("The other one dragon is greedy and hungry, and will eat you on sight.")

print("which cave will you go into? (1 or 2)")

number = int(input())
number_of_choice = random.randint(1, 2)
if number == number_of_choice:
    print("In front of the friendly dragon, have your treasure")
else:
    print("I'm greedy and hungry, you are now my food")

print("Do you want to try again (true or false)?")
true = str(input())
false = str(input())
while true == true:
    if true == true:
        if number == number_of_choice:
            print("In front of the friendly dragon, have your treasure")
        else:
            print("I'm greedy and hungry, you are now my food")
            break
    




        

