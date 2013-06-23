# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name:Olha Vasylevska

# move_letter() function moves letter by "move_by" positions and returns a new letter 

def move_letter(letter, move_by):
	start_pos = ord(letter)
	end_pos = start_pos + move_by
	
	if end_pos < 97:
		end_pos = 123 - (97 - end_pos)
	elif end_pos > 122:
		end_pos = 97 + (end_pos - 123)
		
	new_letter = chr(end_pos)
	return new_letter

# rotate_word() function moves every letter in a word by "move_by" positions and returns a new word

def rotate_word(word, move_by):
	new_word = ''
	for i in range(len(word)):
		new_word += move_letter(word[i], move_by)
	print (new_word)

# Examples:

rotate_word('cheer', 7)
rotate_word('melon', -10)
rotate_word('alba', 0)
rotate_word('az', -26)
rotate_word('az', 26)