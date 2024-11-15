from DoublyLinkedBase import _DoublyLinkedBase


class LinkedDeque(_DoublyLinkedBase):
    '''Double ended queue implementation based on a doubly linked list.'''

    def first(self):
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._header._next._element  # real item just after header

    def last(self):
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._trailer._prev._element  # real item just before trailer

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)  # after header

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)  # before trailer

    def delete_first(self):
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._delete_node(self._header._next)  # use inherited method

    def delete_last(self):
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._delete_node(self._trailer._prev)  # use inherited method


class LinkedQueue:
    '''FIFO queue implementation using a singly linked list for storage.'''

    class _Node:
        '''Lightweight non public class for storing a singly linked node.'''
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        '''Create an empty queue'''
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        '''Return the number of elements in the queue'''
        return self._size

    def is_empty(self):
        '''Return true if the queue is empty.'''
        return self._size == 0

    def first(self):
        '''Return but do not remove the element at the front of the queue'''
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head._element  # front aligned with the head of the list

    def dequeue(self):
        '''Remove and return the first element of the queue (FIFO)'''
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():  # special case as queue is empty
            self._tail = None  # removed head had been the tail
        return answer

    def enqueue(self, e):
        '''Add an element to the back of queue.'''
        newest = self._Node(e, None)  # node will be new tail node
        if self.is_empty():
            self._head = newest  # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest  # update reference to tail node
        self._size += 1


class LinkedStack:
    '''LIFO Stack implementation using a singly linked list for storage.'''

    class _Node:
        '''Lightweight non public class for storing a singly linked node.'''
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        '''Create an empty Stack'''
        self._head = None
        self._size = 0

    def __len__(self):
        '''Return the number of elements in the stack'''
        return self._size

    def is_empty(self):
        '''Return True if the stack is empty.'''
        return self._size == 0

    def push(self, e):
        '''Add element e to the top of the stack.'''
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        '''Return but do not remove the element at the top of the stack'''
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element  # top of the stack is the head of the list

    def pop(self):
        '''Remove and return the elements from the top of the stack (LIFO)'''
        if self.is_empty():
            raise Exception("The stack is empty!")

        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


def print_queue(queue):
    '''Prints the contents of the queue without modifying it.'''
    current = queue._head  # Access the head of the queue
    elements = []

    while current:
        elements.append(str(current._element))  # Collect each element
        current = current._next  # Move to the next node

    print("Q: " + ", ".join(elements))


def print_deque(deque):
    '''Prints the contents of the deque without modifying it.'''
    current = deque._header._next  # Start from first element after header
    elements = []

    while current != deque._trailer:  # Stop at trailer
        elements.append(str(current._element))
        current = current._next

    print("D: " + ", ".join(elements))

def print_stack(stack):
    '''Prints the contents of the stack without modifying it.'''
    current = stack._head  # Start from the top of the stack
    elements = []

    while current:  # Traverse until we reach the end of the stack
          elements.append(str(current._element))  # Collect each element
          current = current._next  # Move to the next node

    print("S: " + ", ".join(elements))  # Print stack contents


# Main logic to manipulate deque and queue
D = LinkedDeque()
Q = LinkedQueue()
S = LinkedStack()

# Populate D with elements
D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)

print("Before Sort")
print_deque(D)
print_queue(Q)
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(Q.dequeue())
Q.enqueue(Q.dequeue())
Q.enqueue(Q.dequeue())
D.insert_first(Q.dequeue())
D.insert_first(Q.dequeue())
Q.enqueue(Q.dequeue())
Q.enqueue(Q.dequeue())
Q.enqueue(Q.dequeue())
Q.enqueue(Q.dequeue())
Q.enqueue(Q.dequeue())
Q.enqueue(Q.dequeue())
Q.enqueue(Q.dequeue())
Q.enqueue(Q.dequeue())
D.insert_first(Q.dequeue())
Q.enqueue(Q.dequeue())
D.insert_first(Q.dequeue())
D.insert_first(Q.dequeue())
print("After Sort")
print_deque(D)
print_queue(Q)

print("Repeat the previous problem using deque D and an initially empty stack S.")

D = LinkedDeque()

print("Stack:")
D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)


D.insert_last(D.delete_first())
D.insert_last(D.delete_first())
D.insert_last(D.delete_first())
S.push(D.delete_first())
D.insert_last(D.delete_first())
D.insert_last(S.pop())
D.insert_last(D.delete_first())
D.insert_last(D.delete_first())
D.insert_last(D.delete_first())
print_deque(D)
print_stack(S)
print("After Sorting with Stack S")
print_deque(D)
print_stack(S)