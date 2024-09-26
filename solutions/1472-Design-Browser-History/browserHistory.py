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
        counter = len(self.backStack)
        while counter > 0 and steps > 0:
            self.forwardStack.append(self.current)
            self.current = self.backStack.pop()
            counter -= 1
            steps -= 1
        return self.current

    def forward(self, steps: int) -> str:
        counter = len(self.forwardStack)
        while counter > 0 and steps > 0:
            self.backStack.append(self.current)
            self.current = self.forwardStack.pop()
            counter -= 1
            steps -= 1
        return self.current


obj = BrowserHistory("leetcode.com")
obj.visit("google.com")
obj.visit("facebook.com")
obj.visit("youtube.com")
obj.back(1)
obj.back(1)
obj.forward(1)
obj.visit("linkedin.com")
obj.forward(2)
obj.back(2)
obj.back(7)
