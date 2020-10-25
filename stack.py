# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# YOUR NAME

class Stack:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def pop(self):
        raise IndexError

    def peek(self):
        raise IndexError

    def push(self, value):
        self.data.append(value)
