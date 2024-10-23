
#Hangman game
import random

words_list = ["apple","banana","pear"]  #creating a list of random hundered words

tries = 6 #total tries

random_word = random.choice(words_list) #selecting a random word from the available list
print(random_word)

#creating a guessed_word list
guessed_word_list = []
for i in range(len(random_word)):
  guessed_word_list.append('_')
print(guessed_word_list)


#main game logic 
# tries = 6

guess_char = input("guess char : ")

for pos in range(len(random_word)):
  letter = random_word[pos]
  if guess_char == letter:
    guessed_word_list[pos] = letter
  else:
    pass

print(guessed_word_list)
  
