import test106 as test

### PROBLEM 1.
# We have provided test cases for the first function, as an example. 
# Write at least two test cases each for the next three functions

def letter_freqs(word_list):
    letter_freq_dict = {}
    for w in word_list:
        for l in w:
            if l not in letter_freq_dict:
                letter_freq_dict[l] = 1
            else:
                letter_freq_dict[l] = letter_freq_dict[l] + 1
    return letter_freq_dict

test.testEqual(type(letter_freqs(["hello", "goodbye"])), type({}))
test.testEqual(letter_freqs(["good", "bad", "indifferent"]), {'a': 1, 'b': 1, 'e': 2, 'd': 3, 'g': 1, 'f': 2, 'i': 2, 'o': 2, 'n': 2, 'r': 1, 't': 1})
test.testEqual(letter_freqs(["good"]), {'g':1, 'o':2, 'd':1})
test.testEqual(letter_freqs([]), {})
    
def key_with_biggest_value(diction):    
    most_freq_letter = diction.keys()[0]
    for item in diction.keys():
        if diction[item] > diction[most_freq_letter]:
            most_freq_letter = item
    return most_freq_letter

test.testEqual(key_with_biggest_value({'hi': 2, 'good': 4, 'bye': 3, 'hi': 6}), 'hi')
test.testEqual(type(key_with_biggest_value({'hi': 2, 'good': 4, 'bye': 3, 'hi': 6})), type(""))   


def most_frequest_letter(word_list):
    return key_with_biggest_value(letter_freqs(word_list))
a = 'hhbbzzz'
b = 'hhbbzzzh'
test.testEqual(most_frequest_letter(['hi', 'bye', 'why', 'cry', 'hi']), 'h')
test.testEqual(most_frequest_letter(a), 'z')
test.testEqual(most_frequest_letter(b), 'h')

def popular_keys(diction):
    pop_keys = []
    for k in diction:
        if diction[k] > 3:
            pop_keys.append(k)
    return pop_keys
di = {'hi': 2, 'hello': 4, "bye": 1, "hello": 6, 'hi': 2}
test.testEqual(popular_keys(di), ['hello'])
test.testEqual(type(popular_keys(di)), type([]))
### PROBLEM 2. 
#Define test cases for the Car class below that will make you confident that all three of the methods are operating correctly. 
#For each of your tests, include a comment stating whether it's a return-value test or a side-effect test. 

# (Note: we never showed any examples in class of explicitly calling the __str__ method, but you can. 
    # If x is an instance of the class Car, x.__str__() can be invoked just as x.move_forward() can. 
    # Indeed, __init__ can also be invoked this way, too, but in practice you would not want do it; __init__ gets called automatically when a new instance is created, and that's normally the only time it gets called.)
    
class Car:
    def __init__(self,color,wheels=4,size="compact",make="None"):
        self.color = color
        self.wheels = wheels
        self.size = size
        self.make = make
        self.wheels_with_uhaul = wheels + 4
        self.dist_from_origin = 0.0

    def __str__(self):
        s = "A %s car:\n" % (self.color)
        if self.make:
            s = s + "Make: %s\n" % (str(self.make))
        s = s + "Has %d wheels\n" % (self.wheels)
        s = s + "Current distance from origin: %.02f miles" % (self.dist_from_origin)
        return s

    def move_forward(self,miles=1):
        self.dist_from_origin = self.dist_from_origin + miles
        return "Moved forward %.02f miles" % (miles)

p = Car(make = "Chevy", color = "blue")
#return value test
test.testEqual(p.color, 'blue')
#Return value Test
test.testEqual(p.wheels, 4)
#Return Value Test
test.testEqual(p.move_forward(80.245), "Moved forward 80.25 miles")
#Return Value Test
test.testEqual(p.move_forward(76.834), "Moved forward 76.83 miles")
#Return Value Test
test.testEqual(type(p.move_forward(7)), type(''))
#Return value test
test.testEqual(p.__str__(), 'A blue car:\nMake: Chevy\nHas 4 wheels\nCurrent distance from origin: 164.08 miles')
#Return Value test
test.testEqual(type(p.__str__), type(p.move_forward))
#Return value test



