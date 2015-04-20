import test106 as test
import csv

def collapse_whitespace(txt):
        # turn newlines and tabs into spaces and collapse multiple spaces to just one space
        res = ""
        prev = ""
        for c in txt:
            # if not second space in a row, use it
            if c == " " or prev == " ":
                res = res + c.replace(" ", "")
            else:
                res = res + c
            # current character will be prev on the next iteration
        return res



class TextInformation:
    def __init__(self, txt_in):
        self.txt = txt_in
    
    def most_freqs_lets(self):
        if type(self.txt) == type(""):
            dictionary_wanted_output = {}
            split = collapse_whitespace(self.txt)
            for a in split:
                if a not in dictionary_wanted_output:
                    dictionary_wanted_output[a] = 1
                else:
                    dictionary_wanted_output[a] += 1
            keys = dictionary_wanted_output.keys()
            first = keys[0]
            for b in keys:
                if dictionary_wanted_output[b] > dictionary_wanted_output[first]:
                    first = b
            print "%s occurs %d times" % (first, dictionary_wanted_output[first])
        elif type(self.txt) == type([]):
            dictionary_wanted_output = {}
            for a in self.txt:
                for b in a:
                    if b not in dictionary_wanted_output:
                        dictionary_wanted_output[b] = 1
                    else:
                        dictionary_wanted_output[b] += 1
            keys = dictionary_wanted_output.keys()
            first = keys[0]
            for c in keys:
                if dictionary_wanted_output[c] > dictionary_wanted_output[first]:
                    first = b
            print "%s occurs %d times" % (first, dictionary_wanted_output[first])
        elif type(self.txt) == type({}):
            keys = self.txt.keys()
            first = keys[0]
            for b in keys:
                if self.txt[b] > self.txt[first]:
                    first = b
            print "%s occurs %d times" % (first, self.txt[first])
    def most_freqs_word(self):
        if type(self.txt) == type([]):
            dictionary_wanted_output = {}
            for a in self.txt:
                if a not in dictionary_wanted_output:
                    dictionary_wanted_output[a] = 1
                else:
                    dictionary_wanted_output[a] += 1
            keys = dictionary_wanted_output.keys()
            first = keys[0]
            for b in keys:
                if dictionary_wanted_output[b] > dictionary_wanted_output[first]:
                    first = b
            print "%s occurs %d times" % (first, dictionary_wanted_output[first])
        elif type(self.txt) == type(""):
            dictionary_wanted_output = {}
            split = self.txt.split()
            for a in split:
                if a not in dictionary_wanted_output:
                    dictionary_wanted_output[a] = 1
                else:
                    dictionary_wanted_output[a] += 1
            keys = dictionary_wanted_output.keys()
            first = keys[0]
            for b in keys:
                if dictionary_wanted_output[b] > dictionary_wanted_output[first]:
                    first = b
            print "%s occurs %d times" % (first, dictionary_wanted_output[first])
        elif type(self.txt) == type({}):
            keys = self.txt.keys()
            first = keys[0]
            for b in keys:
                if self.txt[b] > txt[first]:
                    first = b
            print "%s occurs %s times" % (first, self.txt[first])
        else:
            print "Can't get the most frequent word"


    def word_count(self, name):
        accum = 0
        txt = self.txt.lower()
        count_it = txt.split()
        for a in count_it:
            if name in a:
                accum += 1
        print "%s occurs %d times" % (name, accum)
    def top_five(self):
        dictionary_wanted_output = {}
        banana = self.txt.split()
        for a in banana:
            if a not in dictionary_wanted_output:
                dictionary_wanted_output[a] = 1
            else:
                dictionary_wanted_output[a] += 1
        going = sorted(dictionary_wanted_output.keys(), key = lambda x: dictionary_wanted_output[x], reverse = True)
        print "For this file the top five most used words are: %s" % (going[:5])

