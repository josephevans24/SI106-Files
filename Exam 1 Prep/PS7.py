# Problem Set 7
import test106 as test
import random

## NAME: [please put your name here to make it easier on us grading]

## NOTE: All places where you have to do work/write a comment/change code/add code
##       in this problem set are marked with the word "PROBLEM". If you're looking
##       for where you need to add code and get confused, search for that, and read
##       the code and directions around it to understand the context of what you need
##       to do!

##########

## [PROBLEM 1] - Unix problems...

# run the unix curl program to download the
# list of all valid scrabble words 
# curl http://www.puzzlers.org/pub/wordlists/ospd.txt
# Then run it again and save the output to a file called words.txt
# curl http://www.puzzlers.org/pub/wordlists/ospd.txt > words.txt`
# ----------------

## SORTING EXERCISES

# ----------------

## [PROBLEM 2] 

fall_list = ["leaves","apples","autumn","bicycles","pumpkin","squash","excellent"]
sorted_fall_list = sorted(fall_list, reverse = True)
print sorted_fall_list
# Write code to sort the list fall_list in reverse alphabetical order. 
# Assign the sorted list to the variable sorted_fall_list.

# Now write code to sort the list fall_list by length of the word, longest to shortest.
# Assign this sorted list to the variable length_fall_list.

length_fall_list = sorted(fall_list, key = len, reverse = True)
try:
    test.testEqual(sorted_fall_list[0], 'squash', "squash first")
    test.testEqual(length_fall_list[0], 'excellent', "excellent first")
except:
    print "sorted_fall_list or length_fall_list don't exist or have no items"

# -----------------

## [PROBLEM 3]

food_amounts = [{"sugar_grams":245,"carbohydrate":83,"fiber":67},{"carbohydrate":74,"sugar_grams":52,"fiber":26},{"fiber":47,"carbohydrate":93,"sugar_grams":6}]

# Write code to sort the list food_amounts by the key "sugar_grams", from lowest to highest.
# Assign the sorted list to the variable sorted_sugar.
sorted_sugar = sorted(food_amounts, key = lambda food_amounts: food_amounts['sugar_grams'])
print sorted_sugar
# Now write code to sort the list food_amounts by 
#  the value of the key "carbohydrate" minus the value of the key "fiber" in each one, from lowest to highest.
# Assign this sorted list to the variable raw_carb_sort.


raw_carb_sort = sorted(food_amounts, key = lambda x: x['carbohydrate'] - x['fiber'])

try:
    test.testEqual(sorted_sugar[0], food_amounts[2], "sorted_sugar test")
    test.testEqual(raw_carb_sort[0], food_amounts[0], "raw_carb_sort test")
except:
    print "sorted_sugar or raw_carb_sort don't exist or have no items"

# ----------------Don't change code in this seciton----------------

## You won't need to change any code above this line. But definitely
## read it and understand it! Hint: Thinking back and looking at the flow chart from
## the first user-played Hangman problem set may help.

# Below is the full set of Hangman code.
# If you run this code without adding or changing anything, 
# the computer will play Hangman on manual mode, so
# if you keep pressing Enter, you can watch it play.

# Try it out! Then you'll build a couple functions that will make this game better.

# this block of code will get a bunch of random words for the computer to choose
# from as the word to guess. Make sure you download the words.txt file (using curl above, the UNIX problem) 
# Also, make sure you download the test.py file, from cTools
all_words = []
f = open('words.txt', 'r')
for l in f.readlines():
    all_words.append(l.strip().upper())
f.close()
## just use a subset of the dictionary, to keep the program from running too slow.
random.seed("This is a fixed seed so the random number generator will always pick the same 2000 words. Makes debugging easier.")
all_words = random.sample(all_words, 2000)
print all_words[0]


def guess(blanked_word, guesses_so_far, all_words=all_words, version=1, manual=False):
    """Return a single letter (upper case)"""
    # version 1 guesses the letters in alphabetic order
    # version 2 (to be implemented), guesses them in order of frequency of occurrence in the list all_words
    # version 3 (to be implemented), guesses them in order of frequency of occurrence in the list of words that are still possible, given the guesses_made and the current state of the blanked_word
    
    if version == 1:
        guesses = "abcdefghijklmnopqrstuvwxyz".upper()
    elif version == 2:
        guesses = sorted_letters(letter_frequencies(all_words))
    else:
        guesses = sorted_letters(letter_frequencies(possible_words(blanked_word, guesses_so_far, all_words)))
    if manual:
        print "guesses: ", guesses
    for let in guesses:
        if let not in guesses_so_far:
            if manual:
                print "guessing: ", let
            return let
    # if all of the letters to guess have already been guessed, something's gone wrong!
    print "something went wrong! No more letters to guess"
    return None
        
