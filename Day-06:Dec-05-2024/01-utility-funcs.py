
'''
    type() --> Function:
    -------------------
        Since in python Data-type is automatically applyed as per the data given to the variable
        to see the Data-type we use "type()" function.

    id() --> Function:
    -----------------
        All the variables defined will be pointing to some unique memory address or location were the value
        to be stored in memory, This address specified to variable automatically by PVM.
        To see this address we use "id()" function.

    print() --> Function:
    --------------------
        It is used to print any data as a out put.

'''

a = 100
b = 20.43
c = "All The Best"
d = 6+5j
e = True

print("\n----------------------------------------\n")
print("Data available Variable a is {}" .format(a))
print("Data Type of a is ",type(a))
print("Address of a is ",id(a))

print("\n----------------------------------------\n")
print("Data available Variable b is {}" .format(b))
print("Data Type of b is ",type(b))
print("Address of b is ",id(b))

print("\n----------------------------------------\n")
print("Data available Variable c is {}" .format(c))
print("Data Type of c is ",type(c))
print("Address of c is ",id(c))

print("\n----------------------------------------\n")
print("Data available Variable d is {}" .format(d))
print("Data Type of d is ",type(d))
print("Address of d is ",id(d))

print("\n----------------------------------------\n")
print("Data available Variable e is {}" .format(e))
print("Data Type of e is ",type(e))
print("Address of e is ",id(e))

print()