class ShannonGameGuesser:
    def __init__(self, txt_in, guesser_txt_in):
        self.txt = txt_in
        self.guesser_txt = guesser_txt_in
        self.big_dictionary = self.next_letter_frequencies()
        self.two_letter_big_dictionary = self.more_letter_frequencies()
        self.letters_sorted_by_frequency = "eothasinrdluymwfgcbpkvjqxz".upper()
        self.alphabet = self.setUpAlphabet()
        self.rls = [('.', ' '), (". ", self.letters_sorted_by_frequency), (' ', self.alphabet), (None, self.alphabet)]
        self.length_of_rules = 0
        self.set_up_rules()
        self.set_up_rules_for_two_letters()
    def setUpAlphabet(self):
        """Creates an alphabet of every character in the training data to guess if none of the other rules appeal"""
        list_of_alphabet = []
        for x in self.txt:
            if x not in list_of_alphabet:
                list_of_alphabet.append(x)
        return "".join(sorted(list_of_alphabet))
    def next_letter_frequencies(self):
        """Creates a dictionary of letters and then the frequency of the next letter after"""
        r = {}
        #creating a blank dictionary
        for i in range(len(self.guesser_txt)-1):
            #iterating through positions in txt up to the last charcter
            if self.guesser_txt[i] not in r:
                # if the value of txt[i] not in r (i is an integer)
                r[self.guesser_txt[i]] = {}
                #make a new dictionary within the dictionary for that chracter
            next_letter_freqs = r[self.guesser_txt[i]]
            #assings the blank dictionary within the dictionary to next_letter_freqs
            next_letter = self.guesser_txt[i+1]
            #assings value next letter to be the position after the current character
            if next_letter not in next_letter_freqs:
                #if the next letter is not in the dictionary for that letter value...
                next_letter_freqs[next_letter] = 1
                #assing it the value of 1
            else:
                next_letter_freqs[next_letter] = next_letter_freqs[next_letter] + 1
                #if the next letter is already in the dictionary of next letters after the current letter add one to that value
        return r
    def more_letter_frequencies(self):
        """Creates a dictionary of the past two letters in a text and frequency of the next letter after"""
        r = {}
        #creating a blank dictionary
        for i in range(len(self.guesser_txt)-1):
            #iterating through positions in txt up to the last charcter
            if self.guesser_txt[i-2: i] not in r:
                # if the value of txt[i] not in r (i is an integer)
                r[self.guesser_txt[i-2: i]] = {}
                #make a new dictionary within the dictionary for that chracter
            next_letter_freqs = r[self.guesser_txt[i-2: i]]
            #assings the blank dictionary within the dictionary to next_letter_freqs
            next_letter = self.guesser_txt[i+1]
            #assings value next letter to be the position after the current character
            if next_letter not in next_letter_freqs:
                #if the next letter is not in the dictionary for that letter value...
                next_letter_freqs[next_letter] = 1
                #assing it the value of 1
            else:
                next_letter_freqs[next_letter] = next_letter_freqs[next_letter] + 1
                #if the next letter is already in the dictionary of next letters after the current letter add one to that value
        return r
    def set_up_rules(self):
        """Creates tuples to add to the rules and guess for the text were trying to predict"""
        for key in self.big_dictionary:
            string_to_append = ""
            values = self.big_dictionary[key]
            letter_list = sorted(values.keys(), key = lambda x: values[x], reverse = True)
            for letter in letter_list:
                string_to_append += letter
            tuple_to_insert = (key, string_to_append)
            self.rls.insert(1,tuple_to_insert)
        self.length_of_rules = len(self.rls)
    def set_up_rules_for_two_letters(self):
        """Creates rules based on what the past two letters are and what to guess next"""
        for next in self.two_letter_big_dictionary:
            add_on = ""
            more = self.two_letter_big_dictionary[next]
            almost = sorted(more.keys(), key = lambda x: more[x], reverse = True)
            closer = almost[:15]
            for lets in almost:
                add_on += lets
            tuple_to_insert = (next, add_on)
            self.rls.insert(self.length_of_rules, tuple_to_insert)
    

    def guesser(self, prev_txt):
        """Guesser function to be used in the performance function to create a string of guesses for the performance function to try"""
        all_guesses = ""
        for (suffix, guesses) in self.rls:
                # if len(str(suffix) == 1:
                        try:
                            if suffix == None or prev_txt[-len(suffix):] == suffix:
                                all_guesses += guesses
                        except:
                            #error because not enough characters in prev_txt    
                            pass
                # elif len(str(suffix) == 2:

                # else:


        return all_guesses

    def performance(self):
        """Shannon Guesser function for how accurate our training data was"""
        tot = 0
        #begins the accumulation
        for i in range(len(self.txt)-1):
            #iterate through the lenght of txt up to last character
            #print txt[:i+1]
            #print txt[:]
            to_try = self.guesser(self.txt[:i+1])
            #using the guesser function to see if the previous letters used tell us what to guess based on the list rules
            guess_count = to_try.index(self.txt[i+1])
            #Creates an integer for the index of the next letter of txt to iterate if a guess is possible by passing through the guesser function
            tot = tot + guess_count
            #Accumulates the total amount of guesses
        print "%d characters to guess\t%d guesses\t%.2f guesses per character, on average\n" % (len(self.txt) -1, tot, float(tot)/(len(self.txt) -1))
        #prints how many characters to guess in the text, #the total amount of guesses needed to correctly predict the txt, and the average amount of guesses needed per charcter


    def most_freq_return(self):
        """Returns a numerical instead of a string value in a dictionary"""
        if type(self.txt) == type({}):
            keys = self.txt.keys()
            first = keys[0]
            for b in keys:
                if self.txt[b] > self.txt[first]:
                    first = b
        return first
