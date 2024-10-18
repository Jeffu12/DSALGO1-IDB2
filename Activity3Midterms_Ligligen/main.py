from ArrayStack import ArrayStack as Stack

def is_matched(expression):
    matching_brackets = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in expression:
        if char in matching_brackets.values():
            stack.append(char)
        elif char in matching_brackets.keys():
            if not stack or stack[-1] != matching_brackets[char]:
                return False
            stack.pop()
    return len(stack) == 0
n = input("Enter to know if balanced or not: ")

if is_matched(n):
    print("Symbols are balanced")
else:
    print("Symbols are not balanced")

def reverse_file(myfile):
    stack = []

    with open(myfile, 'r') as file:
        for line in file:
            stack.append(line.rstrip('\n'))

    with open(myfile, 'w') as file:
        while stack:
            file.write(stack.pop())
            if stack:
                file.write('\n')
reverse_file('myfile.txt')