# Problem 1.2 - Given two strings, write a method
# to decide if one is a permutation of the other

def isPermutation(s1,s2):
	# The set check could alternatively be performed in the second loop
	# by checking for a character not in the dictionary and returning false immediately 
	if len(s1) != len(s2) or set(s1) != set(s2):
		return False
	d = {}
	# Populate the dictionary
	for char in s1:
		if not char in d:
			d[char] = 1
		else:
			d[char] += 1
	# Subtract value associated with each key
	for char in s2:
		d[char] -= 1
		# If a value is less than zero it is not a permutation
		if d[char] < 0:
			return False 
	return True 

def main():
	s1 = "jeededd"
	s2 = "dddeejd"
	print(isPermutation(s1,s2))
main()