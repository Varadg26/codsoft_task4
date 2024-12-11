import random

def play_game():
    print("*ROCK, PAPER, SCISSORS!*")
    print('*')
    print('Rules:\n 1. Paper beats Rock\n 2. Rock beats Scissors\n 3. Scissors beats Paper')
    for i in range(10):
        print('*')
    print("Enter Your choice:\n 1-Rock\n 2-Paper \n 3-Scissors")

    # User's turn with input validation
    while True:
            user_turn = int(input("Enter your choice : "))
            if user_turn in [1, 2, 3]:
                break  # Valid input, exit loop
            else:
                print("Invalid input! Please enter 1, 2, or 3.")

    if user_turn == 1:
        user_choice = "Rock"
    elif user_turn == 2:
        user_choice = "Paper"
    elif user_turn == 3:
        user_choice = "Scissors"

    # Computer's turn
    comp_turn = random.randint(1, 3)

    if comp_turn == 1:
        comp_choice = "Rock"
    elif comp_turn == 2:
        comp_choice = "Paper"
    elif comp_turn == 3:
        comp_choice = "Scissors"

    print("Let's Play!")
    print("*")
    print(" ROCK! \n PAPER! \n SCISSORS! \n SHOOT!")
    print("*")
    print("User's choice:", user_choice)
    print("Computer's choice:", comp_choice)

    # Calculating the winner
    if user_choice == comp_choice:
        result = "DRAW"
    elif (comp_turn == 1 and user_turn == 2) or (user_turn == 1 and comp_turn == 3) or (comp_turn == 3 and user_turn == 2):
        result = "USER WINS"
    elif (comp_turn == 2 and user_turn == 1) or (user_turn == 3 and comp_turn == 1) or (comp_turn == 2 and user_turn == 3):
        result = "COMPUTER WINS"

    # Print the result
    if result == "DRAW":
        print("It's a DRAW!")
    elif result == "USER WINS":
        print('USER WINS!')
    elif result == "COMPUTER WINS":
        print('COMPUTER WINS!')

    return result

def main():
    user_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        result = play_game()

        # Update win/loss/draw counters
        if result == "USER WINS":
            user_wins += 1
        elif result == "COMPUTER WINS":
            computer_wins += 1
        else:
            draws += 1

        # Show win counts
        print(f"Current Score: USER WINS: {user_wins} | COMPUTER WINS: {computer_wins} | DRAWS: {draws}")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (Y/N): ").strip().lower()

        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
