import random #importing module
playing = True #initialise
number = str(random.randint(0,9)) #random in-built function
print ("I will generate")
print("a number from o to 9, and you have to guess the numberone digit at a time.")
print("The game ends when you get 1 hero!")
#iterate loop till the condition is true while playing:
while playing:
    guess = input("Give me your best guess! \n")
    if  number == guess:
       
     print ("You win the game")
     print("The number was", number)
     break
    else:
       print("your guess was not right")
