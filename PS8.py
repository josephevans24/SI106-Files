## Problem Set 8
import test106 as test

## Please write your name here in a comment -- makes it easier for us grading!

## All graded problems are marked with [PROBLEM <#>].


##### Try/except ###########

# [PROBLEM 1]

# The following code first checks to see if the list has at least three
# items, printing the third item if it exists, and an error message
# otherwise. Rewrite it to have exactly the same effect, but using a 
# try/except statement instead of an if/then.

def f(L):
    try:
        print L[2]
    except:
        print "not enough items in L"


# write your code here
        

###### String Interpolation Questions #######

# [PROBLEM 2]

# Complete the following string interpolation/formatting problems.

# Convert this string interpolation to one using only the + operator, not %.
# Make the variable t equal to the same thing as the variable s.
x = 12
y = 4
s = "You have $%d. If you spend $%d, you will have $%d left." % (x, y, x-y)
# fill in the next line to generate the same string using only the + operator.
# Don't write t = s or otherwise reference s -- use the + operator!
t = "You have $"+str(x)+". If you spend $" +str(y)+ ", you will have $" +str(x-y)+ " left." 

# testing 
test.testEqual(t, s, "convert string interpolation to one using only the + operator, not %")

# Convert this string concatenation to one using string interpolation.
# Assign the result to the variable t. Again, don't refer to s...
x = 12
fname = "Joe"
our_email = "scammer@dontfallforthis.com"
s = "Hello, " + fname + ", you may have won $" + str(x) + " million dollars. Please send your bank account number to " + our_email + " and we will deposit your winnings."
t = "Hello, %s, you may have won $%d million dollars. Please send your bank account number to %s and we will deposit your winnings." % (fname, x, our_email)

# testing
test.testEqual(t, s, "convert string concatenation to one using string interpolation")

# Write code, using string interpolation and the variables nm, min_mt, and mile_amt, to produce the string 
# "Albert walked 0.67 miles today in 50 minutes." Assign it to albert_str.
nm = "Albert"
min_amt = 50
mile_amt = 0.673892
albert_str = "%s walked %0.2f miles today in %d minutes." % (nm, mile_amt, min_amt)


# testing
test.testEqual(albert_str, "Albert walked 0.67 miles today in 50 minutes.", "testing albert_str")

# Define a function called walk_reporter, which takes as input: 
#  - a string that represents someone's name, 
#  - a float that represents the number of miles they walked,
#  - and an integer that represents the number of minutes they spent walking.
#
# The function should RETURN a string in the format:
# "[NAME STR] walked [MILE FLOAT with TWO digits after the decimal] miles in [MINUTES INT] minutes."
# You MUST use string interpolation in the function. 
# You should NOT use raw_input to get the inputs; they are passed in as parameters.

def walk_reporter(nm, miles, mins):
    return "%s walked %0.2f miles in %d minutes." % (nm, miles, mins) # fill in the function body here

# tests for the walk_reporter function
test.testEqual(walk_reporter("Jamie",5.233679,202), "Jamie walked 5.23 miles in 202 minutes.", "walk_reporter test 1")
test.testEqual(walk_reporter("Pythagoras",3.1415926,314),"Pythagoras walked 3.14 miles in 314 minutes.", "walk reporter test 2")

###### Writing a .CSV file #######

# [PROBLEM 3]

# Write code to create a .csv file called [your uniqname]_namescores.csv.
# The .CSV file should have two columns whose first cells are Name and Game-Score.
# Add the lines saved in the variables one_score and two_score.
# Your result should look somewhat like this, in cells IF you open it in MS Excel:
# (if you open the file in a text editor, it will look like a plain text file, with a bunch of commas in it)
# Name Game-Score
# Andy 75
# Jen  82

# Remember, having commas between elements in a string are what make different
# cells in a CSV file in Excel!

# HINT: Think about where you need to make sure you write newline characters.

header_line = ("Name", "Game-Score")
one_score = ("Andy", 75) 
two_score = ("Jen", 82)
print type(one_score)
# Write your code for problem 3 below, using the variables header_line, one_score, and two_score.
# We've included comments that describe the steps you should take --
# you just need to translate them into code.

# Step 1. Open a file for writing with the correct file name specified above, [your uniqname]_namescores.csv.

outfile = open("joblue_namescore.csv","w") #creates a new CSV file called grades.csv that can be opened in programs like    excel and google spread sheet
# output the header row
# output each of the rows:


