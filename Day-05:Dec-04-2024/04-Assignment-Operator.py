'''
    In python '=' (Assignment Operator) used to assign Data or Value to the Variable.
    In Python we can assign any type of data to any variable directly without mentioning its Data Type.

    Data type is taken Automatically in python looking at Data or Value provided to the variable.
'''

# Write a program to Assign diffrent type of data to variables and Print.

StuName = 'Irfan Mohiuddin'
RollNo = 20
DOB = 12-07-1995
Percentage = 79.9
Addr = "Andheri Galli"

print("\n\t********** Student Details **********\n")
print("\t\tStudent Name : {}".format(StuName))
print("\t\tRollNo : {}" .format(RollNo))
print("\t\tDOB : {}".format(DOB))
print("\t\tPercentage : {}".format(Percentage))
print("\t\tAddress : {}".format(Addr))

print("\n====================================================================================\n")


# Write a program to assign same value to multiple variables in a single statement.

Var1 = Var2 = Var3 = 100

print("\n\n\t********** Assign Multiple Variables same value using single Statement **********\n")
print("\t\t\tVar1 : {}".format(Var1))
print("\t\t\tVar2 : {}".format(Var2))
print("\t\t\tVar3 : {}\n\n".format(Var3))

print("=========================================================================================")


# Write a program to assign multiple variable with diffrent values or Data in a single statement.

Var1, Var2, Var3 = 14, "Azeem Khan", 75.9 # Here Left most Variable gets assigned with Left most value or Data.

print("\n\n\t********** Assign Multiple Variables with Diffrent value using single Statement **********\n")
print("\t\t\tVar1 : {}".format(Var1))
print("\t\t\tVar2 : {}".format(Var2))
print("\t\t\tVar3 : {}\n\n".format(Var3))

print("\n\n\n")
