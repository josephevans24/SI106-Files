# list of words to classify
list_of_words = ['apple','pear','banana','pepper','cucumber','pepper','basil','orange','pear','apple','pineapple','apple','cucumber','elephant','banana','broccoli','coffee','apple']

# list of fruits for positive classification
list_of_fruits = ['apple','pear','banana','orange','pineapple']

# is_fruit - given word and list of fruits, is word a fruit?
# (remember that you have to INPUT the list of fruit words into the function in order to use it)

def is_fruit(fruit_candidate, fruit_list): # you'll need to change this function
	if fruit_candidate in fruit_list:
		return True
	else:
		return False
print is_fruit('pear', list_of_fruits)

def fruit_count(word_list, fruit_list):
    fruit_count_dictionary = {}
    for b in word_list:
    	if is_fruit(b, fruit_list):
             if b not in fruit_count_dictionary:
                    fruit_count_dictionary[b] = 1
             else:
                 fruit_count_dictionary[b] += 1
    return fruit_count_dictionary
dictionary_of_fruit_counts = fruit_count(list_of_words, list_of_fruits)

print dictionary_of_fruit_counts