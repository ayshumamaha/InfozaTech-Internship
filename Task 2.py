"""INFOZATECH Task 2: Rock, Paper, Scissors Game
Run with: python task2_rock_paper_scissors.py
"""
import random

CHOICES = ("rock", "paper", "scissors")


def decide_winner(player, computer):
    if player == computer:
        return "draw"
    if (player, computer) in {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    }:
        return "player"
    return "computer"


def main():
    player_score = 0
    computer_score = 0
    draws = 0
    print("===== ROCK, PAPER, SCISSORS =====")

    while True:
        player = input("\nChoose rock, paper, scissors, or q to quit: ").strip().lower()
        if player in {"q", "quit", "exit"}:
            break
        if player not in CHOICES:
            print("Invalid choice. Please enter rock, paper, scissors, or q.")
            continue

        computer = random.choice(CHOICES)
        print(f"You chose: {player}")
        print(f"Computer chose: {computer}")
        result = decide_winner(player, computer)

        if result == "draw":
            draws += 1
            print("It's a draw!")
        elif result == "player":
            player_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round.")

        print(f"Score — You: {player_score} | Computer: {computer_score} | Draws: {draws}")

    print("\n===== FINAL SCORE =====")
    print(f"You: {player_score} | Computer: {computer_score} | Draws: {draws}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
