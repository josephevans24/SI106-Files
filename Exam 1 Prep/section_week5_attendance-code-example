# The following is code that solves all the problems we were 'faced with'
# in section, week 5, writing a toy attendance program. Except it's in a real Python file!

# Our suggestion is that you look through this code, run it, make sure you understand
# all of it. Look away and try to write it yourself. If this makes sense, and you can
# recreate it after thinking about it for a while, you're in really good shape.

#######

# this is the original dictionary we started with
class_meetings = {"morning section":14,"afternoon section":16,"evening section":9,"monday lecture":96}

# add a key for wednesday lecture with attendance value of 100
class_meetings["wednesday lecture"] = 100

# add three to the attendance value of the key for the evening section
class_meetings["evening section"] = class_meetings["evening section"] + 3

meeting_keys = class_meetings.keys()

total = 0 # set the accumlator in order to find the sum of all attendance values

smallest_so_far = meeting_keys[0] # set the smallest value to get the smallest so far

# doing this all in the same loop is hard, but any way that works OK is fine!
# think about how you might begin to write some of this code and keep editing it
# to do all the things that you want it to do...
for k in meeting_keys:
	print k, "attendance:", class_meetings[k] # or could do this using string concatenation, coercing the key value into a string
	total = total + class_meetings[k] # accum step
	if class_meetings[k] > smallest_so_far # find least attendance step
		smallest_so_far = k

# remainder of print statements to print out the results of using the accum. pattern
print "Total of values:", total # or using string concat, etc
print "The meeting with the smallest attendance is:", smallest_so_far

# Code for finding the total attendance in any SECTION, no lecture
total_section_att = 0
for k in meeting_keys:
	if "section" in k:
		total_section_att = total_section_att + class_meetings[k]
	# no need for an else, because you only care if section IS in the key
# now we're done with the for loop, so we can 'outdent'
print "The total section attendance this week was", total_section_att