def promptUser():
        typeOfFile = ""
        firstTry = True
        firstChoicefirstTry = True
        first_choice = 0
        while first_choice != 1 and first_choice != 2:
            if firstChoicefirstTry:
                firstChoicefirstTry = False
            else:
                print "You must enter a 1 or a 2"
            first_choice = int(raw_input("Press 1 and Enter if you would like to enter your own text. Press 2 if you would like to use text from a file.\n\n"))
        if first_choice == 2:
            while typeOfFile != "CSV" and typeOfFile != "TXT" and typeOfFile != "csv" and typeOfFile != "txt":
                if firstTry:
                    firstTry = False
                else:
                    print "You must enter CSV or TXT"
                typeOfFile = raw_input("Please type the file extension of the file you would like to use: CSV or TXT\n\n")
            nameOfTextFile = raw_input("Please give me the name of a file.\n\n")
            text_to_guess = ""
            if nameOfTextFile.find("csv") == -1 and nameOfTextFile.find("txt") == -1:
                if typeOfFile.lower() == "csv":
                    opened =  open(nameOfTextFile+".csv", "rU")
                    text_to_guess = opened.read()
                elif typeOfFile.lower() == "txt":
                    opened = open(nameOfTextFile+".txt", "r")
                    text_to_guess = opened.read()
            else:
                opened = open(nameOfTextFile, "r")
                text_to_guess = opened.read()
        else:
            text_to_guess = raw_input("Please enter the text you want guessed.\n\n")
        return text_to_guess

