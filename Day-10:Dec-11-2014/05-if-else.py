'''
    if-else statement:-
        (Here we have 2nd option also)
            Syntax:-
	            if condition:
		            True-Stmts;
		            .....
	            else:					#here : is mandatory
		            False-Stmts;
		            .....
	            .....
	            next-line
	            .....
	
    Here if condition is true then True-Stmts are executed,
    if condition is False then False-Stmts are executed
    (and comes to next-line)

'''

# Program to demo if-else statement.
'''
name = input("Enter your name : ")
print(name)

if (name == 'Irfan'):
    print("***** Hello",name,"*****")
    print("Welcome to Python Programming")
else:
    print("Hay",name)
    print("Please Dont touch this laptop")
    print("If you repeat same")
    print("I will notify to Irfan about This, Be carefull!!!!!!")
'''


# Program to write if-else with single line statement.
num = int(input("Enter any value : "))

if (num != 0): print("You have enterd a non zero number\n")
else: print("You have enterd a zero\n")

print("Thank You!")

