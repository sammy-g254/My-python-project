#Tuples are ordered lists of elements whose contents cannot be changed... they are immutable
mycourses=("python","html","javascript","django")
print(mycourses)
print(type(mycourses))
#accessing items
print(mycourses[1:])
print(mycourses[1])
#len - Returns the length of an object
print(len(mycourses))
#loop - execute a block of code repeatedly
#For loop -  when you know in advance how many times you want to iterate or when you want to process each item in a sequence (like a list, tuple, string, or dictionary)
for x in mycourses:
    print(x)