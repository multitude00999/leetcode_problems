class MinStack:
    def __init__(self):
        self.data = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        # store minval with each element (which denotes the minimum of all the elements below this element including itself)
        dataval = [-1, -1]
        dataval[0] = val
        if len(self.data)>0:
            dataval[1] = min(self.data[-1][1], val)
        else:
            dataval[1] = val
        self.data.append(dataval)

    def pop(self) -> None:
        self.data.pop(-1)

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]