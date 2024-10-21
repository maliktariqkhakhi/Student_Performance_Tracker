from student import Student
class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if len(self.students) == 0:  # Check if there are any students
            return 0  # or return None, or handle it as you wish
        total_scores = sum(student.calculate_average() for student in self.students.values())
        return total_scores / len(self.students)


    def display_student_performance(self, passing_score=40):
        for student in self.students.values():
            average = student.calculate_average()
            passing_status = "Passing" if student.is_passing(passing_score) else "Failing"
            print(f"Name: {student.name}, Average: {average:.2f}, Status: {passing_status}")
