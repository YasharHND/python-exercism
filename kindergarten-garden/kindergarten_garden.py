plants = {
    "G": "Grass",
    "C": "Clover",
    "R": "Radishes",
    "V": "Violets"
}

default_students = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry"
]


class Garden:
    def __init__(self, diagram, students=None):
        if students is None:
            students = default_students
        else:
            students.sort()
        self.students = students
        self.rows = diagram.split()

    def plants(self, student):
        out = []
        index = self.students.index(student) * 2
        out.append(plants[self.rows[0][index]])
        out.append(plants[self.rows[0][index + 1]])
        out.append(plants[self.rows[1][index]])
        out.append(plants[self.rows[1][index + 1]])
        return out
