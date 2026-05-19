class FreqStack:

    def __init__(self):
        self.stack = {}
        # value and count
        self.hashmap = {}
        self.max_count = 0
        

    def push(self, val: int) -> None:

        
        valueCount = 1 + self.hashmap.get(val,0)

        if valueCount > self.max_count:
            self.max_count = valueCount
            self.stack[valueCount] = []
        self.stack[valueCount].append(val)
        self.hashmap[val] = valueCount

    def pop(self) -> int:
        # print(self.stack)
        popped_item = self.stack[self.max_count].pop()
        self.hashmap[popped_item] -=1
        if self.stack[self.max_count] == []:
            self.max_count -=1
        return popped_item


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()