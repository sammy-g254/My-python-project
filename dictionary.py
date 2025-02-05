#A dictionary is a built-in data type
#It stores collections of data in key-value pairs.
student={
    "name":"jane",
    "age":20,
    "city":"nairobi",
}
print(student)
#Accessing values
print(student["name"])
print(student["age"])
#Keys: Must be unique within a dictionary and immutable 
#      (e.g., strings, numbers, or tuples containing only immutable elements).
print(student.keys())
#Values: Can be of any data type and can be easily changed
student["name"]="Joseph"
print(student)
#Adding items
student["course"]="fullstack"
print(student)
#remove item - pop()
student.pop("city")
print(student)
#loop through the keys
#loop through the values
#Loop through keys and values using items method
for x,y in student.items():
    print(x,y)