def RuleMaker():
    filelib = ""
    firstTry = True
    firstChoicefirstTry = True
    first_choice = 0
    while first_choice != 1 and first_choice != 2:
        if firstChoicefirstTry:
            firstChoicefirstTry = False
        else:
            print "You must enter a 1 or a 2"
        first_choice = int(raw_input(" Now well make the rules! Press 1 if you would like to use your own text or file. Press 2 if you would like to use a file from our library to make your predictive text\n\n"))
        if first_choice == 2:
            text_to_choose = raw_input("Enter (t) for a CSV of text messages\nEnter (totc) for a Tale of Two Cities\n Enter (w) for The Wizard of Oz\n Enter (b) to use a Biology Textbook\n Enter (4) for the novel I am Number Four\nEnter (g) for The Great Gatsby in Spanish\n\n")
            text_to_choose =text_to_choose.lower()
            if text_to_choose == "t":
                message = open("SItextmessages.csv", "rU")
                rules = message.read()
            if text_to_choose == "totc":
                book = open("Tale of Two Cities.txt", "r")
                rules = book.read()
            if text_to_choose == "w":
                play = open("Wizard of Oz.txt", "r")
                rules = play.read()
            if text_to_choose == "b":
                textbook = open("Biology Textbook.txt", "r")
                rules = textbook.read()
            if text_to_choose == "4":
                novel = open("I am Number Four.txt", "r")
                rules = novel.read()
            if text_to_choose == "g":
                spanish = open("El Gran Gatsby.txt", "r")
                rules = spanish.read()
        if first_choice == 1:
            typeOfFile = ""
            secondTry = True
            secondChoicesecondTry = True
            second_choice = 0
            while second_choice != 1 and second_choice != 2:
                if secondChoicesecondTry:
                    secondChoicesecondTry = False
                else:
                    print "You must enter a 1 or a 2"
                second_choice = int(raw_input("You've chosen to use your own text or file! Press 1 and Enter if you would like to make rules from your own text. Press 2 if you would like to use text from a file.\n\n"))
            if second_choice == 2:
                while typeOfFile != "CSV" and typeOfFile != "TXT" and typeOfFile != "csv" and typeOfFile != "txt":
                    if secondTry:
                        secondTry = False
                    else:
                        print "You must enter CSV or TXT"
                    typeOfFile = raw_input("Please type the file extension of the file you would like to use: CSV or TXT (Make sure the file you choose is in the same directory)\n\n")
                nameOfTextFile = raw_input("Please give me the name of a file.\n\n")
                if nameOfTextFile.find("csv") == -1 and nameOfTextFile.find("txt") == -1:
                    if typeOfFile.lower() == "csv":
                        csv_file =  open(nameOfTextFile+".csv", "rU")
                        rules = csv_file.read()
                    elif typeOfFile.lower() == "txt":
                        txt_file = open(nameOfTextFile+".txt", "r")
                        rules = txt_file.read()
                else:
                    opened = open(nameOfTextFile, "r")
                    rules = opened.read()
            else:
                rules = raw_input("Please enter the text you want to make your rules from.\n\n")
    return rules

    # original = file('SItextmessages.csv', 'rU')

    # CSV = csv.reader(original)
    # # #print(CSV )
    # # texts = ""
    # # for row in orange:
    # #     texts += row[3] + "\n"





text = promptUser()
rules_text = RuleMaker()


print "\n\nInitializing the TextInformation class and the methods you can use it for" +'\n\n'
First_Instance = TextInformation(text)
First_Instance.top_five()
First_Instance.most_freqs_word()
First_Instance.most_freqs_lets()
First_Instance.word_count('test')

print "\n\nTime to see the accuracy of our Shannon Game Guesser" +'\n\n'
gameInstance = ShannonGameGuesser(text, rules_text)
gameInstance.performance()


print "That's the end of my project, hope you enjoyed it! If you would like to see a variance in accuracy of the guesser, simply change the position of the two letter rules and the initial rules created. Oddly enough, the two letter guesser is not very accurate."


Practice_Instance = TextInformation("This is a test string for my SI 106 final project. Let's see what TextInformation we can find out")
Testing_Instance = ShannonGameGuesser("This is a test string for my SI 106 final project. Let's see what TextInformation we can find out", rules_text)
test.testEqual(type(Practice_Instance.top_five()), type(Practice_Instance.word_count('Hey')))
test.testEqual(type(Testing_Instance.performance()), type(Practice_Instance.most_freqs_lets()))
test.testEqual(type(Practice_Instance.most_freqs_word), type(Testing_Instance.performance))








