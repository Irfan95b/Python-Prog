
'''
 Write a python program to print using (end)

    Example for understanding
    -------------------------

        a=10
        b=20
        print(a)
        print(b)
        print(a+b)

        output: 
        10
        20
        30
            Here every print function is printing it new line. 
            by default every print function end's with new line charector (\n) 
            we can change the value of end by using end="<charector with which to be changed>"

'''

a = 10
b = 20

print(a)
print(b)
print(a+b)


print(a, end = "+")
print(b, end = "=")
print(a+b, end = "\n\n\t")


