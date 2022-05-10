
class MyStack:

    stack = list()

    def __init__(self):
        pass

    def push(self,element):
        self.stack.append(element)
        self.display()

    def pop(self):
        self.stack.pop()
        self.display()

    def is_empty(self):
        if not self.stack:
            return True
        else:
            return False

    def display(self):
        print(self.stack)

    def lenght(self):
        return len(self.stack)

