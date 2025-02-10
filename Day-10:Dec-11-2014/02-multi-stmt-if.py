'''
    Multiple statements in If condition:-
        
        For multiple statements in If all the statements should be in same sequence or indent from the left side.

        if not in same sequence then error will occure.

        Ex:-
            if(condition):
                stmt...............1
                stmt............2
                stmt.................3

'''
# multi line if statement.
'''
a = int(float(input("Enter a Value : ")))
b = int(float(input("Enter b Value : ")))

if (a > 0 or b > 0):
    sum = a+b;
    print("Sum of a and b is :", sum);

print("Out of if condition...\n");
'''

# special case
# Header and suite in single Line.

a = int(input("Enter any +ve integer : "));
if (a>0): print("Given Number is +ve Number");

print("End of the Prog");
