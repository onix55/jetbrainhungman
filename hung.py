import random
print("H A N G M A N")
while True:
    play = input('Type "play" to play the game, "exit" to quit:')    
    if play == "play":
        break
    elif play == "exit":
        exit()

wordslist = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(wordslist)

stars = (len(word) * '-')
list_word = list(word)
list_stars = list(stars)

secretdict = dict()
k = 0
for i in list_word:
    secretdict.update({k:i})
    k += 1

starsdict = dict()
k = 0
for i in list_stars:
    starsdict.update({k:i})
    k += 1

out = "".join(starsdict.values())
count = 8

wrongletters = set()
while count > 0:
    
    if out == word:
        print("You guessed the word!")
        print("You survived!")
        break
    
    while True:
        print("")
        print(out)
        letter = input("Input a letter: ")
        if 0 <= len(letter) > 1:
            print ("You should input a single letter")
        elif letter.isupper():
                print ("Please enter a lowercase English letter")
        elif letter not in set('abcdefghijklmnopqrstuvxywz'):
                print ("Please enter a lowercase English letter")
        else:
            break
    
    if letter in word:
        if letter in out:
            print("You've already guessed this letter")
        else:
            for key,value in secretdict.items():
                if value == letter:
                    starsdict.update({key:letter})            
            out = "".join(starsdict.values())
            #print("")
    else:
        if letter in wrongletters:
            print("You've already guessed this letter")
        else:
            print("That letter doesn't appear in the word")
            wrongletters.add(letter)
            count -= 1    
            if count == 0:
                print("You lost!")