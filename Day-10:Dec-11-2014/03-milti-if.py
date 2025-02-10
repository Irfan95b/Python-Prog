'''
    Multiple-if Statements::-
        Here we use, multiple-if Statements one after the another
            Syntax:-
	            if <<condition1>>:
		            stmts;
		            stmts;
	            if <<condition2>>:
		            stmts;
		            stmts;
	            if <<condition3>>:
		            stmts;
		            stmts;	
	            next-line;
	            ......
	            ......	
Here, whichever condition is True, its corresponding indented-statements(block) are executed & comes to next-line o.w smts not-executed for False
It executes all the if conditions which are true.
'''

#Program to demo Multiple-if stmts with +ve,-ve,0

num = int(input("Enter any intiger number : "))

if(num>0):
    print("Given number is positive");
if(num == 0):
    print("zero is the key number to solve mathematical equations")
if(num<0):
    print("Given number is -ve")
if(num == 0):
    print("Given number is Zero")


print("End of program\n");
