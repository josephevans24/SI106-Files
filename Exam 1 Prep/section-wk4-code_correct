# section week 4 code

# this code has errors -- where?
# how would you fix them?
# think about the debugging strategies!

# you can assume that you have access to the functions
# square
# &
# random_digit
import random
def random_digit():
	return random.choice(range(9))

def square(i):
	return i*i


abc = 6 + 7

x = 5 == 4

if x == True:
	print "This should not print"

avocado = [abc, x, "antidisestablishmentarianism", 8.0, False, True, [abc,x,3]]

#for guac in avocado # error -- no colon here
for guac in avocado:
	print type(guac)
	print type("hello")

#fd = abc + x # error (you can't add these -- why?)
fd = abc + 4 # any number

#cb = avocado + 4 # error (need to: make 4 a list, append 4)
cb = avocado + [4] # one possibility
cb = avocado.append(4) # another

#for y in len(avocado[2]): # error - make the integer a range(int)
for y in range(len(avocado)):
	print y

srt = "An-ti-dis-est-ab-lish-ment-ar-i-an-is-m"
# we want to get a list with all the syllables as strings, no -s
#syll_list = split(srt) # error - need to call split correctly with "-" input
syll_list = srt.split("-")

f = "supercalifragilistic"
for l in f:
	print l

if abc > 6:
	check_size = True
else:
	check_size = False

print check_size

b = "this section is by far the mostest, best"
#print b.append("est") # error - can't append to a string, must concatenate
print b + "est"

# Below this line, the code will not run in your scratch window,
# because we have not supplied you with the functions we
# described in the problem set. HOWEVER, you could try running it
# in the problem set windows where the code IS provided, if you
# want to test it --
# you just won't be able to save it.

z = random_digit()
#n = random_digit(4) # error - random digit does not take any inputs
n = random_digit()
m = square(z)
print m


