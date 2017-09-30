def hangman(the_word):
    
    solved = False

    found_values = []

    print ("Let's play Hangman!")
    for each in range(len(the_word)):
        found_values.append(0)
    life_count=4+len(the_word)
    while (solved == False):
        life_count=life_count-1
        if life_count>1:
            print("You have "+str(life_count)+" guesses remaining")
        elif life_count>0:
            print("You have "+str(life_count)+" guess remaining")
        else:
            print("Game Over... Better luck next time!")
            break

        the_string = ""
        for each in range(len(the_word)):
            if found_values[each] == 0:
                the_string = the_string + "_"
            else:
                the_string = the_string + the_word[each:each + 1]
        print ("Your word is: " + the_string)

        if is_solved(the_word, found_values):
            solved = True

        if solved == False:
            make_guess(the_word,found_values)
    if life_count>0:
        print ("You Win!")


def is_solved(the_word, found_values):
    flag = True
    for each in range(len(the_word)):
        if found_values[each] == 0:
            flag = False
    return flag


def make_guess(the_word,found_values):
    print("Pick a letter! ")
    letter = (input())
    letter = letter[0:1]

    word = ""

    for each in range(len(the_word)):
        if found_values[each]==0:
            word=word+the_word[each:each+1]
        else:
            word=word+"!"

    if word.find(letter) == -1:
        print ("Sorry! Bad guess.")
    while word.find(letter)!=-1:
        found_values[word.find(letter)] = 1
        word = word.replace(letter,"!",1)



hangman("hangman")
