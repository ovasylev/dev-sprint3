# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Olha Vasylevska


# 9.1

# Opens words.txt for reading and prints only words with more than 20 characters 

fin = open('words.txt')
for line in fin:
	word = line.strip()
	if len(word)>20:
		print word


# 9.2

# has_no_e() function returns True for words without letter 'e' in them.

# percent_of_no_e_words() function opens words.txt file for reading 
# and prints percentage of words without letter 'e' in them.

def has_no_e(word):
	for letter in word:
		if letter == 'e':
			return False
	return True
		
def percent_of_no_e_words(file):
	summ = 0
	total = 0

	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		total += 1
		if has_no_e(word):
			summ += 1
			print word
	print summ
	print total
	perc = float(summ)/total *100

	print "This word list contains", str(int(perc)), "% of no 'e' words."

percent_of_no_e_words('words.txt')

# 9.3

# avoids() returns True if the word doesn't use any of the forbidden letters.

# words_without_forbidden_letters() takes a file and prints the number of words 
# in file without forbidden letters.

def avoids(word, string):
	for letter in word:
		for symbol in string:
			if letter == symbol:
				return False
	return True


def words_without_forbidden_letters(file):
	valid_words_count = 0.0

	forbidden = raw_input("Please enter a string of forbidden letters: ")

	fin = open('words.txt')

	for line in fin:
		word = line.strip()
		if avoids(word, forbidden):
			valid_words_count += 1
			#print word

	print "Number of words with no forbidden letter: ", int(valid_words_count)

words_without_forbidden_letters('words.txt')

# 9.4

# uses_only() returns True if the word contains only allowed letters.

def uses_only(word, allowed):
	for letter in word:
		if letter not in allowed:
			return False
		return True

print uses_only('hello', 'acefhlo')