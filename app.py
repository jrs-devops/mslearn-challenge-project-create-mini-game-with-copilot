# write 3 variables: rock, paper, scissors
rock = "rock"
paper = "paper"
scissors = "scissors"

wins = 0
losses = 0
ties = 0
# Write a function that makes a user choice between rock, paper, or scissors. Otherwise it will return an error message
def get_user_choice():
    user_choice = input("Please, type rock, paper, or scissors: ")
    if user_choice == rock or user_choice == paper or user_choice == scissors:
        return user_choice
    else:
        print("Invalid input. Please, type rock, paper, or scissors")
        return get_user_choice()
       
# Write a function that takes a string as an argument and returns a string
# that represents the computer's choice ("rock", "paper", or "scissors")
def get_computer_choice():
    import random
    computer_choice = random.choice([rock, paper, scissors])
    return computer_choice
# Write a function that takes two arguments, the user's choice and the computer's choice,
# and returns a string that announces the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == rock and computer_choice == scissors:
        return "You win!"
    elif user_choice == paper and computer_choice == rock:
        return "You win!"
    elif user_choice == scissors and computer_choice == paper:
        return "You win!"
    else:
        return "You lose!"
# write a function to determine number of wins, losses, and ties
def determine_stats(user_choice, computer_choice):
    if user_choice == computer_choice:
        ties += 1
    elif user_choice == rock and computer_choice == scissors:
        wins += 1
    elif user_choice == paper and computer_choice == rock:
        wins += 1
    elif user_choice == scissors and computer_choice == paper:
        wins += 1
    else:
        losses += 1
    return wins, losses, ties
# Write a function that prints the number of wins, losses, and ties
def print_stats(wins, losses, ties):
    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")
# Write a function to determine number of games played
def determine_games_played(wins, losses, ties):
    games_played = wins + losses + ties
    print(f"Games played: {games_played}")
    return games_played
# Write a function that allows user to continue playing the game by typing "screen", if user types "No" the game will exit
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("Computer choice:", computer_choice)
    print(determine_winner(user_choice, computer_choice))
    determine_stats(user_choice, computer_choice)
    while True:
        play_again = input("Play again? Please, type (Screen/No): ")
        if play_again.lower() == "screen":
            play_game()
        if play_again.lower() == "no":
            print_stats(wins, losses, ties)
            determine_games_played(wins, losses, ties)
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please, type (Screen/No)")
# Write the main function that will call the play_game function
def main():
    play_game()