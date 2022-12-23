class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.empty = True
        self.single = False

    def push(self, value):
        node = Node(value)
        if self.empty:
            self.first, self.last = node, node
            self.empty = False
            self.single = True
        elif self.single:
            node.previous = self.first
            self.first.succeeding = node
            self.last = node
            self.single = False
        else:
            node.previous = self.last
            self.last.succeeding = node
            self.last = node

    def pop(self):
        if self.empty:
            raise IndexError("List is empty")
        value = self.last.value
        if self.single:
            self.first, self.last = None, None
            self.single = False
            self.empty = True
        elif self.last.previous == self.first:
            self.first.succeeding = None
            self.last = self.first
            self.single = True
        else:
            self.last = self.last.previous
            self.last.succeeding = None
        return value

    def shift(self):
        if self.empty:
            raise IndexError("List is empty")
        value = self.first.value
        if self.single:
            self.first, self.last = None, None
            self.single = False
            self.empty = True
        elif self.first.succeeding == self.last:
            self.last.previous = None
            self.first = self.last
            self.single = True
        else:
            self.first = self.first.succeeding
            self.first.previous = None
        return value

    def unshift(self, value):
        node = Node(value)
        if self.empty:
            self.first, self.last = node, node
            self.empty = False
            self.single = True
        elif self.single:
            node.succeeding = self.last
            self.last.previous = node
            self.first = node
            self.single = False
        else:
            node.succeeding = self.first
            self.first.previous = node
            self.first = node

    def delete(self, value):
        if self.empty:
            raise ValueError("Value not found")
        if self.single:
            if self.first.value != value:
                raise ValueError("Value not found")
            self.first, self.last = None, None
            self.single = False
            self.empty = True
        else:
            node = self.first
            while node:
                if node.value == value:
                    if node.previous:
                        node.previous.succeeding = node.succeeding
                    if node.succeeding:
                        node.succeeding.previous = node.previous
                    if not self.first.previous and not self.first.succeeding:
                        self.last.value = self.first.value
                        self.first.succeeding = None
                        self.single = True
                    elif not self.last.previous and not self.last.succeeding:
                        self.first.value = self.last.value
                        self.last.previous = None
                        self.single = True
                    return
                node = node.succeeding
            else:
                raise ValueError("Value not found")

    def __len__(self):
        if self.empty:
            return 0
        if self.single:
            return 1
        count = 0
        node = self.first
        while node:
            count += 1
            node = node.succeeding
        return count
