class MinStack:
    stack = []
    minStack = []

    def __init__(self):
        return

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if not self.minStack:
    #         self.minStack.append(val)
    #     if self.minStack and val < self.minStack[-1]:
    #         self.minStack.append(val)

    # def pop(self) -> None:
    #     popped = self.stack[-1]
    #     if popped == self.minStack[-1]:
    #         self.minStack.pop()
    #     self.stack.pop()

    # ^ above is what I originally wrote. For some reason it worked on my machine but LeetCode wouldn't take it. Idk.
    # At any rate, I *did* figure out the design of the solution myself, but obviously there was an implementation issue.

    # neetcode solution
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


minstack = MinStack()
minstack.push(-1)
print(minstack.top())
print(minstack.getMin())
