from LinkedStack import LinkedStack
from PositionalList import PositionalList


def precedence(op):
    """Return the precedence of the operator."""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    """Convert infix expression to postfix using LinkedStack."""
    stack = LinkedStack()  # Use LinkedStack instead of a list
    output = []

    for char in expression:
        if char.isdigit():
            output.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty():
                top = stack.pop()
                if top == '(':
                    break
                output.append(top)
            else:
                raise Exception("Mismatched parentheses")
        else:  # Operator
            while (not stack.is_empty() and
                   precedence(stack.top()) >= precedence(char)):
                output.append(stack.pop())
            stack.push(char)

    while not stack.is_empty():
        output.append(stack.pop())

    return " ".join(output)


def insertion_sort_ascending(positional_list):
    """Sorts a PositionalList in ascending order using insertion sort."""
    if positional_list.is_empty():
        return

    # Extract elements into a list
    elements = [positional_list.delete(positional_list.first()) for _ in range(len(positional_list))]

    # Sort using insertion sort on list
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and elements[j] > key:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key

    # Reinsert sorted elements back into positional list
    for element in elements:
        positional_list.add_last(element)


def insertion_sort_descending(positional_list):
    """Sorts a PositionalList in descending order using insertion sort."""
    if positional_list.is_empty():
        return

    # Extract elements into a list
    elements = [positional_list.delete(positional_list.first()) for _ in range(len(positional_list))]

    # Sort using insertion sort on list
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and elements[j] < key:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key

    # Reinsert sorted elements back into positional list
    for element in elements:
        positional_list.add_last(element)


def main():
    # Create a PositionalList instance for the infix expression.
    P = PositionalList()
    P.add_last('(')
    P.add_last('(')
    P.add_last('5')
    P.add_last('+')
    P.add_last('2')
    P.add_last(')')
    P.add_last('*')
    P.add_last('(')
    P.add_last('8')
    P.add_last('-')
    P.add_last('3')
    P.add_last(')')
    P.add_last(')')
    P.add_last('/')
    P.add_last('4')
    # Convert to postfix notation
    postfix_expression = infix_to_postfix(list(P))
    print("Postfix expression:", postfix_expression)

    print()


    # sorting demonstration.
    Q = PositionalList()

    Q.add_last(1)
    Q.add_last(72)
    Q.add_last(81)
    Q.add_last(25)
    Q.add_last(65)
    Q.add_last(91)
    Q.add_last(11)

    print("Array: ", list(Q))

    insertion_sort_ascending(Q)
    print("Sorted in Ascending Order:", list(Q))

    insertion_sort_descending(Q)
    print("Sorted in Descending Order:", list(Q))


if __name__ == "__main__":
    main()