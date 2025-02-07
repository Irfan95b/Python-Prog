'''
    Standard Input :

        In python we have two types of input to the program
            1. Static Input
            2. Dynamic Input

        1. In programing, when we are giving direct-input-values, it is known as (static input).
                Ex :-
                    a = 10;
                    b = 20.7
                    str = "Python Programing"

        2. input() - function is used to read/accept data directly from keyboard,
           while program is in executing form, This is known as (dynamic-input).
           input() - function reads any data from keyboard as string-format only
           Hence, Typecasting is also Required here.
           so we use (type-conversion funcs) to get input in dezaired form
            i.e,
	         int(), float(), bool(), complex() etc...
                Ex :-
                    a = int(input("Enter A-value :: "));
                    b = float(input("Enter B-value : "));

        Note:-
            Give Proper-input-value from keyboard other wise we get "ValueError".


'''

# Simple program to get the Dynamic input.
'''
a = input("Enter 'a' value : ")
b = input("Enter 'b' value : ")

print("Given 'a' value is :",a, type(a))
print("Given 'b' value is :",b, type(b))

a = int(a)
b = float(b)

print("\nAfter conversion")
print("Given 'a' value is :",a, type(a))
print("Given 'b' value is :",b, type(b))
'''

# Program to print sum of two numbers
'''
a = float(input("Enter 'a' value : "))
b = int(input("Enter 'b' value : "))

sum = a+b;

print("Sum of {} and {} is :".format(a,b),sum)
'''


# Program to get different data as input and print it.

# int
a = int(input("Enter integer value for variable a : "))
print("Given 'a' value is : ",a, type(a));

# float
a = float(input("Enter float value for variable a : "))
print("Given 'a' value is : ",a, type(a));

# complex
a = complex(input("Enter complex value for variable a : "))
print("Given 'a' value is : ",a, type(a));

# boolean
a = bool(input("Enter boolean value for variable a : "))
print("Given 'a' value is : ",a, type(a));

# string
a = input("Enter string value for variable a : ")
print("Given 'a' value is : ",a, type(a));

