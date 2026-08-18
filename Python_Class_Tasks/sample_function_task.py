#function introduction

#Every function should take in something throught the parameter and print something through the return type

#def stands for define

#parameters that are not used should'nt be specified

def count_vowel(word): #This is a parameter. it is also a placeholder

	vowel_sample = "aeiou"

	counter = 0

	word = word.lower()

	for letter in word:

		if letter in vowel_sample:

			counter = counter + 1

	return counter

	#print(word)

	#print(word * 2)

	#return word * 2 #The return statement wouldn't print because it wasn't assigned to a variable

	#print(word * 3)

	#yield word * 3

	#Anything not printed wouldn't return anything

	#return always marks the end of the function. if there's a print statement after the return, nothing happens
	#That would be the end of the method.

	#To print after a return statement, keyword yield is used

	#There are  types of arguments



print(count_vowel("Maraiam")) #"Mariam here is an argument"

#A function shouldn't be called in the indentation block in the function. It should be called outside the function. If called, it would result in a recursion.

def count_consonant(word):

	vowel_sample = "aeiou"

	word = word.lower()

	counter = 0

	for letter in word:

		if letter not in vowel_sample:

			counter = counter + 1

	return counter


print(count_consonant("Arequiation"))


def count_space(word):

	counter = 0
	
	for character in word:

		if character == " ":

			counter = counter + 1


	return counter 


print(count_space("There isn't money anymore"))


def count_symbol(word):

	counter = 0

	for letter in word:

		if letter == "_": #The identifier doesn't exclude numbers

			counter = counter + 1

		elif not letter.isidentifier() and not letter.isspace() and not letter.isdigit():

			counter = counter + 1

	return counter

print(count_symbol("matter8@#__"))