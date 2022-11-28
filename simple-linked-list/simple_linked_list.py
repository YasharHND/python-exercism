class Node:
    def __init__(self, value):
        self.val = value
        self.next_node = None

    def value(self):
        return self.val

    def next(self):
        return self.next_node


class LinkedList:
    def __init__(self, values=None):
        self.values = [Node(val) for val in values[::-1]] if values else []
        for i, node in enumerate(self.values[:-1]):
            node.next_node = self.values[i + 1]
        self.current_node = self.values[0] if self.values else None

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current_node:
            raise StopIteration
        out = self.current_node.value()
        self.current_node = self.current_node.next()
        return out

    def head(self):
        self.check_length()
        return self.values[0]

    def push(self, value):
        node = Node(value)
        next_node = self.values[0] if self.values else None
        node.next_node = next_node
        self.values.insert(0, node)

    def pop(self):
        self.check_length()
        return self.values.pop(0).value()

    def reversed(self):
        return LinkedList([node.value() for node in self.values])

    def check_length(self):
        if not self.values:
            raise EmptyListException("The list is empty.")


class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message
