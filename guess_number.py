import random

while True:

    while True:
        play_again = input("\nDo you want to play the game? (yes/no): ").lower()

        if play_again == "yes":
            break

        elif play_again == "no":
            print("Thank you for playing! Goodbye!")
            exit()

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    secret_number = random.randint(1, 10)

    print("\n================================")
    print("       GUESS THE NUMBER")
    print("================================")
    print("I have selected a number between 1 and 10.")
    print("You have 5 tries to guess it!")

    for attempt in range(1, 6):

        guess = int(input(f"\nTry {attempt} - Enter your guess: "))

        if guess == secret_number:
            print("🎉 Congratulations!")
            print("You guessed the correct number!")
            break

        elif guess < secret_number:
            print("Your guess is LESS than the number.")

        else:
            print("Your guess is GREATER than the number.")

    else:
        print("\n Game Over!")
        print("The correct number was:", secret_number)