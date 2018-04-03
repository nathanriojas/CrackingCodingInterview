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

  def removeFirst (self):
    removed = self.first
    self.first.next= self.first.next.next
    self.first = self.first.next
    return removed

# Stack class implemented such that push, pop, and min are O(1)
class Stack (object):
  def __init__ (self):
    self.stack = LinkedList()
    self.minimum = None
  def push (self,data):
    if data < self.minimum:
      self.minimum = data
    self.stack.insertFirst(data)
  def pop (self):
    return self.removeFirst()
  def min (self):
    return self.minimum
