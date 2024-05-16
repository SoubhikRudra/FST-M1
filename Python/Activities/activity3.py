user1_name = input("Enter Player1 Name:")
user2_name = input("Enter Player2 Name:")

user1_choices = input(user1_name + ", Do you want to select rock, paper or Scissor ?").lower()
user2_choices = input(user2_name + ", Do you want to select rock, paper or Scissor ?").lower()

if user1_choices == user2_choices:
    print("it is Tie")
elif user1_choices == "rock":
    if user2_choices == "scissors":
        print("Rock Wins, winner is {}".format(user1_name))
    else:
        print("Paper Wins ")
elif user1_choices == "scissors":
    if user2_choices == "paper":
        print("Scrssors Wins, winner is {}".format(user1_name))
    else:
        print("Rock Wins")
elif user1_choices == "paper":
    if user2_choices == "rock":
        print("Paper Wins, winner is {} ".format(user1_name))
    else:
        print("Scissors Wins")
else:
    print("Invalid Input")