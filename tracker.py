class Student:
    def __init__(self, name):
        self.name = name  # Store the student's name
        self.scores = []  # Initialize an empty list for scores

    def add_scores(self, scores):
            self.scores.extend(scores)  # Add multiple scores at once

    def calculate_average(self):
        if not self.scores:
            return 0  # Return 0 if there are no scores
        return sum(self.scores) / len(self.scores)  # Calculate average score

    def is_passing(self, passing_score=40):
        if all(score >= passing_score for score in self.scores):  # Check if all scores are >= passing_score
            return f"Passed"
        else:
            return f"Failed"

    def __str__(self):
        return f"Name: {self.name}, Scores: {self.scores}, Average: {self.calculate_average():.2f}, {self.is_passing()}"


class PerformanceTracker:
    def __init__(self):
        self.students = {}  # Dictionary to store students by name

    def add_student(self, name, scores):
        if name in self.students:
            print(f"Student {name} already exists! Adding new scores...")
            self.students[name].add_scores(scores)
        else:
            student = Student(name)
            student.add_scores(scores)
            self.students[name] = student

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)

    def display_student_performance(self):
        if not self.students:
            print("No students available.")
        for student in self.students.values():
            print(student)


# Main Program
tracker = PerformanceTracker()

while True:
    print("\nMenu:")
    print("1. Add Student and Scores")
    print("2. Display Student Performance")
    print("3. Calculate Class Average")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        for i in range(2):
            name = input("Enter the student's name: ")
            if len(name)>= 3:
                break
            else:
                print("Enter a valid name having 3 or more letters!")
        try:
            scores = []
            for i in range(3):
                a = int(input(f"Enter Marks in subject {i+1}: "))
                scores.append(a)
                
            # scores = list(map(int, input("Enter the scores (comma-separated): ").split(',')))
            tracker.add_student(name, scores)
            print(f"Scores added for {name}.")
        except ValueError:
            print("Invalid input. Please enter numeric scores only.")

    elif choice == '2':
        print("\nStudent Performance:")
        tracker.display_student_performance()

    elif choice == '3':
        print(f"\nClass Average Score: {tracker.calculate_class_average():.2f}")

    elif choice == '4':
        print("Exiting the tracker. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
