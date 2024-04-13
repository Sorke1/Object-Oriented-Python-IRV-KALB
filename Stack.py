class Stack:
    ''' Stack class implements a last in first out LIFO algorithm'''
    def __init__(self, startingStackAsList=None):
        if startingStackAsList is None:
            self.dataList = []
        else:
            self.dataList = startingStackAsList[:]
    
    def push(self, item):
        self.dataList.append(item)
    
    def pop(self):
        if len(self.dataList) == 0:
            raise IndexError("Stack is empty")
        return self.dataList.pop()

    def peek(self):
        if len(self.dataList) == 0:
            raise IndexError("Stack is empty")
        return self.dataList[-1]

    def getSize(self):
        return len(self.dataList)

    def show(self):
        # Show the stack in a vertical orientation
        print('Stack is:')
        for value in reversed(self.dataList):
            print('   ', value)

# Example usage:
my_stack = Stack([1, 2, 3])
my_stack.push(4)
my_stack.show()
print("Popped item:", my_stack.pop())
print("Top item:", my_stack.peek())
print("Size of stack:", my_stack.getSize())
