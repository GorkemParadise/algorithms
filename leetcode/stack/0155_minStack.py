class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:    # 5 3 2 1
        if len(self.stack) > 0:
            if self.stack.pop() == self.min_stack[-1]:
                self.min_stack.pop()


    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        