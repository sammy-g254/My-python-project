#open(filename,mode)
#modes-r:read,w:write,a:append
#Write to a file
#close()
x=open("demo.txt","w")
x.write("this is a new file")
x.close()
#read the file
x=open("demo.txt","r")
print(x.read())
x.close()
#append
f=open("demo.txt","a")
f.write("\nhello good morning")
f.close()
#read
f=open("demo.txt","r")
print(f.read())
f.close()
