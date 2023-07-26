class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        

    def push(self, x: int) -> None:

        # empty queue1 into queue2
        while len(self.queue1):
            self.queue2.append(self.queue1[0])
            self.queue1.pop(0)
        
        self.queue1.append(x)

        # put back element from queue2 to queue1
        while len(self.queue2):
            self.queue1.append(self.queue2[0])
            self.queue2.pop(0)

    def pop(self) -> int:
        if self.empty():
            return -1
        val = self.queue1[0]
        self.queue1.pop(0)
        return val

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return len(self.queue1) == 0