# this function tells you how many guesses you made 
# vs how many guesses you COULD have gotten the word in
def show_results(word, guess_count):
    """Results to show at end of game"""
    print "You got it in " + str(guess_count) + " guesses."
    if guess_count == len(set(list(word))):
        print "Awesome job."
    else:
        print "You could have gotten it in " + str(len(set(list(word)))) + " guesses."

# from ps6        
def blanked(word, revealed_letters):
   blanked_word = "" # assigning the empty string to the blanked_word to be accumulated
   for ch in word:
      if ch in revealed_letters: # if the letter has been revealed
         blanked_word = blanked_word + ch # add that letter to be visible in the blanked word
      else: # otherwise,
         blanked_word = blanked_word + "_" # add a blank
   return blanked_word

# from ps6
def health_prompt(current_health, max_health):
   return "+"*current_health + "-"*(max_health-current_health) # multiplying strings by proper amounts and returning the new, concatenated string

# from ps6
def game_state_prompt(txt, h, m_h, word, guesses):
    """Returns a string showing current status of the game"""
    res = txt + "\n"
    res = res + health_prompt(h, m_h) + "\n"
    if guesses != "":
        res = res + "Guesses so far: " + guesses.upper() + "\n"
    else:
        res = res + "No guesses so far" + "\n"
    res = res + "Word: " + blanked(word, guesses) + "\n"
    return(res)

# Helper function to count how many distinct characters are in the word.
# It is used to determine the minimum number of guesses that are needed
# to guess the word
def count_distinct_chars(word):
    chars_so_far = ""
    for c in word:
        if c not in chars_so_far:
            chars_so_far = chars_so_far + c
    return len(chars_so_far)
    
#### GAMEPLAY
# This following function makes the computer play the game.
# Note the default parameters, go through the code, and think about what each part means.
def play_game(manual=False, version = 1, max_health = 26):
    """Plays one game"""
    health = max_health
    word = random.choice(all_words)
    word = word.upper() # everything in all capitals to avoid confusion
    guesses_made = ""
    game_over = False

    feedback = "let's get started"

    while not game_over:
        if manual: # if manual is set to true, the user will have to keep pressing enter to keep going with the game
            # now, give the user a chance to see what happened on previous guess
            prompt = game_state_prompt(feedback, health, max_health, word, guesses_made)
            full_prompt = prompt + "Press enter to make the program guess again; anything else to quit\n"
            command = raw_input(full_prompt)
            if command != "":
                # user entered a character, so (s)he wants to stop the game
                return
        # call your function guess to pick a next letter
        next_guess = guess(blanked(word, guesses_made), guesses_made, all_words, version, manual)
        
        # proceed as with last week to process the next_guess
        guesses_made = guesses_made + next_guess
        if next_guess in word:
            if blanked(word, guesses_made) == word:
                feedback = "Congratulations"
                game_over = True
            else:
                feedback = "Yes, " + next_guess + " is in the word"
        else: # next_guess is not in the word word
            feedback = "Sorry, " + next_guess + " is not in the word."
            health = health - 1
            if health <= 0:
                feedback = " Waah, waah, waah. Game over."
                game_over= True

    if manual:
        # this is outside the for loop; it happens once game_over is True
        print(feedback)
        print("The word was..." + word)
        if health > 0:
            show_results(word, len(guesses_made))

    return len(guesses_made), count_distinct_chars(word)


## [PROBLEM 4]
play_game(max_health = 20)


# This code will run initially. 
# After you've played around with the guesser, change the call to play_game so 
# a game is played with a maximum of 3 wrong guesses before the game ends.
# (Hint: Which parameter affects that?)


# ------------------end of section with code you aren't supposed to change----


# Now, you're going to start making some tools to play Hangman better.

## [PROBLEM 5]

# First, you need to define a function called letter_frequencies.
# This function should take as input:
        # - a list words
# It should return a dictionary whose key value pairs are letters and the number
#   of times each letter appears in the total set of words. For example, {"A":3,"T":6} ...

# Finish the function definition below, adding parameters and function body.
def letter_frequencies(x):
    d = {}
    for a in x:
        for b in a:
            if b not in d:
                d[b] = 1
            else:
                d[b] += 1
    return d
x = ['hi','sup', 'what happens']
print letter_frequencies(x)
# this code helps test whether your letter_frequencies function is working!
test_words = ["HELLO", "GOODBYE"]
r = letter_frequencies(test_words)
try:
    test.testEqual(r['H'], 1, "H occurs once")
    test.testEqual(r['O'], 3, "O occurs three times")
except:
    print "couldn't look up 'H' or 'O' in dictionary r"
    
# --------------

# [PROBLEM 6]