# Step 2. Now write the header line to the file. Don't forget to also write a '\n' character to mark the end of the line.
outfile.write('"%s","%s"\n' % header_line)
# Step 3. Now write each othe other two lines to the file. Don't forget to also write '\n' characters to mark the ends of the lines.
outfile.write('"%s", "%d"\n' % one_score)
outfile.write('"%s", "%d"\n' % two_score)
# Step 4. Now close the file.
outfile.close()
# Step 5. Now open the file (in a text editor, and then in Excel or Google Sheets) and check to see you made the file you want!

########## This section includes code that you won't change, but do need to understand ##############

# Look through this code and understand it, make comments, test it, pull it apart in your head
# (or in a blank .py file!).

def collapse_whitespace(txt):
    # turn newlines and tabs into spaces and collapse multiple spaces to just one space
    txt = txt.replace("\r", " ").replace("\n", " ").replace("\t", " ")
    res = ""
    prev = ""
    for c in txt:
        # if not second space in a row, use it
        if c != " " or prev != " ":
            res += c
        # current character will be prev on the next iteration
        prev = c
    return res

# get a bunch of text from A Study in Scarlet to use as training data
f = open("train.txt", 'r')
train_txt = collapse_whitespace(f.read())
f.close
# get some other text to use for testing
f = open("test.txt", 'r')
test_txt = collapse_whitespace(f.read())
f.close()
   

# The text includes some weird characters that don't even print out nicely.
# Find the complete alphabet of characters that are used anywhere in the training and testing texts
lets = []
for x in train_txt+test_txt:
    if x not in lets:
        lets.append(x)
alphabet = "".join(sorted(lets))


# Here is a guesser function based on the rule-based guesser 
# in the textbook. It's simplified to make things easier. 
# The simplification is that we only consider
# rules that match the ending (suffix) of the previous text. 
# As a result, we don't need the rule to be a function, just 
# a string that the suffix of the previous text has to match.

# For example, if the rule was ("ca", "bdklmnp"), it would 
# match any text where the last two revealed letters were "ca"
# and it would make the guesses "bdklmnp", in that order, for
# the next letter.

# You'll be using this, with some rules you create, to play the Shannon Game.

def guesser(prev_txt, rls):
    all_guesses = ""
    for (suffix, guesses) in rls:
        try:
            if suffix == None or prev_txt[-len(suffix):] == suffix:
                all_guesses += guesses
        except:
            #error because not enough characters in prev_txt    
            pass 
    return all_guesses

## List of rules -- you'll be adding to this list!

rules = [("q", "uai"),
         (None, alphabet)]

# Note that the second rule will match *any* previous text.
# It ensures that every letter in the text's alphabet will
# be guessed eventually. It should always remain the *last*
# rule in the list, because it doesn't make very good guesses,
# but at least it guesses every letter. Think of it as the default
# rule when nothing else generates a good guess.
         
         
## Here are some sample calls to the guesser function, like the ones provided in the textbook,
## if you want to play with it and remember what it does.
# print guesser(" ", rules) # remember, rules has the value you can see above -- it's a list of tuples!
# print guesser(" The q", rules)
# print guesser(" The qualit", rules)


########### end of code that you don't need to change ###############

# [PROBLEM 4]
# Add comments to the function definition below
# explaining each line and what the function does overall

def performance(txt, rls):
    tot = 0
    #begins the accumulation
    for i in range(len(txt)-1):
        #iterate through the lenght of txt up to last character
        to_try = guesser(txt[:i+1], rls)
        #using the guesser function to see if the previous letters used tell us what to guess based on the list rules
        guess_count = to_try.index(txt[i+1])
        #Creates an integer for the index of the next letter of txt to iterate if a guess is possible by passing through the guesser function
        tot = tot + guess_count
        #Accumulates the total amount of guesses
    print "%d characters to guess\t%d guesses\t%.2f guesses per character, on average\n" % (len(txt) -1, tot, float(tot)/(len(txt) -1))
    #prints how many characters to guess in the text, #the total amount of guesses needed to correctly predict the txt, and the average amount of guesses needed per charcter


# Should be 107641 guesses total)
    
# --------------

# [PROBLEM 5]

# Now you'll start adding extra rules that, hopefully,
# lead to fewer guesses being necessary.

# Write a new rule that will guess capitals first if the 
# previous text is a period followed by a space. 
# HINT: Model this after the rule that determines what comes after q!
# Save that tuple rule into the variable caps_rule.

# Put your code here!
caps_rule = (". ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")



# This code will add your rule to the list of rules:
# (Make sure you've used all the right variable names, like caps_rule, 
#  or else this won't work.)
try:
    rules.insert(1, caps_rule)
