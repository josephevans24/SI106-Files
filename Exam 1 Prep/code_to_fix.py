# section week 4 code

# this code has errors -- where?
# how would you fix them?
# think about the debugging strategies!

# you can assume that you have access to the functions
# square
# &
# random_digit

abc = 6 + 7

x = 5 == 4
print x #prints False
if x == True:
	print "This should not print"

avocado = [abc, x, "antidisestablishmentarianism", 8.0, False, True, [abc,x,3]]

for guac in avocado: 
	print type(guac)
	print type("hello")

fd = abc + x 

cb = len(avocado) + 4 

for y in range(27): 
	print y

srt = "An-ti-dis-est-ab-lish-ment-ar-i-an-is-m"
# we want to get a list with all the syllables as strings, no -s
syll_list = srt.split('-')
print str(syll_list)

f = "supercalifragilistic"
for l in f:
	print l

if abc > 6:
	check_size = True
else:
	check_size = False

print check_size

b = "this section is by far the mostest, best"
print b+"est"

# Below this line, the code will not run in your scratch window,
# because we have not supplied you with the functions we
# described in the problem set. HOWEVER, you could try running it
# in the problem set windows where the code IS provided, if you
# want to test it --
# you just won't be able to save it.
def random_digit():
    import random
    a = random.choice[0,1,2,3,4,5,6,7,8,9,0]
    return a
def square(x):
    return x**x
z = random_digit()
n = random_digit(4) 
m = square(z)
print m


