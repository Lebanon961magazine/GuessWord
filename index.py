import random


def choose_word():
    words = [
        ("cedar", "A type of tree that is a national emblem of Lebanon."),
        ("beirut", "The capital and largest city of Lebanon."),
        ("lebanon", "A country located in the Middle East, known for its rich history and culture."),
        ("mediterranean", "The sea that borders Lebanon to the west."),
        ("history", "The study of past events in Lebanon and around the world."),
        ("culture", "The customs, arts, and achievements of a particular group in Lebanon."),
        ("mountains", "Lebanon is home to a range of these natural formations.")
    ]
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def main():
    attempts_per_word = 6
    total_score = 0

    print("Welcome to the Lebanon Word Guessing Game!")
    print("Try to guess words related to Lebanon.")

    while True:
        word_to_guess, definition = choose_word()
        guessed_letters = []
        attempts = attempts_per_word

        print("\nGuess The Word:", definition)
        print(f"({attempts} attempts remaining)")

        while attempts > 0:
            display = display_word(word_to_guess, guessed_letters)
            print(display)

            if display == word_to_guess:
                print("Congratulations! You guessed the word:", word_to_guess)
                total_score += 1
                print("Total Score:", total_score)
                break

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess in word_to_guess:
                print("Correct!")
            else:
                print("Incorrect!")

                attempts -= 1
                print(f"{attempts} attempts remaining.")

                if attempts == 0:
                    print("Sorry, you're out of attempts. The word was:", word_to_guess)
                    break


if __name__ == "__main__":
    main()
