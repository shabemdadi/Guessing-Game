import random

scores = []
playing = True
while playing == True:
    print "Howdy, what's your name"
    player = raw_input("(type in your name) ")
    print "%s, I'm thinking of a number between 1 and 100. Try to guess my number" % player

    number = random.randint(1,100)

    valid = False
    count = 1
    
    while valid == False:
        try:
            guess = int(raw_input("Your guess? "))
            while guess != number:
                if guess < 1 or guess > 100:
                    print "not in the range. Enter a valid number"
                else:   
                    if guess > number:
                        print "Your guess is too high, try again."
                    else:
                        print "Your guess is too low, try again."
                guess = int(raw_input("Your guess? "))
                count = count + 1

            else:
                print "Well done, %s! You found my number in %d tries" % (player, count) 
                valid = True
                again = raw_input("Would you like to play again? ")
                if again == "no":
                    playing = False
                else:
                    scores.append(count)
                    best = min(scores)
                    print "Current best score is", best


        except:
            print "not a number.Enter a valid number"
            count = count + 1
