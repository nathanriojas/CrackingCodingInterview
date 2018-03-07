#Return Kth to Last Element of a singly linked list

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


#                                      ACTUAL ANSWER

# Using the Linked List class above / assuming the above class methods
# Assumptions: there is at least one link before and afer the input link
def deleteMiddle(InputLink):
	# 6
	current = InputLink
	# next
	#InputLink.next = InputLink.next.next
	InputLink.data = current.next.data
	InputLink.next = current.next.next







def main():

 	newList = LinkedList()
 	for i in range (1,11):
 		newList.insertLast(i)
 	testLink = newList.first
 	for i in range(5):
 		testLink = testLink.next
 	print("Test link to delete is " + str(testLink.data))
 	print(newList)
 	deleteMiddle(testLink)
 	print(newList)



main()
