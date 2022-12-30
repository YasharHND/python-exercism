class CustomSet:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = elements

    def isempty(self):
        return len(self.elements) == 0

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        for element in self.elements:
            if element not in other.elements:
                return False
        return True

    def isdisjoint(self, other):
        for element in self.elements:
            if element in other.elements:
                return False
        return True

    def __eq__(self, other):
        return sorted(self.elements) == sorted(other.elements)

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def intersection(self, other):
        common = []
        for element in self.elements:
            if element in other.elements:
                common.append(element)
        return CustomSet(common)

    def __sub__(self, other):
        for element in other.elements:
            if element in self.elements:
                self.elements.remove(element)
        return CustomSet(self.elements)

    def __add__(self, other):
        for element in other.elements:
            self.add(element)
        return CustomSet(self.elements)
