class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2  = []

    def push(self, x: int) -> None:

        # empty stack 1 into stack2
        while len(self.stack1):
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()

        # add element to stack 1
        self.stack1.append(x)

        # put back from stack 2 to stack 1
        while len(self.stack2):
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()
        
    def pop(self) -> int:
        if self.empty():
            return -1
        val = self.stack1[-1]
        self.stack1.pop(-1)
        return val

    def peek(self) -> int:
        if self.empty():
            return -1
        return self.stack1[-1]
        

    def empty(self) -> bool:
        if len(self.stack1)==0:
            return True
        return False