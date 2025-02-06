'''
    Logical Operators:-
    -----------------
        They checks/compares multiple conditions at a time and gives True or False
        They are 3-types
            1)  Logical and
            2)  Logical or
            3)  Logical not

        logical and     (if all conds. are True then True other wise False)
        logical or      (if any one conds. is True then True other wise False) 
        logical not	    (True is False & False is Ttrue)


        Truth Table :
        ------------

            Logical and :-
          .-----------------------------------------------.  
          |  (Condetion-1) | (Condetion-2) | logical and  |
          |-----------------------------------------------|
          |     True       |     True      |    True      |
          |     True       |     False     |    False     |
          |     False      |     True      |    False     |
          |     False      |     False     |    False     |
          |,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,|
          

            Logical or :-
          .-----------------------------------------------.
          |  (Condetion-1) | (Condetion-2) | logical or   |
          |-----------------------------------------------|
          |     True       |     True      |    True      |
          |     True       |     False     |    True      |
          |     False      |     True      |    True      |
          |     False      |     False     |    False     |
          |,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,|


            Logical not :-
          .--------------------------------.
          |  (Condetion-1) |  logical not  |
          |--------------------------------|
          |     True       |     False     |
          |     False      |     True      |
          "''''''''''''''''''''''''''''''''"


'''

# Program to show logical and behavior.

a=10;
b=20;

print(a>5 and b>5)	#T and T (True)
print(a>5 and b<5)	#T and F (False)
print(a<5 and b>5)	#F and T (False)
print(a<5 and b<5)	#F and F (False)

print()

# Program to show logical or behavior.

###
a=10;
b=20;

print(a>5 or b==20);	#T or T (True)
print(a>5 or b!=20);	#T or F (True)
print(a<5 or b==20);	#F or T (True)
print(a<5 or b!=20);	#F or F (False)

print()

# Program to show logical not behavior.

a=10
b=20

print(not (a==b));	#not F(True)
print(not (a!=b));	#not T(False)


'''
    NOTE:- (Special-cases)

        1. For non-boolean values,

            0,0.0(any-Zero) is False
            any Non-Zero is True (0.5,15,-9,-0.6)

-----------------------------------------------------------------

        2. (Empty-String) is False
            
            any-non-empty-string is True ("hi","123", "0","False")

'''
