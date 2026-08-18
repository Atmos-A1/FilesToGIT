sentence = input("Enter a sentence: ")

vowel_counter = 0

consonant_counter = 0

space_counter = 0

lower_case_counter = 0

upper_case_counter = 0

symbols_counter = 0

for character in sentence:
	if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
		vowel_counter = vowel_counter + 1
	else:
		consonant_counter = consonant_counter + 1

for character in sentence:
	if character == " ":
		space_counter = space_counter + 1

for character in sentence:
	if character == '/' or character == '.' or character == ',' or character == '&' or character == '!' or character == "" or character == ':' or character == "'\'" or character == ';':
		symbols_counter = symbols_counter +  1

print(vowel_counter)

print(consonant_counter)

print(space_counter)

print(symbols_counter)