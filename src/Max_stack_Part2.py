"""
You've encountered a situation where you want to easily be able to pull the
largest integer from a stack.

You already have a `Stack` class that you've implemented using a dynamic array.

Use this `Stack` class to implement a new class `MaxStack` with a method
`get_max()` that returns the largest element in the stack. `get_max()` should
not remove the item.

*Note: Your stacks will contain only integers. You should be able to get a
runtime of O(1) for push(), pop(), and get_max().*
"""
class Stack:  # Only want to use push, peek and pop in stacks. 
           # Peek returns last elemeent, would have to pop everything off to get peek.
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack:             # Max is the maximum value inside the stack
    def __init__(self):
        # Your code here
        self.stack = Stack()
        self.max_stack = Stack()
        self.max = None


    def push(self, item):
        # 0(1)
        """Add a new item onto the top of our stack."""
        # Your code here
        self.stack.push(item)
        # update max if necessary
        # if self.max is None or self.max < item:
        #     self.max = item
        # get the current max, compate it to item, and if current max < item, new max - item
        current_max = self.get_max()
        if current_max is None or current_max < item:
            current_max = item
        # push the max onto max_stack
        self.max_stack.push(current_max)

    def pop(self):
        # O(1)
        """Remove and return the top item from our stack."""
        # Your code here
        item = self.stack.pop()         # O(1)
        # check if we're removing the max
        #if item == max:             #O(1)
            # if so, we need to update self. max
            #new_max = self.find_max()  # O(n)      # Don't need find anymore
            # self.max = new_max          #O(1)
            # self.max = item
        #return self.stack.pop()
        self.max_stack.pop()
        return item



    def get_max(self):
        # 0(1)
        """The last item in maxex_stack is the max item in our stack. """
        return self.max_stack.peek()

        # Don't need find_max we returned max_stack.peek()
        
    # def find_max(self):
    #     # O(n)

    #     # Your code here
    #     # approach 1; pop everything off, find the max, and push it back on.
    #     # trick; when we push it back on, we want everything to stay in the same order.

    #     values = []
    #     element = self.stack.pop()
    #     cur_max = None
    #     while element is not None:
    #         values.append(element)
    #         if cur_max is None or cur_max < element:
    #             cur_max = element
    #         element = self.stack.pop()

    #     # loop
    #     for i in range(len(values) -1, -1, -1):
    #         # start with i = len(values -1), go up to (but not including) i= -1, drementi by -1 on each loop
    #         # for (int i = len(values) -1, i> -1; i--) - JS
    #         element = values[i]
    #         self.push(element)
        
    #     return cur_max

        #stack: 1, 2, 3
        #values = [3, 2, 1], stack = []


max_stack = MaxStack()
max_stack.push(1)           # stack: 1, max_stack = 1
max_stack.push(2)           # stack: 1, 2 max_stack = 1, 2
max_stack.push(3)           # stack: 1, 2, 3 max_stack = 1, 2, 3
max = max_stack.get_max()
print(max == 3)

max_stack.pop()             # stack: 1, 2 max_stack = 1, 2, 3
print(max_stack.get_max() == 2)

max_stack.push(0)           # stack: 1, 2, 0 max = 1, 2, 2
print(max_stack.get_max() == 2)
max_stack.pop()             # stack: 1, 2 max_stack = 1, 2, 3

# STACK 1, 2, 3 (pop() removes the 3)
            # (push(0)) adds 0 to the end max_stack.get_max() still returns 2. highest value