import random
import json
import os

SCORE_FILE = "scores.json"


def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_scores(scores):
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f)


def play_game(player_name):
    print(f"\n🎮 {player_name}'s Turn")

    print("\nChoose difficulty:")
    print("1 - Easy (1-50 | 10 tries)")
    print("2 - Medium (1-100 | 7 tries)")
    print("3 - Hard (1-200 | 5 tries)")

    while True:
        try:
            level = int(input("Enter level: "))
            if level in [1, 2, 3]:
                break
        except:
            pass

    if level == 1:
        max_number, max_tries = 50, 10
    elif level == 2:
        max_number, max_tries = 100, 7
    else:
        max_number, max_tries = 200, 5

    number = random.randint(1, max_number)
    tries = 0
    score = 100
    last_diff = None
    guesses = []
    print(f"\nNumber is between 1 and {max_number}")

    while tries < max_tries:
        try:
            guess = int(input("Your guess: "))
        except:
            print("Enter a number!")
            continue

        tries += 1
        guesses.append(guess)

        diff = abs(number - guess)

        if guess == number:
            print("🎉 Correct!")
            break

        print("🔥 Hotter!" if last_diff and diff < last_diff else "❄ Colder!" if last_diff else "First try")

        if diff <= 5:
            print("Very close")
        elif diff <= 15:
            print("Close")
        else:
            print("Far")

        print("EVEN" if tries >= 3 and number % 2 == 0 else "ODD" if tries >= 3 else "")
        print("Multiple of 3" if tries >= 4 and number % 3 == 0 else "")

        print("Try smaller" if guess > number else "Try bigger")

        score -= 5 if diff <= 5 else 10 if diff <= 15 else 20

        last_diff = diff

    print("\n📊 Final Report")
    print("Score:", max(score, 0))
    print("Guesses:", guesses)
    print("Correct number:", number)

    return max(score, 0)


def multiplayer():
    p1 = input("Player 1 name: ")
    p2 = input("Player 2 name: ")

    print("\n🔁 Player 1 starts!")
    s1 = play_game(p1)

    print("\n🔁 Player 2 starts!")
    s2 = play_game(p2)

    if s1 > s2:
        print(f"\n🏆 Winner: {p1}")
    elif s2 > s1:
        print(f"\n🏆 Winner: {p2}")
    else:
        print("\n🤝 It's a draw!")


def show_high_scores(scores):
    print("\n🏅 HIGH SCORES")
    for name, score in scores.items():
        print(name, ":", score)


def main():
    scores = load_scores()

    print("\n🎮 GUESS NUMBER GAME")
    print("1 - Single Player")
    print("2 - Multiplayer")
    print("3 - High Scores")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter your name: ")
        score = play_game(name)

        if name not in scores or score > scores[name]:
            scores[name] = score
            save_scores(scores)

    elif choice == "2":
        multiplayer()

    elif choice == "3":
        show_high_scores(scores)

    else:
        print("Invalid choice!")


main()