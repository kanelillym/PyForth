THE_DICTIONARY = {
    "+": "add",
    ".": "pop",
    ".s": "display_stack",
    "negate": "negate",
    "-": "negate +",
    "(": "comment_begin",
    ")": "comment_end"
}

class Stack:
    def __init__(self):
        self.stack_data = []

    def push(self, val):
        self.stack_data.append(val)

    def pop(self):
        return self.stack_data.pop(-1)

    def top(self):
        return self.stack_data[-1]

    def size(self):
        return len(self.stack_data)
    
    def is_empty(self):
        return self.size() == 0

THE_STACK = Stack()

def dot_pop():
    print(THE_STACK.pop())

def dot_s():
    print(THE_STACK.stack_data, "<- Top")

def add():
    val1 = THE_STACK.pop()
    val2 = THE_STACK.pop()
    THE_STACK.push(val1+val2)

THE_STACK.push(10)
THE_STACK.push(11)
dot_s()
add()
dot_s()
