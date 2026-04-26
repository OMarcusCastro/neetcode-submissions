class MinStack:

    def __init__(self):
        self.data = []
        self.min_ = None

    def push(self, val: int) -> None:
        self.data.append(val)
        

    def pop(self) -> None:
        
        self.data.pop()
        

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        self.min_ = self.data[-1]
        for element in self.data:
            self.min_ = min(self.min_,element)
        return self.min_
