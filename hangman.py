import numpy as np

store = ["apple", "book", "python", "school", "flower"]
word = np.random.choice(store)

view = ["_" for _ in word]
print(view)

limits = 6
guessed = []

hangman_stages = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """
]

while limits > 0:
    enter = input("enter letter: ")

    if enter in guessed:
        print('already tried')
        continue
    else:
        guessed.append(enter)

    if enter in word:
        for i in range(len(word)):
            if word[i] == enter:
                view[i] = enter
    else:
        limits -= 1   
        print(hangman_stages[6 - limits]) 

    print("Current guessed list: ", view)
    print("Remaining attempts: ", limits)

    if '_' not in view:
        print("Player wins" )
        break

if '_' in view:
    print("No more attempts.. You lost")
    print("The correct word was:", word)
