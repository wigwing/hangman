import random

f = open("words.txt","r")
words = f.read().split("\n")
answer = random.choice(words)

guesses = []
incorrect = []
display = [None]*len(answer)
lives = 6

def displayString():
  s = ""
  for c in display:
    if c == None:
      s += "_ "
    else:
      s += c + " "
  return s

while True:
  print(displayString())
  if len(incorrect)>0:
    print("guesses:"+",".join(incorrect))
  print("Guess the letter? (" + str(lives) + " guesses left)")
  g = input(">")
  if len (g)!= 1:
    print("PLS GUESS ONE LETTER AT A TIME")
    continue
  if g in guesses:
    print("already guessed")
    continue
  guesses.append (g)
  if g in answer:
    incomplete = False
    for i,c in enumerate(answer):
      if g == c:
        display[i] = g 
      elif display[i] == None:
        incomplete = True
    if not incomplete:
      print(displayString())
      print("you win")
      break
    print("correct")
  else:
    print ("incorrect")
    incorrect.append(g)
    lives -= 1
    if lives < 1:
      print("you lost better luck next time :)")
      break 
  