# write a function to check if a linked list is a palindrome

# Linked List Class I use
class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class LinkedList (object):
  def __init__ (self):
    self.first = None

  def insertFirst (self, data):
    newLink = Link (data)
    newLink.next = self.first
    self.first = newLink

  def insertLast (self, data):
    newLink = Link (data)
    current = self.first

    if (current == None):
      self.first = newLink
      return

    while (current.next != None):
      current = current.next

    current.next = newLink

  def __str__ (self):
  	lstring = ""
  	current = self.first
  	while current != None:
  		lstring = lstring + str(current.data)
  		current = current.next
  	return lstring

# take a string and make it into a linked list
def stringToList(st):
	stringList = LinkedList()
	for letter in st:
		stringList.insertLast(letter)
	return stringList








# --------------------Actual Answer-------------------------


# continuously check if the list is a palindrome until there are no more links
# change data to string, have two strings to compare
def isPalindrome(LL):
	if LL.first == None:
		return None
	current = LL.first
	firstHalf = ""
	secondHalf = ""
	while current != None:
		firstHalf = firstHalf + str(current.data)
		secondHalf = str(current.data) + secondHalf
		current = current.next
	return firstHalf == secondHalf






def main():
	st1 = "hello world"
	st2 = "arggra"
	st3 = "123454321"
	st4 = "1"
	L1 = stringToList(st1)
	L2 = stringToList(st2)
	L3 = stringToList(st3)
	L4 = stringToList(st4)
	print(isPalindrome(L1))
	print(isPalindrome(L2))
	print(isPalindrome(L3))
	print(isPalindrome(L4))
main()



















