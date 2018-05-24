# Cracking the coding interview problem 3.4
# Implement a queue, MyQueue class using two stacks


# Implementation of Stack Class
class Stack (object):
  def __init__ (self):
    self.stack = []

  def push (self, item):
    self.stack.insert (0, item )

  def pop (self):
    return self.stack.pop(0)

  def peek (self):
    return self.stack[0]

  def isEmpty (self):
    return (len(self.stack) == 0)

# -----------------------My anser begins here-------------------------------
# Here is one solution in which the enqueue works by pushing new values to stack1 as a normal stack would.
# When dequeue is called, the queue length is immediately reduced so that all of stack1 can be popped and pushed onto
# stack2, except for the last value, which is popped and returned. Before returning, all of stack2 is popped and pushed back
# onto stack1 to keep stack1 in the traditional first in last out structure and keep enqueue O(1). The reverse could be done to make dequeue O(1)
class myQueue1():
  def __init__(self):
    self.stack1 = Stack()
    self.stack2 = Stack()
    self.queueLength = 0

  def enqueue(self, item):
    self.queueLength += 1
    self.stack1.push(item)
      

  def dequeue(self):
    if self.queueLength == 0:
      raise ValueError('No elements in Queue to dequeue')
    self.queueLength -=1
    for elements in range(self.queueLength):
        self.stack2.push(self.stack1.pop())
    dequeued = self.stack1.pop()
    for elements in range(self.queueLength):
        self.stack1.push(self.stack2.pop())
    return dequeued
      


# As an alternative approach, instead of choosing between an enqueue or dequeue of O(1), you can choose not to undo the reversal as done in 
# dequeue of the top solution. Instead, the first time dequeue is needed, keep stack1 empty and stack2 reverse so that the next time dequeue is called
# it will be O(1). However, once enqueue is called again, stack2 will need to be popped into stack1 to unreverse it. This will cycle between O(1) each time 
# dequeue is called after enqueue and vice versa.
class myQueue2():
  def __init__(self):
    self.stack1 = Stack()
    self.stack2 = Stack()
    self.stackReversed = False
    self.queueLength = 0

  def enqueue(self, item):
    if self.queueLength == 0:
      self.stack1.push(item)
    elif not self.stackReversed:
      self.stack1.push(item)
    else:
      for elements in range(self.queueLength):
        self.stack1.push(self.stack2.pop())
      self.stack1.push(item)
      self.stackReversed = False
    self.queueLength += 1

  def dequeue(self):
    if self.queueLength == 0:
      raise ValueError('No elements in Queue to dequeue')
    elif not self.stackReversed:
      for elements in range(self.queueLength-1):
        self.stack2.push(self.stack1.pop())
      self.queueLength -=1
      self.stackReversed = True
      return self.stack1.pop()
      
    else:
      self.queueLength -=1
      return self.stack2.pop()

# Testing to see that each works as expected
def main():
  myList = [12,4,5,6,8]
  s = Stack()
  q1 = myQueue1()
  q2 = myQueue2()
  for numbers in myList:
    s.push(numbers)
    q1.enqueue(numbers)
    q2.enqueue(numbers)
  for numbers in myList:
    print("Stack: ")
    print(s.pop())
    print("Queue: ")
    print(q1.dequeue())
    print(q2.dequeue())

main()
