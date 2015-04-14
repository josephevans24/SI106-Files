#1)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#accum = 0
#for w in nums:
   #accum = accum + w
#print accum
#this is original problem for first problem on page Accumulator Pattern
#below is my replacement code
fixed = reduce(lambda x, y: x + y, nums)
print fixed
#2)
lp = ["hello","arachnophobia","lamplighter","inspirations","ice","amalgamation","programming","Python"]

#for charac in lp:
    #print len(charac)
#This was string accumulation for the length of characters its PS 4 Question 2
new = [len(value) for value in lp]
print new
#3)
items = ["whirring", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
#acc_num = 0
#for a in items:
    #if 'w' in a:
        #acc_num = acc_num + 1
#print acc_num
#This was the original code for PS 4 Question 3 to determine the amount of words in the list with the letter w
brand = filter(lambda num: 'w' in num, items)
print len(brand)


# Write code to print the length of the list fancy_tomatoes. This was on Activities 3/1 problem 7

#4)
dcm = [9, 4, 67, 89, 98324, 23, 34, 67, 89, 34, 56, 67, 90, 3242, 9893, 5]
# add 14 to each element of the list dcm and print the result
#This was problem 2 on activities through 3/1
laugh = map((lambda x: x+14), dcm)
print laugh

#5)
#t_count = 0 #initialize the accumulator variable
#s_count = 0 # initialize the s counter accumulator as well
#for c in txt:
   #if c == 't':
      #t_count = t_count + 1   #increment the t counter
   #elif c == 's':
      #s_count = s_count + 1

#This is in the accumulating dictionary section of the textbook, on the first page, the first problem. We need a file name that is only in our book, so used the file nested.txt as an alternative
string = open('nested.txt', 'r')
t = filter(lambda x: 't' in x, string)
t_count = len(t)
print t_count
s = filter(lambda x: 's' in x, string)
s_count = len(s)
print s_count





