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

def main():
	testString = "hello world"
	print(isUnique(testString))
main()
