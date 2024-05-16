user1_name = input("Enter Player1 Name:")
user2_name = input("Enter Player2 Name:")



while True:
    user1_choices = input(user1_name + ", Do you want to select rock, paper or Scissor ?").lower()
    user2_choices = input(user2_name + ", Do you want to select rock, paper or Scissor ?").lower()

    if user1_choices == user2_choices:
        print("it is Tie")
    elif user1_choices == "rock":
        if user2_choices == "scissors":
            print("Rock Wins")
        else:
            print("Paper Wins")
    elif user1_choices == "scissors":
        if user2_choices == "paper":
            print("Scrssors Wins")
        else:
            print("Rock Wins")
    elif user1_choices == "paper":
        if user2_choices == "rock":
            print("Paper Wins")
        else:
            print("Scissors Wins")
    else:
        print("Invalid Input")

    repeat = input("Do you want to play again: Yes/ No :").lower()

    if repeat == "yes":
        pass
    elif repeat == "no":
        break
    else:
        print("invalid Input")
        break
