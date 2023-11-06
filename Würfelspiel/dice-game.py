import random

def roll_dice():
    return random.randint(1, 6)

def main():
    player_score = 0
    computer_score = 0

    print("Willkommen zum Würfelspiel gegen den Computer!")
    input("Drücken Sie Enter, um zu starten...")

    for _ in range(6):
        player_roll = roll_dice()
        computer_roll = roll_dice()

        player_score += player_roll
        computer_score += computer_roll

        print(f"Du hast eine {player_roll} gewürfelt. Der Computer hat eine {computer_roll} gewürfelt.")

    print("\nSpiel beendet!")
    print(f"Dein Endergebnis: {player_score}")
    print(f"Computer Endergebnis: {computer_score}")

    if player_score > computer_score:
        print("Glückwunsch, du hast gewonnen!")
    elif player_score < computer_score:
        print("Der Computer gewinnt. Viel Glück beim nächsten Mal!")
    else:
        print("Unentschieden!")

if __name__ == "__main__":
    main()
