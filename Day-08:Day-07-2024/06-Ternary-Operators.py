'''
    Ternary Operator :-
    ----------------
        It is also known as Conditional-operator
        Ternary means 3
        It takes 3 values to perform operation

            Syntax :-
                (----)if(condition)else(----)

                (when true execute this part) if <Condition to check> else (when false execute this part)
                
'''

# Program to show execution of ternary operator.
a, b = 100, 50
result = "a is minimum" if(a < b) else "b is minimum"

print(result,"\n")


a = b = 11
result = "a is equal to b" if (a == b) else "a is not equal to b"

print(result)

