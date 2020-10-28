# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# YOUR NAME

class Stack:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[len(self.data) - 1]

    def push(self, value):
        self.data.append(value)
