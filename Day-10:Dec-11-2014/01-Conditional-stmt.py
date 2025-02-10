'''
    Conditional Statements:-
        They are also called as Branching stmts
        They executes indented-block-of-code 0 or 1 time only

            Ex:-
                if (condition):     # condition line is called Header
                    Statements to execute.
                    '           
                    '
                    '       #Indented block of code or suite.
                    '
                    '
                    all branch statements should be in same sequence of space.
                    from the left side. this is called indented block of code.

            Here if the statement is true, then the statements inside the condition or (Indented block) will execute.
            If the statement is false, then the statements inside the condition or (Indented block) will not execute.
            For the first line of condition or Header, ':' (colon) after the condition is mandatory but not ()-Brackets.

'''

# Program to Show simple execution of if condition.

# Program to print wellcome message to Irfan only.

name = input("Enter your name : ");

if name == 'Irfan':
    print("***** Hello",name,"*****\n","Welcome to Python Programming\n");

print("I am Out of Condition");

