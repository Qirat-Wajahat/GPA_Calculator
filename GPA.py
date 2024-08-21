# Program to calculate GPA for SMIU

class Student:
    def __init__(self, name, marks,total_marks):
        self.name = name
        self.marks = marks
        self.total_marks = total_marks
        

    def get_GPA(self):
        print("\nCongratulations!", self.name, "Your...")
        sum = 0
        for val in self.marks: 
            sum += val
            percentage = round(sum / self.total_marks * 100)

        print("\nTotal Marks are:", sum)   
        print("\nPercentage is:", percentage, "%")    
        
        if percentage >= 91:
            grade = "A+"
            gpa = 4.00
        elif percentage >= 80 and percentage <= 90:
            grade = "A-"
            gpa = 3.66
        elif percentage >= 75 and percentage <= 79:
            grade = "B+"
            gpa = 3.33
        elif percentage >= 71 and percentage <= 74:
            grade = "B"
            gpa = 3.00
        elif percentage >= 68 and percentage <= 70:
            grade = "B-"
            gpa = 2.66
        elif percentage >= 64 and percentage <= 67:
            grade = "C+"
            gpa = 2.33
        elif percentage >= 61 and percentage <= 63:  
            grade = "C"
            gpa = 2.00
        elif percentage >= 58 and percentage <= 60:
            grade = "C-"
            gpa = 1.66
        elif percentage >= 54 and percentage <= 57:
            grade = "D+"
            gpa = 1.33
        elif percentage >= 50 and percentage <= 53:
            grade = "D"
            gpa = 1.00
        else:
            grade = "F"
            gpa = 0.00
        print(f"\nGrade is {grade} \n\nGPA is {gpa}\n")
                
name = input("\nEnter Your Name: ")

no_of_subjects = int(input(f"\nOk {name}! Enter number of subjects: "))

total_marks = int(input(f"\nNow {name}! Enter Total Marks: "))

# enter exactly 'no_of_subjects' marks
while True:
    marks = [int(x) for x in input(f"\nEnter Your {no_of_subjects} Marks (Use 'Space Key' to separate values): ").split()]
    if len(marks) == no_of_subjects:
        break
    else:
        print(f"\nPlease enter exactly {no_of_subjects} marks.")

s1 = Student(name, marks,total_marks)                
s1.get_GPA()
