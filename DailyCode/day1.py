# number guessing game 
import random
# Guess the number 
class guessTheNumber:

    def __init__(self):
        self.number = random.randint(0,50)
        self.count = 0
        self.max_attempts = 5

    def guess(self, user_guess):
        self.count +=1
        if self.number == user_guess:
            return f"Correct Guess {self.number}"             
        elif self.number >= user_guess:
            return  "Too low"
        else:
            return "Too high"
      
    def play(self):
     
        while self.count < self.max_attempts:
            user_guess = int(input("Guess the number"))

            result = self.guess(user_guess)
            print(result)

            if user_guess == self.number:
                print(f"You won in {self.count} attemps")
                return
        print(f"Try again! you losse number was {self.number}")


game = guessTheNumber()
game.play()


        

