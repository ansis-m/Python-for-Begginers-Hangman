import random
import sys

words = ["python", "java", "swift", "javascript"]

def won(array):

    for z in array:
        if z == '-':
            return False
    return True


def game():

    word = list(words[random.randint(0, len(words) - 1)])
    i = 8
    array = ['-'] * len(word)
    guesses = set()

    while i > 0:
        print("".join(array))
        letter = input("Input a letter:")
        if len(letter) != 1:
            print("Please, input a single letter.")
            continue
        if not letter.isalpha() or not letter.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        if letter in guesses:
            print("You've already guessed this letter.")
            continue
        guesses.add(letter)
        not_found = True
        for j in range(len(word)):
            if letter == word[j]:
                array[j] = letter
                not_found = False
        if won(array):
            print("""You guessed the word {}!
            You survived!""".format("".join(word)))
            return 1, 0
        if not_found:
            print("That letter doesn't appear in the word. ")
            i = i - 1
        print("# {} attempts\n".format(i))

    print("You lost!")
    return 0, 1


def main():
    won = 0
    lost = 0
    print("H A N G M A N   # 8 attempts\n")

    while True:
        menu = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:")
        if menu == "play":
            w, l = game()
            won += w
            lost += l
        elif menu == "exit":
            break
        elif menu == "results":
            print("You won: {} times.".format(won))
            print("You lost: {} times.".format(lost))


if __name__ == "__main__":
    main()