class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = homepage
        self.backStack = []
        self.forwardStack = []

    def visit(self, url: str) -> None:
        self.backStack.append(self.current)
        self.current = url
        self.forwardStack = []

    def back(self, steps: int) -> str:
        # basically treats it like a linked list
        # counter = len(self.backStack)
        # while counter > 0 and steps > 0:
        #     self.forwardStack.append(self.current)
        #     self.current = self.backStack.pop()
        #     counter -= 1
        #     steps -= 1
        # return self.current

        # uses direct indexing so it's faster
        if len(self.backStack) == 0:
            return self.current
        self.forwardStack.append(self.current)
        index = len(self.backStack) - min(len(self.backStack), steps)
        self.current = self.backStack[index]
        poppedItems = self.backStack[index:]
        poppedItems = poppedItems[1:]
        del self.backStack[index:]
        poppedItems.reverse()
        self.forwardStack.extend(poppedItems)
        return self.current

    def forward(self, steps: int) -> str:
        # basically treats it like a linked list
        # counter = len(self.forwardStack)
        # while counter > 0 and steps > 0:
        #     self.backStack.append(self.current)
        #     self.current = self.forwardStack.pop()
        #     counter -= 1
        #     steps -= 1
        # return self.current

        # uses direct indexing so it's faster
        if len(self.forwardStack) == 0:
            return self.current
        self.backStack.append(self.current)
        index = len(self.forwardStack) - min(len(self.forwardStack), steps)
        self.current = self.forwardStack[index]
        poppedItems = self.forwardStack[index:]
        poppedItems = poppedItems[1:]
        del self.forwardStack[index:]
        poppedItems.reverse()
        self.backStack.extend(poppedItems)
        return self.current


obj = BrowserHistory("leetcode.com")
obj.visit("google.com")
obj.visit("facebook.com")
obj.visit("youtube.com")
obj.visit("theverge.com")
obj.visit("nytimes.com")
obj.visit("twitter.com")
obj.back(100)
obj.back(100)
