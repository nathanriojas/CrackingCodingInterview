# Cracking the coding interview chapter 1 problem 1: Given a string, determine if each character is unique

# Assuming spaces are not counted
def isUnique(st):
	charSet = [] # hold unique characters
	for char in st: # iterate through each character in string
		if char in charSet and char != " ": # end program if in charSet array
			return False
		charSet.append(char)
	return True
# Alternatively  
'''
def isUnique(st):
	string = st.replace(" ","")
	return len(set(string)) == len(string)
'''

# If no additional data structures are allowed, does not consider white space when determining if unique
'''
def isUnique(st):
  for charCheck in range(len(st)):
    for chars in range (len(st)):
        if charCheck != chars and st[charCheck] == st[chars] and not st[chars].isspace():
          return False
  return True
'''
def main():
	testString = "hello world"
	print(isUnique(testString))
main()
