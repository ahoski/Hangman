import random 
name = input("What would you like to be called? ")
print("Good Luck", name)
words= ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 
        'player', 'condition', 'reverse', 'water', 'board', 'garden', 'football',
        'gaming', 'tennis', 'fire', 'ice', 'thor', 'birthday','captain','tolerate']

word = random.choice(words)
print("Guess the characters in the word : ")

guesses = ''
turns=12
while turns >0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")

            failed+=1

    if failed ==0:
        print("You win, congrats!!!")
        print("The word is ",word)
        break

    guess = input("Guess a character : ")

    guesses+=guess

    if guess not in word:
        turns -= 1
        print("wrong")
        print("You have",+turns,"more guesses" )

        if turns==0:
            print("you loose,better luck next time :)")