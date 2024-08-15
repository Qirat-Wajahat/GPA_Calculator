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
        percentage = sum / self.total_marks * 100
        print("\nTotal Marks are:", sum)   
        print("\nPercentage is:", percentage, "%")    
        
        if percentage >= 91:
            print("\nGrade is A+ \n\nGPA is 4.00\n")
        elif percentage >= 80 and percentage <= 90:
            print("\nGrade is A- \n\nGPA is 3.66\n")
        elif percentage >= 75 and percentage <= 79:
            print("\nGrade is B+ \n\nGPA is 3.33\n")
        elif percentage >= 71 and percentage <= 74:
            print("\nGrade is B \n\nGPA is 3.00\n")
        elif percentage >= 68 and percentage <= 70:
            print("\nGrade is B- \n\nGPA is 2.66\n")
        elif percentage >= 64 and percentage <= 67:
            print("\nGrade is C+ \n\nGPA is 2.33\n")
        elif percentage >= 61 and percentage <= 63:  
            print("\nGrade is C \n\nGPA is 2.00\n")
        elif percentage >= 58 and percentage <= 60:
            print("\nGrade is C- \n\nGPA is 1.66\n")
        elif percentage >= 54 and percentage <= 57:
            print("\nGrade is D+ \n\nGPA is 1.33\n") 
        elif percentage >= 50 and percentage <= 53:
            print("\nGrade is D \n\nGPA is 1.00\n")     
        else:
            print("\nGrade is F \n\nGPA is 0.00\n")
                
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
