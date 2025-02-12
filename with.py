with open("example.txt","w") as f:
    f.write("hello, this is python \n")
    f.write("this is how to write to a file in python")
#read
with open("example.txt","w") as f:
    f.write("welcome to the new python \n")
#read
with open("example.txt","r") as f:
    print(f.read())