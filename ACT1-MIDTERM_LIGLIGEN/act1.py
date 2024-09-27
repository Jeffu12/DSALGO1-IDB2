class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return item

    def pop(self):
        if self.is_empty():
            return "Stack Empty"
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

S = Stack()
S.push(5)
print(S)
S.push(3)
print(S)
print("Length:", len(S))
print("S.pop(): ", S.pop())
print(S)
print("S.is_empty:", S.is_empty())
print("S.pop(): ", S.pop())
print("S.is_empty:", S.is_empty())
print("S.pop(): ", S.pop())
S.push(7)
print(S)
S.push(9)
print(S)
print("Peek/ Top: ", S.peek())
S.push(4)
print(S)
print("Length:", len(S))
print("S.pop(): ", S.pop())
print(S)
S.push(6)
print(S)
S.push(8)
print(S)
print("S.pop(): ", S.pop())
print(S)
"""Start of Simulation 2"""
print()
print("Simulation 2")
print("push(5), push(3), pop(), push(2), push(8), pop(), "
      "pop(), push(9), push(1), "
      "pop(), push(7),push(6), pop(), "
      "pop(), push(4), pop(), pop().")
X = Stack()
X.push(5)
print(X)
X.push(3)
print(X)
print("X.pop(): ", X.pop())
print(X)
X.push(2)
print(X)
X.push(8)
print(X)
print("X.pop(): ", X.pop())
print("X.pop(): ", X.pop())
X.push(9)
print(X)
X.push(1)
print(X)
print("X.pop(): ", X.pop())
X.push(7)
print(X)
X.push(6)
print(X)
print("X.pop(): ", X.pop())
print("X.pop(): ", X.pop())
X.push(4)
print(X)
print("X.pop(): ", X.pop())
print("X.pop(): ", X.pop())
print(X)