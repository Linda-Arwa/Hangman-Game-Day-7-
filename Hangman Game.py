import random

from hangman_words import word_list

# word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
#print(chosen_word)

# Create a variable called 'lives' to keep track of the number of lives left. 
# Set 'lives' to equal 6.
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.

from hangman_art import logo
print(logo)

#Create an empty List called display.

display = []

#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

for char in chosen_word:
    display += "_"
print(display)


# while loop is needed here so that each letter guessed by the user fills up the display list.

end_of_game = False

while not end_of_game:
    
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter\n").lower()
    
    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for char in chosen_word:
        if char == guess:
            print("right")
        else:
            print("wrong")
       
# Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # print(letter)
        if letter == guess:
            display[position] = letter
            
    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            
    #print(display)
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    
    if "_" not in display: # used in keyword
        end_of_game = True
        print("You win")
        
# Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])
