#Combination
fname="john"
course="cybersecurity"
print("my name is",fname, "and I'm learning",course)
#Using f string formatting
print(f'my name is {fname} and I am learning {course}')
#Arithmetic Operators
a=60
b=40
c=3
#Addition
sum=a+b
print(f'the sum of {a} and {b} is {sum}')
#Subtraction
diff=a-b
print(f'the difference of {a} and {b} is {diff}')
#Multiplication
prod=a*b
print(f'the product of {a} and {b} is {prod}')
#Division
div=a/b
print(f'the quotient from the division of {a} by {b} is {div}')
#modulus
mod=a%b
print(f'the remainder from the division of {a} by {b} is {mod}')
#Exponential
exp=b**c
print(f'the exponent of {b} by the index {c} is {exp}')
#Comparison operators
x=40
y=35
#Equal to
eq=x==y
print(f'is {x} equal to {y}? {eq}')
#Greater than
gr=x>y
print(f'is {x} greater than {y}? {gr}')
#Less than
le=x<y
print(f'is {x} less than {y}? {le}')
#Greater than or Equal to
greq=x>=y
print(f'is {x} greater than or equal to {y}? {greq}')
#Less than or Equal to
leeq=x<=y
print(f'is {x} less than or equal to {y}? {leeq}')
#Logical operators
#They are used to combne conditional statements
c=5
d=3
e=10
f=2
#And returns true when both statements are true
And1=c>d and c<e
print(f'is {c}>{d} and {c}<{e} ? {And1}')
And2=c>d and c<f
print(f'is {c}>{d} and {c}<{f} ? {And2}')
#Or returns true if one of the statements is true and false if both are false
Or1=c>d or c<e
print(f'is {c}>{d} or {c}<{e} ? {Or1}')
Or2=c>d or c<f
print(f'is {c}>{d} or {c}<{f} ? {Or2}')
Or3=c<d or c<f
print(f'is {c}<{d} or {c}<{f} ? {Or3}')
#Not returns the inverse of the result
Not1=c>d or c<e
print(f'is {c}>{d} or {c}<{e} ? {not(Not1)}')
Not2=c>d or c<f
print(f'is {c}>{d} or {c}<{f} ? {not(Not2)}')
Not3=c<d or c<f
print(f'is {c}<{d} or {c}<{f} ? {not(Not3)}')