#Create a program that asks users to input their age
#Then displays
#from apport.fileutils import mark_report_seen
age=int(input("What is your age? "))
if age>=18 and age<=25:
    print("You are an youth")
elif age>=26 and age<=40:
    print("You are an adult")
elif age>=40:
    print("You are a middle-aged adult")
else:
    print("You are a child")
#A program that checks if a number entered by the user is an even number
num=int(input("Enter a number "))
if num%2==0:
    print(num,"is an even number")
else:
    print(num,"is an odd number")
#A program that displays student grades according to marks
#A=80-100
#B=70-79
#C=60-69
#D=50-59
#E=40-49
#F=0-39
marks=int(input("Enter your marks "))
if marks>=80 and marks<=100:
    print(marks," A")
elif marks>=70 and marks<=79:
    print(marks," B")
elif marks>=60 and marks<=69:
    print(marks," C")
elif marks>=50 and marks<=59:
    print(marks," D")
elif marks>=40 and marks<=49:
    print(marks," E")
elif marks>=0 and marks<=39:
    print(marks," F")       