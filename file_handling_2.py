#open(filename,mode)
#modes-r:read,w:write,a:append
#Write to a file
#close()
#Reading a specific line
f=open("demo.txt","r")
print(f.readlines(1))
print(f.readlines(2))