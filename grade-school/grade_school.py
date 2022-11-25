class School:
    def __init__(self):
        self.grades = {}
        self.add_result = []

    def add_student(self, name, grade):
        if name not in self.grades:
            self.grades.update({name: grade})
            self.add_result.append(True)
        else:
            self.add_result.append(False)

    def roster(self):
        return [name for name, grade in sorted(self.grades.items(), key=lambda x: (x[1], x[0]))]

    def grade(self, grade_number):
        return sorted([name for name, grade in self.grades.items() if grade == grade_number])

    def added(self):
        return self.add_result
