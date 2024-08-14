# Program to calculate GPA for SMIU

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        

    def get_GPA(self):
        print("\nCongratulations!", self.name, "Your...")
        sum = 0
        for val in self.marks: 
            sum += val
        percentage = sum / 600 * 100
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

# enter exactly 7 marks
while True:
    marks = [int(x) for x in input("\nEnter Your 7 Marks (Use 'Space Key' to separate values): ").split()]
    if len(marks) == 7:
        break
    else:
        print("\nPlease enter exactly 7 marks.")

s1 = Student(name, marks)                
s1.get_GPA()
