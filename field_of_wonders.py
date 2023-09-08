import random

words = ["apple", "program", "champion", "python", "elderberry", "fig", "field"]

selected_word = random.choice(words)

attempts = int(input("Enter attempts: "))

hidden_word = ["*"] * len(selected_word)

while attempts > 0:
    print(" ".join(hidden_word))
    guess = input("Enter a letter or a word: ").lower()

    if guess == selected_word:
        print("You guessed the word! Victory!")
        break

    if len(guess) == 1 and guess.isalpha():
        if guess in selected_word:
            for i in range(len(selected_word)):
                if selected_word[i] == guess:
                    hidden_word[i] = guess
        else:
            print("There is no such letter.")
            attempts -= 1
    else:
        print("Incorrect input.")

    if "*" not in hidden_word:
        print("You guessed the word! Victory!")
        break

if attempts == 0:
    print(f"You lost. Correct word: {selected_word}")
