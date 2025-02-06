import random
import hangman
word_list = ["aardvark", "baboon", "camel"]
live=len(hangman.stages)

guessing_word=random.choice(word_list)
print(guessing_word)
place=[]
placeholder=[]
for word in guessing_word:
    place.append(word)
    placeholder.append("_")
    print(placeholder)
game_is_on=True
while game_is_on:
    guess=input("Guess the word")
    for letter in range(len(guessing_word)):
        if guess in place[letter]:
            placeholder[letter]=guess
    print(placeholder)
    if guess not in place:
        live-=1
        print(hangman.stages[live])
    if "_" not in placeholder:
        game_is_on=False
        print("You win!")
    if live==0:
        game_is_on=False
        print("You loose!")
    print(f"{' '.join(placeholder)}")

