master = "tnetennba"

word = list(master)
length = len(word)
right = list("_" * length)

finished = False

while finished == False:
    guess = input("Guess a letter!")

    if guess not in master:
        print("This letter is not in the word.")

    for letter in word:
        if letter == guess:
            index = word.index(guess)
            right[index] = guess
            word[index] = "_"

    print(right)

    if list(master == right):
        print("You guessed all the letters! Great work!")
        finished = True
