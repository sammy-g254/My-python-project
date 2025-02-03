#string is a data type used to represent text
greeting="hello world"
course='python'
print(greeting)
print(course)
#string edits
#change case
print(greeting.upper())
print(greeting.lower())
print(greeting.title())
#length
print(len(course))
print(len(greeting))
print(len("mark"))
#string concatenation "+""
fname="Sam"
lname="G"
print(fname+" "+lname)
#escape characters "\"
print("hello good morning, \nhow are you")
print("name\tcourse")
print('She actually "responded"')
print('but truly, is it actually \"possible\"')
print("Now that's it")
print("she said \"hello\"")
print("she said \"it's a nice day\"")
print("""
      This 
      is 
      an 
      example 
      of 
      a 
      multiline 
      string""")
#string indexing starts from 0
text=('python')
print(text[1])
print(text[3])
message="hello"
print(message[-3],message[-3])
#string slicing
mytext="Fullstack"
print(mytext[0:4]) #full
print(mytext[4:]) #stack
print(mytext[0:5]) #fulls
#replace
sentence="I love html"
print(sentence.replace("html","python"))