except:
    print "the caps_rule tuple does not exist yet"

# testing your caps rule
test.testEqual(guesser("The quick brown fox jumped over the lazy dog. ", rules)[:3], "ABC", "Testing for p_rule")

performance(test_txt, rules)
# should be 107641 guesses total)

# --------------

# [PROBLEM 6]

# Now you'll improve on that by writing rule that will guess letters in order of their
# frequency in the TRAINING SET of A Study in Scarlet. 
# (Stored in the variable train_txt.)

# We've provided you the letter_frequencies function that you wrote in a previous pset.
def letter_frequencies(txt):
    d = {}
    for c in txt:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    return d

# We also provide a concat_all function that takes a list of strings and concatenates them all together.
def concat_all(L):
    res = ""
    for s in L:
        res += s
    return res
    
# Now, write a rule that will guess letters in order of their frequency in the training data,
# no matter what the previous text is. You need to figure out the string of letters to guess, sorted
# in order of their frequency
# HINT: 
# a) Make use of the letter_frequencies function that we've provided to find the letter
# frequencies in train_txt. 
# b) Make a sorted list of the letters, sorted in decreasing order by frequency
# c) Turn that list into a string, using the concat_all function we provided
def next_guess(text):
    c = letter_frequencies(text)
    d = sorted(c.keys(), key = lambda x: c[x], reverse = True)
    e = concat_all(d)
    return e


f = next_guess(train_txt)
# write your code here! This should assign a string for the freqs_rule to a variable.


# Also, replace the tempty string in freqs_rule[1] below with a reference to that variable you just created.
freqs_rule = (None, f)

# This code will add your rule to the list of rules.
# Note that we insert it just before the default rule at
# end, rather than appending it. We still need the default
# rule in case the testing text contains a letter in the 
# alphabet that never appears in the training text.
try:
    rules.insert(-1,freqs_rule)
except:
    print "the freqs_rule tuple does not exist yet"

performance(test_txt, rules)
# should be 15011 guesses total

# --------------

# [PROBLEM 7]

# Now we will add rules that define what to guess after every possible previous letter.

# Here is code to create a dictionary to store the frequency of letters that follow 
# each letter in the alphabet, using some input training text.
# Go through this and comment it with what's happening (you'll be graded on that)!
# Do not change the code!

def next_letter_frequencies(txt):
    r = {}
    #creating a blank dictionary
    for i in range(len(txt)-1):
        #iterating through positions in txt up to the last charcter
        if txt[i] not in r:
            # if the value of txt[i] not in r (i is an integer)
            r[txt[i]] = {}
            #make a new dictionary within the dictionary for that chracter
        next_letter_freqs = r[txt[i]]
        #assings the blank dictionary within the dictionary to next_letter_freqs
        next_letter = txt[i+1]
        #assings value next letter to be the position after the current character
        if next_letter not in next_letter_freqs:
            #if the next letter is not in the dictionary for that letter value...
            next_letter_freqs[next_letter] = 1
            #assing it the value of 1
        else:
            next_letter_freqs[next_letter] = next_letter_freqs[next_letter] + 1
            #if the next letter is already in the dictionary of next letters after the current letter add one to that value
    return r
    #outputs the full dictionary of how frequently the next letter occurs after the current letter

counts = next_letter_frequencies(train_txt)

# The structure of the dictionary counts we created there looks like this:
# {'a':{'b':2,'c':4}, 'd':{'e':6,'a':7}}
# if, for example, b came after a 2 times in the data, 
# and c came after a 4 times
# in the data, e came after d 6 times, and so on.
# You might want to try printing out several different values or
# iterating through the dictionary's keys in different ways to make sure
# you understand the structure. It may also help to put it into an activecode window
# in the textbook and then run it step by step in codelens

# --------------

# [PROBLEM 8] EXTRA CREDIT

# Now write code to add one new rule for each letter in the 
# alphabet, saying what letters to guess next if that letter has
# just appeared.
for key in counts:
    string_to_append = ""
    values = counts[key]
    fix = sorted(values.keys(), key = lambda x: values[x], reverse = True)
    for letter in fix:
        string_to_append += letter
    tuple_to_insert = (key, string_to_append)
    rules.insert(1,tuple_to_insert)

# for i in range(20,40):
#     print rules[i]
# Make sure you insert these new rules at the beginning of the list of
# rules. You want them to take precedence over the generic ordering
# of guesses that you created in the previous problem.

# this code tests the text against all the rules    
performance(test_txt, rules)
print '---------------------------'

# should be 8978 guesses total