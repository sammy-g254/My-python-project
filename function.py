#It does a specified task, which can be recalled, hence without the necessity of typing the code repeatedly
def myfunction():
    print("hello this is a function")
myfunction()
def greeting():
    print("hello!,good morning")
greeting()
#Fuction with parameters and arguments
def hello(fname,age): #argument
    print("how are you?",fname,"You are",age,"years old")
hello("Kim",67)
#Area of the rectangle
def areaofrect(l,w):
    print("The area of a rectangle is",l*w)
areaofrect(34,23)
#A function with a return keyword
def functionex(x):
    return 2*x
y=functionex(2)
print(y)
#function with default parameter
def mycourse(name="python"):
    print("i am learning ",name)
mycourse("html")
mycourse()
mycourse("django")
