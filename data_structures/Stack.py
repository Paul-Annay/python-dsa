class Stack:
    def __init__(self):
        self.data = [None] * 10
        self.top = -1
        self.size = self.data.__len__()


    def push(self, val):
        if self.top == self.size - 1:
            self.data.extend([0] * self.size)
            self.size = self.data.__len__()
        self.top += 1
        self.data[self.top] = val

    def pop(self):
        val = None
        if self.top != -1:
            val = self.data[self.top]
            self.data[self.top] = None
            self.top -= 1

        return val
    
    
    def peek(self):
        val = None
        if self.top != -1:
            return self.data[self.top]
        return val
    
    def length(self):
        return self.top + 1
    
    def __str__(self):
        return f"stack: {self.data}, top: {self.top}"
    
    def isempty(self):
        return self.top == -1
    
