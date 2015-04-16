import test106 as test
import csv
# 1) Add a rule for past two letters and another for end of sentence and space
# 2) Turn it all into two separate classes
# 4) How do I get \x out?
# 3) Make multiple versions showing guessing getting lower

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

def most_freqs_lets(txt):
    if type(txt) == type(""):
        dem = {}
        split = collapse_whitespace(txt)
        for a in split:
            if a not in dem:
                dem[a] = 1
            else:
                dem[a] += 1
        keys = dem.keys()
        first = keys[0]
        for b in keys:
            if dem[b] > dem[first]:
                first = b
    elif type(txt) == type([]):
        dem = {}
        for a in txt:
            for b in a:
                if b not in dem:
                    dem[b] = 1
                else:
                    dem[b] += 1
        keys = dem.keys()
        first = keys[0]
        for c in keys:
            if dem[c] > dem[first]:
                first = b
        return "%s occurs %d times" % (first, dem[first])
    elif type(txt) == type({}):
        keys = txt.keys()
        first = keys[0]
        for b in keys:
            if txt[b] > txt[first]:
                first = b
    return "%s occurs %d times" % (first, txt[first])
def most_freqs_word(txt):
    if type(txt) == type([]):
        dem = {}
        for a in txt:
            if a not in dem:
                dem[a] = 1
            else:
                dem[a] += 1
        keys = dem.keys()
        first = keys[0]
        for b in keys:
            if dem[b] > dem[first]:
                first = b
        return "%s occurs %d times" % (first, dem[first])
    elif type(txt) == type(""):
        dem = {}
        split = txt.split()
        for a in split:
            if a not in dem:
                dem[a] = 1
            else:
                dem[a] += 1
        keys = dem.keys()
        first = keys[0]
        for b in keys:
            if dem[b] > dem[first]:
                first = b
        return "%s occurs %d times" % (first, dem[first])
    elif type(txt) == type({}):
        keys = txt.keys()
        first = keys[0]
        for b in keys:
            if txt[b] > txt[first]:
                first = b
        return "%s occurs %s times" % (first, txt[first])
    return "Can't get the most frequent word"

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
def word_count(txt, name):
    accum = 0
    count_it = txt.split()
    for a in count_it:
        if name in a:
            accum += 1
    return "%s occurs %d times" % (name, accum)
def top_five(txt):
    dem = {}
    banana = txt.split()
    for a in banana:
        if a not in dem:
            dem[a] = 1
        else:
            dem[a] += 1
    going = sorted(dem.keys(), key = lambda x: dem[x], reverse = True)
    return going, "For this file the top five most used words are: %s" % (going[:5])

def most_freq_return(txt):
    """Returns a numerical instead of a string value in a dictionary"""
    if type(txt) == type({}):
        keys = txt.keys()
        first = keys[0]
        for b in keys:
            if txt[b] > txt[first]:
                first = b
    return first


original = file('SItextmessages.csv', 'rU')

orange = csv.reader(original)
#print(orange)
texts = ""
for row in orange:
    texts += row[3] + "\n"

#texts = cool.replace('!', " ").replace('.', ' ').replace(':', ' ').replace(',', ' ').replace('?', ' ').replace("/", ' ').replace('\\', ' ')
lsttexts = texts.split()
nospaces = collapse_whitespace(texts)
#print nospaces

#print word_count(texts, 'hey')

#adding comment for github
lets = []
for x in texts:
    if x not in lets:
        lets.append(x)
alphabet = "".join(sorted(lets))
# print alphabet
pink = next_letter_frequencies(texts)
rule2 = next_letter_frequencies(lsttexts)



# for deep in lsttexts:
#     for deeper in range(len(deep)-1):
#         next = deep[deeper+1]
#         if next == next.upper():
#             lsttexts.insert((deeper+1), ' ')

#print most_freqs_lets(red)
#print most_freqs_lets(nospaces)
#print most_freqs_lets(lsttexts)
# print most_freqs_word(texts)
# print most_freqs_word(lsttexts)

# test.testEqual(most_freqs_word({'hi': 4, 'bye': 8, 'sup': 3}), ('bye', 'occurs', 8, 'times'))
# test.testEqual(most_freqs_word('hey buddy how are ya buddy'), ('buddy', 'occurs', 2, 'times'))
# test.testEqual(most_freqs_word(['hi', 'hey', 'bye', 'hi']), ('hi', 'occurs', 2, 'times'))
# test.testEqual(most_freqs_lets('hey buddy whats going on today'), ('d', 'occurs', 3, 'times'))
# test.testEqual(most_freqs_lets(['this', 'day', 'has', 'taken', 'its toll']), ('l', 'occurs', 2, 'times'))
rules = [(".", 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), (' ', alphabet), (None, alphabet)]
performance('These days they go by so fast. Nothing I can do about it', rules)


for key in pink:
    string_to_append = ""
    values = pink[key]
    fix = sorted(values.keys(), key = lambda x: values[x], reverse = True)
    for letter in fix:
        string_to_append += letter
    tuple_to_insert = (key, string_to_append)
    rules.insert(0,tuple_to_insert)

print '----------------------'

# performance('These days they go by so fast. Nothing I can do about it', rules)
# performance('Joey, what the fuck are you doing', rules)
# performance('LeBron James for NBA MVP? Here are seven games that make a great case for the Cleveland Cavaliers star. His talent is simply off the chart. I have never seen a guy who is as talented as LeBron, his raw ability is astonishing.', rules)
performance("What the hell are you doing? I mean this has been fun, but it's crazy that you're thinking about this to begin with.", rules)

please = []
thanks = []
for a in rule2.keys():
        please.append(a)
for b in rule2.values():
     kumar = most_freq_return(b)
     thanks.append(kumar)
doit = zip(please, thanks)
for i in doit:
    rules.insert(1,i)

# print rules[83030]
# performance('Hey man hows it hanging.', rules)












