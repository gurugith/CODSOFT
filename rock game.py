import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Choose 'rock', 'paper', or 'scissors'.")
    
    while True:
        # Get user input
        user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        # Get computer choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display scores
        print(f"Score - You: {user_score}, Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()