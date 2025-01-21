'''
    Type-Casting:
    ------------
        Converting one datatype value into another datatype value is called type casting.
        It is Known as (Type coersion) or (Type Conversion) or (Type Casting).

        Python provides inbuilt type casting functions...................
            int() --> Converts other data-type into int-type
            float() --> Converts other data-type into float-type
            complex() --> Converts other data-type into complex-type
            bool() --> Converts other data-type into bool-type
            str() --> Converts other data-type into str-type

'''

# Program to show type-casting with python functions.

'''
int_var = 10
float_var = 142.38
complex_var = 5+6j
bool_var = True
str_var = "Hello Python Programmers"
'''


# int() conversion function
#----------------------------
a = int(10)
print(a)
a = int(142.38) # complete decimal part is deleted.
print(a)
a = int("2025")
print(a)
a = int("-2025")
print(a)
#a = int("123.45") # Here we get value error due to point decimal carecter in middle which is other than digits.
print(a)
#a = int("Hello Programmers") #Value Error due to string.
print(a)
a = int(True)
print(a)
a = int(False)
print(a)
#a = int(5+6j) # Type Error due to complex data. (complex data cannot be converted to int)
print(a)
print(type(a))


'''
# float() conversion function
#------------------------------
a = float(10)
print(a)
a = float(142.38)
print(a)
a = float("-2025")
print(a)
a = float("2025")
print(a)
a = float("123.45")
print(a)
a = float("-123.45")
print(a)
#a = float("Hello Programmers") # Value Error due to string.
print(a)
a = float(True)
print(a)
a = float(False)
print(a)
#a = float(5+6j) # type error due to complex data.
print(a)
print(type(a))
'''

'''
# complex() convertion function
#-------------------------------
a = complex(10)
print(a)
a = complex(142.38)
print(a)
a = complex("2025")
print(a)
a = complex("123.45")
print(a)
#a = complex("Hello Programmers") # Value Error due to string
#print(a)
a = complex(True)
print(a)
a = complex(False)
print(a)
a = complex(5+6j)
print(a)
print(type(a))
'''

'''
# bool() conversion function.
#-----------------------------
a = bool(10)
print(a)
a = bool(142.38)
print(a)
a = bool("2025")
print(a)
a = bool(-2025)
print(a)
a = bool("123.45")
print(a)
a = bool("Hello Programmers")
print(a)
a = bool(True)
print(a)
a = bool(False)
print(a)
a = bool(5+6j)
print(a)
a = bool("")
print(a)
print(type(a))
'''

'''
# str() conversion function.
#----------------------------
a = str(10)
print(a)
a = str(142.38)
print(a)
a = str("2025")
print(a)
a = str("123.45")
print(a)
a = str("Hello Programmers")
print(a)
a = str(True)
print(a)
a = str(False)
print(a)
a = str(5+6j)
print(a)
print(type(a))
'''
