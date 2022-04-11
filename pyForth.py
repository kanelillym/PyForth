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

def eval_word(key_word):
    # if COMMENT_MODE only process comment_end
    if is_number(key_word):
        THE_STACK.push(int(key_word))
    else:
        match key_word.split():
            case ["bye"]:
                bye()
                return
            case [*words]:
               pass
        if key_word in THE_DICTIONARY:
            word_value = THE_DICTIONARY[key_word]
            if len(word_value.split()) == 1:
                word_value.split()[0]()
            else:
                eval_string(word_value)
        else:
            # process undefined word error
            pass

def main():
    print("Welcome to PyForth!")
    while True:
        data = input(">> ")
        data_array = data.split(" ")
        print(data_array)
        for word in data_array:
            eval_word(word)
        match data_array:
            case ['bye']:
                print("byebye!")
                break

main()
