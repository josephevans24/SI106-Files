import test106 as test
# this imports the module 106test.py, but lets you refer
# to it by the nickname test

#### 1. Write three function calls to the function ``give_greeting``: 

   # * one that will return the string ``Hello, SI106!!!``
   # * one that will return the string ``Hello, world!!!``
   # * and one that will return the string ``Hey, everybody!`` 

# You may print the return values of those function calls, but you do not have to.

def give_greeting(greet_word="Hello",name="SI106",num_exclam=3):
  final_string = greet_word + ", " + name + "!"*num_exclam
  return final_string

#### DO NOT change the function definition above this line (OK to add comments)

# Write your three function calls below


#### 2. Define a function called mult_both whose input is two integers, whose default parameter values are the integers 3 and 4, and whose return value is the two input integers multiplied together.

print "\n---\n\n"
print "Testing whether your function works as expected (calling the function mult_both)"
test.testEqual(mult_both(), 12)
test.testEqual(mult_both(5,10), 50)

#### 3. Use a for loop to print the second element of each tuple in the list ``new_tuple_list``.

new_tuple_list = [(1,2),(4, "umbrella"),("chair","hello"),("soda",56.2)]


#### 4. You can get data from Facebook that has nested structures which represent posts, or users, or various other types of things on Facebook. We won't put any of our actual Facebook group data on this textbook, because it's publicly available on the internet, but here's a structure that is almost exactly the same as the real thing, with fake data. 

# Notice that the stuff in the variable ``fb_data`` is basically a big nested dictionary, with dictionaries and lists, strings and integers, inside it as keys and values. (Later in the course we'll learn how to get this kind of thing directly FROM facebook, and then it will be a bit more complicated and have real information from our Facebook group.)

# Follow the directions in the comments!

# first, look through the data structure saved in the variable fb_data to get a sense for it.

fb_data = {
    "data": [
    {
    "id": "2253324325325123432madeup", 
    "from": {
      "id": "23243152523425madeup", 
      "name": "Jane Smith"
    }, 
    "to": {
      "data": [
        {
          "name": "Your Facebook Group", 
          "id": "432542543635453245madeup"
        }
      ]
    }, 
    "message": "This problem might use the accumulation pattern, like many problems do", 
    "type": "status", 
    "created_time": "2014-10-03T02:07:19+0000", 
    "updated_time": "2014-10-03T02:07:19+0000"
    }, 

    {
    "id": "2359739457974250975madeup", 
    "from": {
      "id": "4363684063madeup", 
      "name": "John Smythe"
    }, 
    "to": {
      "data": [
        {
          "name": "Your Facebook Group", 
          "id": "432542543635453245madeup"
        }
      ]
    }, 
    "message": "Here is a fun link about programming", 
    "type": "status", 
    "created_time": "2014-10-02T20:12:28+0000", 
    "updated_time": "2014-10-02T20:12:28+0000"
    }]
}

# Here are some questions to help you. You don't need to 
# comment answers to these (we won't grade your answers)
# but we suggest doing so! They 
# may help you think through this big nested data structure.

# What type is the structure saved in the variable fb_data?
# What type does the expression fb_data["data"] evaluate to?
# What about fb_data["data"][1]?
# What about fb_data["data"][0]["from"]?
# What about fb_data["data"][0]["id"]?

# Now write a line of code to assign the value of the first 
# message ("This problem might...")  in the big fb_data data 
# structure to a variable called first_message. Do not hard code your answer! 
# (That is, write it in terms of fb_data, so that it would work
# with any content stored in the variable fb_data that has
# the same structure as that of the fb_data we gave you.)
print "testing whether variable first_message was set correctly"
test.testEqual(first_message,fb_data["data"][0]["message"])

#### 5. Here's a warm up exercise on defining and calling a function:

# Define a function is_prefix that takes two strings and returns 
# True if the first one is a prefix of the second one, 
# False otherwise.

# Here's a couple example function calls, printing the return value 
# to show you what it is.
print is_prefix("He","Hello") # should print True
print is_prefix("Hi","Hello") # should print False
      
print 'testing whether "Big" is a prefix of "Bigger"'
test.testEqual(is_prefix("Big", "Bigger"), True)
print 'testing whether "Bigger" is a prefix of "Big"'
test.testEqual(is_prefix("Bigger", "Big"), False)


#### 6. Now, in the next few questions, you will ll build components and then a complete program that lets people play Hangman. Below is an image from the middle of a game...

# Your first task is just to understand the logic of the program, by matching up elements of the flow chart above with elements of the code below. In later problems, you'll fill in a few details that aren't fully implemented here.  For this question, write which lines of code go with which lines of the flow chart box, by answering the questions in comments at the bottom of this activecode box. 

# (Note: you may find it helpful to run this program in order to understand it. It will tell you feedback about your last guess, but won't tell you where the correct letters were or how much health you have. Those are the improvements you'll make in later problems.)

def blanked(word, guesses):
  return "blanked word"
  
def health_prompt(x, y):
  return "health prompt"

