#While loop - it executes a set of statements as long as the condition is true
x=1
while x<=10:
    print(x)
    x+=1 #Or x=x+1
print("Another loop")
#print 1-5 using a loop
y=1
while y<=5:
    print(y)
    if y==3:
        break
    y=y+1
#For loop - it loops through a sequence (lists, dictionaries, e.t.c)
cars=["Mazda","BMW","Toyota","RangeRover"]
for x in cars:
    print(x)
#Looping through a string
for y in "hello":
    print(y)
#Looping through a range
for z in range(5):
    print(z)
#Looping through a range with start and stop
for i in range(2,7):
    print(i)
#Break
users=["Mary","Jane","Nelson","John"]
for x in users:
    if x=="Nelson":
        break
    print(x)
#continue
#skip a user and continue with the next user
for x in users:
    if x=="Jane":
        continue
    print(x)