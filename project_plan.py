#See requirements in the "Final Project Instructions" document in cTools

#####Part I. Describe your project #####

# Include:
# a.	What data sources you will use
# b.	How you plan to process the data you will get.
# c.	How you will present the results.
s = """My project is going to be a mix of creating two classes that can pull up text information from a csv file and a Shannon game guesser that bases
its guesses off of all of my text messages over the past two years. This guesser has 11,587,832 letters to rely on as a data base to make a highly accurate guesser. I plan to process
this data through the creation of my class Textinformation. This class will use functions from PS8 in addition to a few more creative functions to pull off more information about the CSV file you are using as an instance of the class. I will present the results to this by
having my class defined and then using raw input to have someone type in a text they would like to manipulate. After that, the raw input will be run through every function within the class, and let the user know how accurate their training data is. My old text messages will be a baselevel training data to use. The other class Textinformation will tell the user interesting information about their data. Things such as the most used word, most used letter, and five most frequent words in the file they are using."""
print s
print
print "------"

#####Part II: Describe a class you willl define ####

# The name of my class will be...
your_name = "Textinformation"

# Each instance of my class will represent one...
your_inst_represents = "CSV or raw input file to explore data from"

# Each instance of my class will have ... instance variables
your_inst_var_count = 3

# Each instance will have instance variables that keep track of...
your_inst_vars = "This is keeping track of the data within the CSV file. The instance variables will keep track of the file as a whole, the words and their frequency in the file, and the letters and their frequency in the file"

# One method of my class, other than __init__, will be named...
your_method_name = "most_freqs_word"

# When invoked, that method will...
your_method_description = "Tell the user what is the most used word in their raw input or csv file they are running their class through"

print "The name of my class will be %s. Each instance of my class will represent one %s. Each instance will have %d instance variables. The instance variables will keep track of %s. One method of my class, other than __init__, will be named %s. When invoked, that method will %s." % (your_name, your_inst_represents, your_inst_var_count, your_inst_vars, your_method_name, your_method_description)
print
print "----------"

# The name of my class will be...
your_name = "Guesser"

# Each instance of my class will represent one...
your_inst_represents = "CSV or raw input file to explore data from"

# Each instance of my class will have ... instance variables
your_inst_var_count = 3

# Each instance will have instance variables that keep track of...
your_inst_vars = "These variables will keep track of a variety of things such as the CSV file or input the user has given, the rules created from that training data in our guesser, and the data of how accurate the guesser is as a whole when given new data to predict"

# One method of my class, other than __init__, will be named...
your_method_name = "performance"

# When invoked, that method will...
your_method_description = "Tell the user how accurate their training data was as a guesser"

print "The name of my class will be %s. Each instance of my class will represent one %s. Each instance will have %d instance variables. The instance variables will keep track of %s. One method of my class, other than __init__, will be named %s. When invoked, that method will %s." % (your_name, your_inst_represents, your_inst_var_count, your_inst_vars, your_method_name, your_method_description)
print
print "----------"

#No API used in this data