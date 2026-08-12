class MinStack:

    def __init__(self):
        self.arr = []
        

    def push(self, value: int) -> None:
        if not self.arr:
            self.arr.append((value,value))
        else:
            curr_min = self.arr[-1][1]
            self.arr.append((value,min(value , curr_min)))

    def pop(self) -> None:
        if self.arr:
            del self.arr[-1]
        

    def top(self) -> int:
        if self.arr:
            return self.arr[-1][0]
        

    def getMin(self) -> int:
        return self.arr[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()