import random
computer = random.choice([-1,0,1])
print("---------------------------")
print("      WELCOME TO GAME      ")
print("---------------------------")
you = input("Enter Your Choice-->")
you_dict = {"stone":-1,"paper":0,"scissor":1}
rev_dict = { -1 : "Stone", 0 : "Paper", 1 : "Scissor"}
you_choice = you_dict[you]
print(f"Computer Choice-->{rev_dict[computer]}\nYour Choice-->{rev_dict[you_choice]}")
if(computer == you_choice):
    print("Match Draw")
else:
    if(computer == -1 and you_choice == 0):
        print("You Win")
    elif(computer == -1 and you_choice == 1):
        print("You Lose Computer Win")
    elif(computer == 0 and you_choice == -1):
        print("You Lose Computer Win")
    elif(computer == 0 and you_choice == 1):
        print("You Win")
    elif(computer == 1 and you_choice == -1):
        print("You Lose Computer Win")
    elif(computer == 1 and you_choice == 0):
        print("You Win")
       
print("---------------------------")
