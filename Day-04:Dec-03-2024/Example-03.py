
'''
 Write a python program to print using (sep)

    Example for understanding
    -------------------------

        a=10
        b=20
        print(a,b,a+b)

        output: 10 20 30
            comma(,) is a seperator
            so here in print function ,(comma) is used to saparate the values a b and a+b
            by default seperator(,) is set to space 
            we can change the value of seperator by using sep="<charector with which to be changed>"

'''

a = 10
b = 20

print(a,b,a+b)

print(a, b, a+b, sep =":")

print(a, b, a+b, sep = "^")

print(a, b, a+b, sep = "data to change")


