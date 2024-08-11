 
import matplotlib.pyplot as plt 
 
class Student: 
    def __init__(self, name, roll_no, marks): 
        self.name = name 
        self.roll_no = roll_no 
        self.marks = marks 
 
class StudentDatabase: 
    def __init__(self): 
        self.students = [] 
 
    def add_student(self, student): 
        self.students.append(student) 
 
    def edit_student(self, roll_no, name, marks): 
        for student in self.students: 
            if student.roll_no == roll_no: 
                student.name = name 
                student.marks = marks 
                return True 
        return False 
 
    def delete_student(self, roll_no): 
        for student in self.students: 
            if student.roll_no == roll_no: 
                self.students.remove(student) 
                return True 
        return False 
 
    def plot_marks_pie_chart(self): 
        labels = [student.name for student in self.students] 
        sizes = [student.marks for student in self.students] 
        
        plt.figure(figsize=(8, 8)) 
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140) 
        plt.axis('equal') 
        plt.title('Distribution of Marks') 
        plt.show() 
 
def get_int_input(prompt): 
    while True: 
        try: 
            value = int(input(prompt)) 
            return value 
        except ValueError: 
            print("Invalid input! Please enter an integer.") 
 
def main(): 
    database = StudentDatabase() 
 
    while True: 
        print("\n1. Add Student\n2. Edit Student\n3. Delete Student\n4. Plot Marks Pie Chart\n5. 
Exit") 
        choice = get_int_input("Enter your choice: ") 
 
        if choice == 1: 
            name = input("Enter student name: ") 
            roll_no = get_int_input("Enter roll number: ") 
            marks = get_int_input("Enter marks: ") 
            database.add_student(Student(name, roll_no, marks)) 
            print("Student added successfully!") 
 
        elif choice == 2: 
            roll_no = get_int_input("Enter roll number of the student to edit: ") 
            name = input("Enter new name: ") 
            marks = get_int_input("Enter new marks: ") 
            if database.edit_student(roll_no, name, marks): 
                print("Record edited successfully!") 
            else: 
                print("Student not found!") 
 
        elif choice == 3: 
            roll_no = get_int_input("Enter roll number of the student to delete: ") 
            if database.delete_student(roll_no): 
                print("Student record deleted successfully!") 
            else: 
                print("Student not found!") 
 
        elif choice == 4: 
            if not database.students: 
                print("No students in the database!") 
            else: 
                database.plot_marks_pie_chart() 
 
        elif choice == 5: 
            print("Exiting program...") 
            break 
 
        else: 
            print("Invalid choice! Please try again.") 
 
if __name__ == "__main__": 
    main()