from student import Student
from performance_tracker import  PerformanceTracker

def get_student_info():
    tracker = PerformanceTracker()

    while True:
        name = input("Enter student's name (or 'stop' to finish): ")

        if name.lower() == 'stop':
            break

        scores = []
        subjects = ['Math', 'Science', 'English']

        for subject in subjects:
            while True:
                try:
                    score = int(input(f"Enter {name}'s {subject} score: "))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a whole number.")

        tracker.add_student(name, scores)

    return tracker  # Return the populated tracker


    
def main():
    print("Student performance tracker")
    print("----------------------------------")
    
    tracker = get_student_info()  # Get the populated tracker
    
    class_average = tracker.calculate_class_average()
    print(f"Class Average: {class_average:.2f}")
    
    tracker.display_student_performance()
   
if  __name__ == "__main__":
    main()



        










