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









# ----------------For lists representing numbers in reverse order--------------

def sumLists(L1,L2):
  if L1.first == None or L2.first == None:
      return None
  L3 = LinkedList()
  current1 = L1.first
  current2 = L2.first
  sumNode = 0
  while current1 != None and current2 != None:
    if current1 == None:
      sumNode += current2
    elif current2 == None:
      sumNode += current1
    else:
      sumNode += current1 + current2
    if sumNode >= 10:
      



