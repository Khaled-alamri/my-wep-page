from math import *

#this is code for library of math

#var,string and type for data .
print(4 ** 2)
print(type(3.3))
message ="what'up \nDec"
#n\ for new lien .
n=10
pi=3.14
print(message)
print(n)
print(pi)
print(n*pi)

print(len('hello'))
#len is for length .
my_name="khaled"
print(my_name[0])
#for find data by length index.
print(my_name.index("a"))
#find index for letters or any tyep data.
print(my_name.replace("e","i"))
#for replace letters or word in my text.

print(sqrt(25))
#this mthod for import library

#/

#input

#name= input("enter your name: ")
#age=input("enter you age: ")
#print("Hello "+name+ " and your age is " + age)

#this is for input and how we are work with it, this part for string jast.

#num_1=input("enter the first no: ")
#num_2=input("enter the second no: ")
#result= float (num_1) + float(num_2)
#print(result)

#this input about number and how we are work with it. 

#animals=input("what your favorite animals? ")
#color=input("what it color?")
#about=input("what you feel about it? ")

#print("it is wonderful choice " + animals)
#print("it is wonderful color "+ color)
#print(about," this is wonderful feel about your animals")

#/

#List in python .

friends =["khaled","nissr"]
programming =["python","html","css"]
 
programming.remove("html")
#1-this for remove i thenk this is so claer.
programming.append("Ionic")
#2-this for add a new data to my list but this function added the data in last the list.
friends.insert(0,"ail")
#3-this function for add data with index number .

pop_vaule=programming.pop()
#4-this function to remove the last data added in your last and you can taking it in var.
friends.sort()
#5-this funtion for data order by letters or numder.

friends+=programming
#6-this example for extend for tow lists together and the ather way it use +=

new_list=friends.copy()
#7-this function for copy the list in last version you do.

friends.append("oumer")

print(friends)
print(new_list)
print(friends[0])
print(friends.index("khaled"))
print(friends.count("html"))
print(pop_vaule)

#/

#Tuples

coordinates=[(23,33),(33,77),(44,90)]
#in tuples you can't chang any data .

#/

#functions1

def say_hi(name ,age):
    print("Hello user " +name+ " you age is " + str(age))
    
say_hi("Ail",43)
#this way of ues function in python writing the code of function after the spac if you go out the spac your function is doen.
#/
#return
def cube(num):
    return num*num*num

def sum(num1,num2):
    return num1+num2
    #Return is the last line in the function .

rseult=cube(5)
print(rseult)
print(sum(4,7))

#/

#conditionals (if,for)

is_hungry=True
wants_to_eat=False
if is_hungry and wants_to_eat:
    print("go eat")
    print("order")
elif is_hungry and not wants_to_eat:
    print("eat so you can survive")
elif not wants_to_eat and is_hungry:
    print("no you most eat")
else:
    print("ok")

#this way to ues if and else in python and use (or,and).

print(max(3,44,3333,23213))
#this function in python return the big number in your numbers.
#/
#Calculator 

num1=float(input("please enter your number: "))
operator=input("please enter the operator: ")
num2=float(input("please enter second number: "))
if operator =="+":
    print(num1+num2)
elif operator =="-":
    print(num1-num2)
elif operator =="*":
    print(num1*num2)
elif operator =="/":
    print(num1/num2)
else:
    print("please try again")


