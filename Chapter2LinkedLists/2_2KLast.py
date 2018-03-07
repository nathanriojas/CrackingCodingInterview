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



#                                      ACTUAL ANSWER

# Depending on how you define Kth to last, switch the for loop to start at 0 or 1
# Ex: if K = 1 should say that 10 is the first last, K = 2 says 9 is second to last, etc. start for loop starts at 1
# Ex: if K = 1 should say that 9 is one away from 10, start for loop at 0

def KToLastElement(inputList, K):
	# Make sure List isn't empty
	if inputList.first == None:
		return None
	# Let this link start at the beginning, it will end K places from the end
	slowerLink = inputList.first
	# Let this link be the runner to find the end, it start K places ahead of the slower link
	fasterLink = inputList.first
	# Need to ensure that the list has at least K elements 
	for links in range (1,K):
		# Not enough elements to have a K from Last
		if fasterLink.next == None:
			return None
		fasterLink = fasterLink.next
	# Find the end of the list
	while fasterLink.next != None:
		slowerLink = slowerLink.next
		fasterLink = fasterLink.next

	return slowerLink.data 







def main():

 	newList = LinkedList()
 	for i in range (1,11):
 		newList.insertLast(i)
 	print(KToLastElement(newList,2))


main()
