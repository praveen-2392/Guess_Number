import random
class GuessNumberGame:

    def __init__(self):
        self.secret_number = random.randint(1, 10)
        self.attempts = 5

    def play(self):
        print("\n================================")
        print("       GUESS THE NUMBER")
        print("================================")
        print("I have selected a number between 1 and 10.")
        print(f"You have {self.attempts} tries to guess it!")

        for attempt in range(1, self.attempts + 1):
            guess = int(input(f"\nTry {attempt} - Enter your guess: "))

            if guess == self.secret_number:
                print(" Congratulations!")
                print("You guessed the correct number!")
                break

            elif guess < self.secret_number:
                print("Your guess is LESS than the number.")

            else:
                print("Your guess is GREATER than the number.")

        else:
            print("\nGame Over!")
            print("The correct number was:", self.secret_number)
    def play_again(self):

        while True:

            choice = input(
                "\nDo you want to play again? (yes/no): "
            ).lower()

            if choice == "yes":
                return True

            elif choice == "no":
                print("Thank you for playing! Goodbye!")
                return False

            else:
                print("Invalid input. Please enter yes or no.")


while True:
    game = GuessNumberGame()
    game.play()

    if not game.play_again():
        break