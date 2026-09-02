import random



class RockPaperScissors:

    def __init__(self):
       self.choices = None

    def play(self):
        # Display game rules
        print("Welcome to Rock-Paper-Scissors!\n")
        print("Winning Rules:")
        print("Rock vs Paper -> Paper wins")
        print("Rock vs Scissors -> Rock wins")
        print("Paper vs Scissors -> Scissors wins\n")

        self.choice = ["Rock", "Paper", "Scissors"]

        while True:
            print("chose a option:")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")

            try:
                choice = int(input("Enter your choice"))
            except ValueError:
                print("please enter a valid number")
                continue

            while choice < 1 or choice > 3 :
                choice = int(input("please select a valid choice (1-3) : "))

            user_choice = self.choices[choice - 1 ]           

            print("\n user choice is :", user_choice)
            print("Now computer turn")   

            # computer choice 
            comp_choice = random.randint(1,3)
            computer_choice = self.choices[comp_choice - 1]

            print("Computer choice is ", computer_choice)
            print(user_choice,"vs", computer_choice)

            # winner 
            if choice == comp_choice:
                print("Draw")  
            elif ((choice == 1 and comp_choice == 3) or (choice == 2 and comp_choice == 1) or (choice == 3 and comp_choice)):
                print("user win")
            else: 
                print("computer win")


            while True:
                ans = input("\n Do you want to play again ? (Y/N):").lower()

                if ans == 'n':
                    break
                print()

    print("\n Thanks for playing!")


game = RockPaperScissors()
game.play()