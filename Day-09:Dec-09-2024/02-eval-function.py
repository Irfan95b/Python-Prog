'''
    evel() - function :-
    -----------------
        It is special function, used to evaluate mathematical-expressions.
        It takes any type-of-data as input & provides respective data-type value
        It takes every-input as string-only.

        There are two uses of evel() - function
            1. Evaluate mathematical-expressions.
            2. Getting any type-of-data as input (auto data type converter).

        Note:
            When providing string data use quots("") compalsary.


'''

# Program to evaluate mathematical expression.
'''
a = eval(input("Enter any Math expression : "))
print("Result for the above expression is : ",a)
'''

# Program to convert data using eval() - function.

a = eval(input("Enter value for variable a : "))
print("Given 'a' value is : ",a, type(a));
