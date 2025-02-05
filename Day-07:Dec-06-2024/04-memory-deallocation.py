'''
    deleting variable referanve

    del key word will delete the referance of variable pointing to value.
    when you redefine with the same value it will re-use the memory

    in python memory/data/value/object is re-used (no wastage of memory)

'''

a = 10
b = 10

print(a,b)

print(id(a))
print(id(b))

del a
del b

# a=b=10

a = None
b = None

print(id(a))
print(id(b))

print(a,b)

del a,b
