import random 


def RockPaperScissors():
    choices = ["Rock", "Paper", "Scissors"]
    win_combo = [("Rock", "Scissors"), ("Paper", "Rock"), ("Scissors", "Paper")]
    score = {"user": 0, "computer": 0, "Draw":0}

    while True:
        try:
            choice = int(input("please choice 1 - 3 : "))

            if 1 <= choice <= 3:
                user_choice = choices[choice - 1]
            else:
                print("Please choose between 1 and 3.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        computer_choice = random.choice(choices)
        print(f"your choice: {user_choice}")
        print(f"computer choice: {computer_choice}")

        if user_choice == computer_choice:
            score["Draw"] += 1
            print("Draw")
        elif (user_choice, computer_choice) in win_combo:
            score["user"] +=1
            print("you win!")
        else:
            print("you loose! computer wins!")
            score["computer"] +=1

        print(f"Score: You {score['user']} - Computer {score['computer']} - Draws {score['Draw']}")
        again = input("you want to play again.press (Y/N):").lower()

        if again != 'y' and again != "n":
            print("please select a correct option Y/N:")
    
        if again == 'n':
            print("Thanks for playing!")
            break


RockPaperScissors()