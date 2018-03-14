# given two numbers represented by linked lists where each node is a digit
# sum the two numbers
# Part 1. The numbers are presented in reverse order in the linked lists
# i.e. 617 and 295 are represented as 7->1->6 and 5->9->2
# and their sum should yield a linked list of 2->1->9 which is 912
# Part 2: Repeat part 1 but the digits are in forward order

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


# ----------------Part 1: For lists representing numbers in reverse order--------------
# Note: in reality this is how we add numbers so add each corresponding digit and put the 
# result in the last place of a new linked list.

def sumLists(L1,L2):
  # check that at least one list is not empty
  if L1.first == None and L2.first == None:
      return None
  L3 = LinkedList()
  current1 = L1.first
  current2 = L2.first
  # initialize the variable that will store the sum of two digits
  sumNode = 0
  # break only when both lists are equal to none
  while (current1 != None) or (current2 != None):
    # add the data from corresponding nodes and store in sumNode
    # when one list becomes empty only add the data from the non empty node
    if current1 == None:
      sumNode += current2.data
      current2 = current2.next
    elif current2 == None:
      sumNode += current1.data
      current1 = current1.next
    else:
      sumNode += (current1.data + current2.data)
      current1 = current1.next
      current2 = current2.next
    # insert the sum of the two digits from corresponding nodes as the last element of the new list
    # if this is greater than 10 only add the number from the ones place to the list and carry the 1
    # by setting sumNode to 1 instead of resetting it to 0
    if sumNode >= 10:
      L3.insertLast(sumNode%10)
      sumNode = 1
    else:
      L3.insertLast(sumNode)
      sumNode = 0
  # account for the end of the addition still needing a 1 carried over i.e 999 + 1 -> 1000
  if sumNode != 0:
    L3.insertLast(sumNode)
  return L3

# simple function to comvert a number to linked list for testing
# assume no trick numbers, nulls, etc
def numToList(number):
  number = str(number)
  numList = LinkedList()
  for ints in number:
    numList.insertFirst(int(ints))
  return numList







def main():
  # Choose two numbers here and they will be converted to lists and added
  n1 = 617
  n2 = 295
  L1 = numToList(n1)
  L2 = numToList(n2)
  L3 = sumLists(L1,L2)
  print(L3)

main()


