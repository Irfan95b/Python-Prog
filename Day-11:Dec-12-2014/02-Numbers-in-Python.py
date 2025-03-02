'''
    Numbers in Python:-
        Numbers means/is numeric-values
        Python supports 3-types of numeric-values or numeric data.

            	a) intiger type (10)
	        b) float type or decimal (10.5)
	        c) complex-type (5+6j)

    For different numeric data values, we have numeric- data type-conversion funcs.
        a) int()
	b) float()
	c) complex(a)	---> a+0j
	d) complex(a,b) ---> a+bj

'''

# example program for numeric data type convertion.
'''
num = input("Enter any number : ")
print("Type of data you entered : ", type(num));

num = int(num);

print("After converting to int  :",num,"Type",type(num));

num = float(num)
print("After converting to float  :",num,"Type",type(num));

num = complex(num)
print("After converting to Complex  :",num,"Type",type(num));
'''
#--------------------------------------------------------------------------------------------------

'''
    Mathematical Functions in Py-Numbers:-
        Python provides different functions, using which we can perform mathematical-operations.
        Python provides "math.py", pre-defined module(lib-module-file)
        Here we have diff-math-funcs
            Ex:-
                square-root
                logarithm
                trignometric
                factorial
                etc...

    *** How to use a lib-module ?
    ---------------------------
        Step1.
        ======
        To import any module in python programming use "import" and the module name.
            syntax:-
                import <module name>

                Ex:-
                    import keyword;

                    import math;

        Step2.
        ======
        To use respective functions related to module use "module_name" dot "function_name"
            syntax:-
                <module name>.<function_name>

                Ex:-
                    ketword.kwlist;

                    math.sqrt(100)

                    math.pi

'''

# Program to demo different Mathematical-Functions


# abs(x):-
'''
# It gives the absolute +ve value of the given number x
print(abs(-9))
print(abs(9));
print(abs(0));
print(abs(-0));
print(abs(-9.5));
print(abs(9.5));
print(abs(0.0));
print(abs(-0.0));
print(abs(23+7j));
'''

# ceil(x):-
'''
# It gives proper-integer-value which is greater-than or equals to given value
# It is in math module required import it.

import math

print(math.ceil(9.8));
print(math.ceil(9.0));
print(math.ceil(9));
print(math.ceil(-9));
print(math.ceil(-9.8));
print(math.ceil(-9.2));
print(math.ceil(-9.0));
#print(math.ceil(23+7j));  # cannot convert complex to float
'''

# factorial():-
'''
# it gives factorial of given number
import math
print(math.factorial(5))
print(math.factorial(6))
'''

# exp(x):-
'''
# It gives exponential of x (e power of x)
# exp() function (e--->Euler's number) (e power x)
import math;
print(math.exp(0));
print(math.exp(1));
#We get exact e-value(2.718281828459045)
'''

# fabs(x):-
'''
# It gives absolute value (+ve) of x
# it is mainly used on float-value(also works on int-values)
import math;
print(math.fabs(3));
print(math.fabs(-3))
print(math.fabs(3.5))
print(math.fabs(-3.5));
print(math.fabs(0));
print(math.fabs(-0));
# print(math.fabs(23+7j));        # can't convert complex to float
'''

# floor(x):-
'''
# It gives nearest-integer-value which is less than or equals to given-value
import math;
print(math.floor(9.8));
print(math.floor(9.0));
print(math.floor(9));
print(math.floor(-9));
print(math.floor(-9.8));
print(math.floor(-9.0));
print(math.floor(-9.2));
# print(math.floor(23+7j));  # can't convert complex to float
'''

# log(x):-
'''
# It give natural logarithm value of x (log to the base-e)
# and x>0 (compulsory)
import math;
print(math.log(10))
print(math.log(math.exp(1)));
print(math.log(1))
# print(math.log(-10));	    #ValueError(-ve no)
'''

# log10(x):-
'''
# It give logarithm value of x (base-10)
# and x>0 (compulsory)
import math;
print(math.log10(10));
print(math.log10(1));
print(math.log10(100));
print(math.log10(1000));
# print(math.log10(-10));	#ValueError
'''

# max(x,y,z,...):-
'''
# It gives maximum value from given arguments.
print(max(10,20,30));
print(max(-10,-20,-30));
print(max(10.5,20.5,30.5));
print(max(-10.5,-20.5,-30.5));
# print(max(-10.5,20,-21,34+6j,54))     # error not supported
'''

# min(x,y,z,...):-
'''
# It gives minimum value from given arguments.
print(min(10,20,30));
print(min(-10,-20,-30));
print(min(10.5,20.5,30.5));
print(min(-10.5,-20.5,-30.5));
'''

# pow(x,y):-
'''
# Gives x to the power of y
import math;
print(math.pow(10,3));
print(math.pow(-10,3));
print(math.pow(10,-3))
print(math.pow(100,0.5));	#it is 10 power 0.5(1/2) i.e. sqrt(100)
'''

# sqrt(x):-
'''
# It gives square-root of given number (x>0)
import math;
print(math.sqrt(100));
print(math.sqrt(81));
#print(math.sqrt(-10));		#ValueError(-ve)
'''

import math;
print(math.pi)
print(math.e)
#exact value of pi 3.141592653589793