# Now you will define a function sorted_letters.
# It takes a dictionary of the kind returned by
# letter_frequencies(). sorted_letters returns a
# sorted list of the keys, sorted by the associated
# counts, in decreasing order.

def sorted_letters(counts):
    sort_list = counts.keys()
    sorted_list = sorted(sort_list, key = lambda x: counts[x], reverse = True)
    return sorted_list
test_words = ["HELLO", "GOODBYE"]
r = letter_frequencies(test_words)
print r    
try:
    test.testEqual(sorted_letters(r)[:2], ['O', 'E'], "sorted_letters")
except:
    print "sorted_letters is not defined, or there's an error in sorted_letters. Try calling sorted_letters yourself in order to see what the error message is."
 
# Once you pass the tests, make another call to play_game. 
# This time, pass a parameter that tells it to use version 2
# It will call your letter_frequencies function and usually
# guess better than the alphabetic guesser (version 1)

 
# --------------

# [PROBLEM 7]
# Now you will define a function possible that determines
# whether a word is still possible, given the guesses that
# have been made and the current state of the blanked word.
#   If a letter has been guessed but not revealed in the blanked
#   word, that eliminates all words with that letter.
#   If a letter has been guessed and is revealed, that
#   eliminates all words without that letter.

def possible(word, blanked, guesses_made):
    for a in word:
        if a in guesses_made:
            if a not in blanked:
                return False
    for b in guesses_made:
        if b in word:
            if b not in blanked:
                return False
    return True
   
    
            
        

        

            
test.testEqual(possible("HELLO", "_ELL_", "ELJ"), True, "possible first test")
test.testEqual(possible("HELLO", "_ELL_", "ELJH"), False, "possible second test")
test.testEqual(possible("HELLO", "_E___", "ELJ"), False, "possible third test")

# --------------

# [PROBLEM 8]

# Now, you should define a function called possible_words.
# This function takes as input 
#    - the blanked word so far,
#    - the string of guesses that have been made so far
#    - the list of all words the game might pick
# It returns a list of words that are still possible to be the word 
#   that needs to be guessed, given this information.

# HINT: You want to return a list of things... what pattern might be useful here?
# HINT 2: make use of the function possible() that you defined in the previous problem

def possible_words(blanked, guesses_made, total_words):
    list_words = []
    for word in total_words:
        if possible(word, blanked, guesses_made):
            list_words.append(word)
    return list_words


test.testEqual(possible_words("_ed", "edj", ["fed", "bed", "led"]), ["fed", "bed", "led"], "possible words")
# if f has been guessed already, then "fed" is no longer one of the possible words
test.testEqual(possible_words("_ed", "edjf", ["fed", "bed", "led"]), ["bed", "led"], "possible words second test")
 
# Once you pass the tests, make another call to play_game. 
# This time, pass a parameter that tells it to use version 3.
# It will call letter_frequencies on only those words that
# are still possible, so it might be a little better than 
# version 2.
    
# --------------

## [PROBLEM 9]

# Now, we are going to see how much better, on average, 
# versions 2 and 3 do.

# play_game returns two values (a tuple):
#   the number of guesses made and 
#   the minimum number of guesses that were required

# To get a sense of the average performance,
# we will have each guesser play the game 30 times. 
# We accumulate the total number of guesses that were made and the
# minimum number that were required, across all 30 games. 
# You'd get really bored having to hit Enter a lot of times.
# To avoid that, we set manual=False in the calls to play_game()
#(Note: it may take a while to complete 30 games on 
# versions 2 and 3, especially if you have an older computer).

# We have provided the code below, commented out. You should first 
# remove all the # signs, so that it runs. 
# The graded part is to comment it, 
# line by line, explaining what each line does.

for v in [1, 2, 3]:
    print "----version", v
    # This iterates through each version and tells us which one we are currently running
    total_guesses = 0
    #This is to start accumulation on the total guesses made in the game
    total_min_guesses = 0
    #The is the start accumulation on the least amount of total guesses needed
    
    for i in range(30):
        print i, ".",
        #This iterates through each game play and runs 30 times, each integer followed by a period represents one game play.
        
        (guesses, min_guesses) = play_game(version = v, manual=False)
        #This is where the game is played. 
        
        total_guesses = total_guesses + guesses
        #This is where we get the total amount of guesses to get the word
        total_min_guesses = total_min_guesses + min_guesses
        #This is where we find the total minimum amount of guesses needed for the words
    print
    print "ratio:", total_guesses / float(total_min_guesses), ";total guesses:", total_guesses, ";min needed:", total_min_guesses
    #This is printing our data output. The ratio is the average amount of incorrect guesses for correct guesses, then it prints the total amount of guesses needed and then the minimum amount of guesses that could have been asked