def game_state_prompt(txt ="Nothing", h = 6, m_h = 6, word = "HELLO", guesses = ""):
   res = "\n" + txt + "\n"
   res = res + health_prompt(h, m_h) + "\n"
   if guesses != "":
       res = res + "Guesses so far: " + guesses.upper() + "\n"
   else:
       res = res + "No guesses so far" + "\n"
   res = res + "Word: " + blanked(word, guesses) + "\n"

   return(res)

def main():
   max_health = 3
   health = max_health
   secret_word = raw_input("What's the word to guess? (Don't let the player see it!)")
   secret_word = secret_word.upper() # everything in all capitals to avoid confusion
   guesses_so_far = ""
   game_over = False

   feedback = "let's get started"

   # Now interactively ask the user to guess
   while not game_over:
       prompt = game_state_prompt(feedback, health, max_health, secret_word, guesses_so_far)
       next_guess = raw_input(prompt)
       next_guess = next_guess.upper()
       feedback = ""
       if len(next_guess) != 1:
           feedback = "I only understand single letter guesses. Please try again."
       elif next_guess in guesses_so_far:
           feedback = "You already guessed that"
       else:
           guesses_so_far = guesses_so_far + next_guess
           if next_guess in secret_word:
               if blanked(secret_word, guesses_so_far) == secret_word:
                   feedback = "Congratulations"
                   game_over = True
               else:
                   feedback = "Yes, that letter is in the word"
           else: # next_guess is not in the word secret_word
               feedback = "Sorry, " + next_guess + " is not in the word."
               health = health - 1
               if health <= 0:
                   feedback = " Waah, waah, waah. Game over."
                   game_over= True

   print(feedback)
   print("The word was..." + secret_word)

# What line(s) of code do what's mentioned in box 1?

# What line(s) of code do what's mentioned in box 2?

# What line(s) of code do what's mentioned in box 3?

# What line(s) of code do what's mentioned in box 4?

# What line(s) of code do what's mentioned in box 5?

# What line(s) of code do what's mentioned in box 6?

# What line(s) of code do what's mentioned in box 7?

# What line(s) of code do what's mentioned in box 8?

# What line(s) of code do what's mentioned in box 9?

# What line(s) of code do what's mentioned in box 10?

# What line(s) of code do what's mentioned in box 11?

         


#### 7. The next task you have is to create a correct version of the blanked function:

# define the function blanked(). 
# It takes a word and a string of letters that have been revealed.
# It should return a string with the same number of characters as
# the original word, but with the unrevealed characters replaced by _ 
     
# a sample call to this function:
print(blanked("hello", "elj"))
#should output _ell_

print "testing blanking of hello when e,l, and j have been guessed"
test.testEqual(blanked("hello", "elj"), "_ell_")
print "testing blanking of hello when nothing has been guessed"
test.testEqual(blanked("hello", ""), "_____")
print "testing blanking of ground when r and n have been guessed"
test.testEqual(blanked("ground", "rn"), "_r__n_")


#### 8. Now you have to create a good version of the health_prompt() function.

# define the function health_prompt(). The first parameter is the current
# health and the second is the the maximum health you can have. It should return a string 
# with + signs for the current health, and - signs for the health that has been lost.

print(health_prompt(3, 7))
#this should produce the output
#health: +++----

print(health_prompt(0, 4))
#this should produce the output
#health: ----

print "testing health_prompt(3, 7)"
test.testEqual(health_prompt(3,7), "+++----")
print "testing health_prompt(0, 4)"
test.testEqual(health_prompt(0, 4), "----")
   
#### 9. Now you have a fully functioning hangman program! 

# uncomment the next line of code to run the hangman program
# main()

i = 0

def testEqual(actual, expected, feedback = ""):
    global i
    i += 1
    print "--",
    if type(expected) != type(actual):
        print "Failed test %d: %s\n\ttype of expected and actual don't match" % (i, feedback)
        return False
    if type(expected) == type(1):
        # they're integers, so check if exactly the same
        if actual == expected:
            print'Pass test %d: %s'  % (i, feedback)
            return True
    elif type(expected) == type(1.11):
        # a float is expected, so just check if it's very close, to allow for
        # rounding errors
        if abs(actual-expected) < 0.00001:
            print'Pass test %d: %s'  % (i, feedback)
            return True
    elif type(expected) == type([]):
        if len (expected) != len(actual):
            print "Failed test %d: %s\n\tLengths don't match" % (i, feedback)
            return False
        else:
            for (x, y) in zip(expected, actual):
                if x != y:
                    print "Failed test %d: %s\n\titems in expected and actual do not match" % (i, feedback)
                    return False
            print'Pass test %d: %s'  % (i, feedback)
            return True
    else:
        # check if they are equal
        if actual == expected:
            print'Pass test %d: %s'  % (i, feedback)
            return True
    print 'Failed test %d: %s\n\texpected:\t%s\n\tgot:\t\t%s' % (i, feedback, expected, actual)
    return False