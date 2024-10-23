random_word = "banana"
word_len = len(random_word)

display = ["_","_","_","_","_","_"]


for pos in range(word_len):
  guess = input("enter guess : ")
  if guess == random_word[pos]:
    display[pos] = random_word[pos]
  else:
    pass

print(display)