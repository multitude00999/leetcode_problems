class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.data = [-1]*self.size
        self.head = -1
        self.tail = -1
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1)%self.size
        self.data[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        
        self.head = (self.head + 1)%self.size
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.tail]

    def isEmpty(self) -> bool:
        if self.head == -1:
            return True
        return False

    def isFull(self) -> bool:
        if ((self.tail + 1)%self.size) == self.head:
            return True
        return False
