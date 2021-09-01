import random 
import stages

hangmanStages = stages.stages

word_arr = [ "philippines", "english", "aeroplane", "ghost"]

# random_number = random.randint(0, (len(word_arr) - 1))
# random_word = word_arr[random_number]
random_word = random.choice(word_arr)
print(f'random word is {random_word}')
empty_game_arr = ["_" for char in random_word]
print(f'This is the word that you have to guess {["_" for char in random_word]}')

game_end = False
life = 7

chars = [char for char in random_word]
emptyGame = []

while not game_end:
    guessedLetter = input("Enter a letter ").lower()
    for position in range(len(empty_game_arr)):
        letter = chars[position]
        if letter == guessedLetter:
            empty_game_arr[position] = letter
    if guessedLetter not in chars:
        life -= 1
        print(hangmanStages[life])
    print(empty_game_arr)
    if life <= 0:
        game_end  = True
        print("You lose")
    if "_" not in empty_game_arr:
        game_end = True
        print("You win")