import random

#engaging
enter = input("Would you like play a guessing game?")
if enter == "yes":
    p1 = input("What is the first player's name?")
    p2 = input("What is the second player's name?")
    print("Okay! The rules are easy, guess the number I'm thinking of between 1 and 10, and you each have five turns. You'll play three times, whoever wins the best of three is the champion.")

#initializing variables and 3 turns
    gameCount = 1
    p1win = 0
    p2win = 0
    for gameCount in range (1,4):
        turnCount = 0
        guess = 0
        right = random.randint(1,10)
        print("Game " + str(gameCount))
#entering loop
        while (turnCount < 10) and (guess != right):
            if (turnCount%2 == 0):
                guess = int(input(p1 + ", what number are you guessing?"))
            else:
                guess = int(input(p2 + ", what number are you guessing?"))
            while (guess < 1) or (guess > 10):
                    print("Sorry, that guess is not between 1 and 10.")
                    guess = int(input("What is your new guess?"))
            if (guess > right):
                print(str(guess) + " is too big!")
            elif (guess < right):
                print(str(guess) + " is too small!")
            else:
                print("Yes! You got it!!")
            if (guess != right) and (turnCount == 9):
                print("You guys used all your guesses, this round is over.")
            if (guess == right) and (turnCount%2 == 0):
                p1win = p1win + 1
            elif (guess == right) and (turnCount%2 != 0):
                p2win = p2win + 1
            turnCount +=1
            gameCount +=1
#out of game
    if (p2win > p1win):
        print("Congratulations " + p2 + ", you won! " + str(p2win) + " out of 3 is pretty good!")
        print("Sorry, " + p1 + ", you gotta do better than " + str(p1win) + " games.")
    elif (p1win > p2win):
        print("Congratulations " + p1 + ", you won! " + str(p1win) + " out of 3 is pretty good!")
        print("Sorry, " + p2 + ", you gotta do better than " + str(p2win) + " games.")
    else:
        print("You guys tied...keep trying...but " + p1 + " and " + p2 + ", you're both losers.")

#end
else:
    print("Okay, see ya.")
print("The end.")
