import random

print("Rock,Paper,Scissor")
print("Computer will choose one of those.")
print("You should choose one.")
print("...")
print("Let's start!!!")


def game(human, computer):
    if( human ==  computer):
        print("You and Computer ties.")

    elif( human == 1):
        if( computer == 2):
            print("Computer win.")
        else:
            print("You win!")

    elif( human == 2):
        if( computer == 3):
            print("Computer win.")
        else:
            print("You win")

    elif( human == 3):
        if( computer == 1):
            print("Computer win.")
        else:
            print("You win!")

    else:
        print("Input Error")
        print("Computer:{}, You:{}".format(computer, me))


computer = random.randint(1, 3)
print("computer:", computer)

me = input("1:Rock, 2:Paper, 3:Scissor  Select the number!>>> ")
me = int(me)

game(me, computer)
print("Computer:{}, You:{}".format(computer, me))