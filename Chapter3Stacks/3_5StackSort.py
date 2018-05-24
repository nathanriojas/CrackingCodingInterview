# Cracking the coding interview problem 3.5 - Sort a stack, use of temporary
# stack (I am using two temporary stacks) allowed. Cannot store in any other data structure.
# Only push, pop, peek, and isEmpty are available


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

# Here is where my solution begins

def sortStack(original):
  if original.isEmpty() == True:
    return original
  # Create two temporary stacks, one for the sorting, one for holding the values temporarily
  sortedStack = Stack()
  tempStack = Stack()
  sortedStack.push(original.pop())
  # Set the minimum as the first value of the original stack
  minS = sortedStack.peek()
  while not original.isEmpty():
    # The value is less than or equal to the min
    if original.peek() <= minS:
      minS = original.peek()
      sortedStack.push(original.pop())
    else:
      # Pop values from the sorted stack until the current value from the orignal stack is less than 
      # the top value of the sorted stack
      count = 0
      while not sortedStack.isEmpty() and original.peek() > sortedStack.peek():
        tempStack.push(sortedStack.pop())
        count += 1
      # Pop the original stack value in the sorted stack
      sortedStack.push(original.pop())
      # Take the values in the temporary stack and place them back into the sorted stack
      for values in range(count):
        original.push(tempStack.pop())
      for values in range(count):
        sortedStack.push(sortedStack.pop())
  return sortedStack

# Demo of solution
def main():

  stackList = [99,3,7,4,9,1,10,13,5]
  inputStack = Stack()
  for number in stackList:
    inputStack.push(number)
  inputStack = sortStack(inputStack)
  for number in stackList:
    print(inputStack.pop())

main()
