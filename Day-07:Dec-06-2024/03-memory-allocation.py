'''
                            Memory Allocation in python
                                        |
                 -----------------------+------------------------
                 |                      |                       |
    Same Variable diff value      Diff var same val           Diff value diff variable
    


'''

# Case 1 (Same Variable diff value)

a = 10
print(a)
print(id(a),"\n")

a = 22.34
print(a)
print(id(a),"\n")

a = "Hello bhai kaise ho"
print(a)
print(id(a),"\n")

# Here we can obsere that each data is stored in different memory location

#-------------------------------------------------------------------------------------

# Case 2 (different variable same value)

a = 254
print(a)
print(id(a),"\n")

b = 254
print(b)
print(id(b),"\n")

c = 254
print(c)
print(id(c),"\n")

# Here we can observe that if the different variables are holding the same value then the will be pointing to same memory address

#------------------------------------------------------------------------------------

# Case 3 (Different variables and different values)

a = 10
print(a)
print(id(a),"\n")

b = 25.4
print(b)
print(id(b),"\n")

c = 26+5j
print(c)
print(id(c),"\n")

# Here we can observe different values have different memory address.
