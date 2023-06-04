import random
from words import word_list
chosen_word =random.choice(word_list)

display = []
word_length = len(chosen_word)
lives = 6

for letter in range(word_length) :
    display+="_"
print(display)
end_of_game = False
while not end_of_game :
    guess = input("Guess a letter").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess :
            display[position]=letter

    print(display)
    if "_" not in display :
        end_of_game = True
        print("You win")
    if guess not in chosen_word :
        lives -=1
        if lives == 0 :
            end_of_game = True
            print("You Lose")

print(f"answer is {chosen_word}")