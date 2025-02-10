'''
    Nested if condition:-
        We can use "if-else-stmts" inside another if-stmt or else-stmt as follows, This is called as Nested if-else.

        Syntax:-
            if condition1:(T)
	            stmts;
	            if condition2:(T)
		            inner-stmts;
		            .....
            else:
	            stmts;
	            if condition3:
		        inner-stmts;
		        .....

=** here if both conditions(outer-if,inner-if) are True then only its inner indented(block) stmts are executed o.w else with if-stmts are executed
'''

# Program to check biggest of 3 numbers using nested-if)
'''
a = int(input("Enter 'a' value : "))
b = int(input("Enter 'b' value : "))
c = int(input("Enter 'c' value : "))

if(a > b):
    if(a > c):
        print("'a' is Greater")
    else:
        print("'c' is greater")
else:
    if(b > c):
        print("'b' is Greater")
    else:
        print("'c' is Greater")
'''

# WAP to print smallest of 3-diff-numbers using nested-if stmts

a = int(input("Enter 'a' value : "))
b = int(input("Enter 'b' value : "))
c = int(input("Enter 'c' value : "))

if (a < b):
    if(a < c):
        print("'a' is Smalest");
    else:
        print("'c' is Smalest");
else:
    if(b < c):
        print("'b' is Smalest");
    else:
        print("'c' is Smalest");


