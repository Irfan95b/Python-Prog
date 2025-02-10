'''
    Iterative Statements:-
    (Looping-stmts) or cyclic-stmts
    -------------------------------
        They are used to execute group-of-statements(indented block-of-code) 0 or more times based on condition/values
        We have 2-types of Iterative-Stmts,
            i) for loop
            ii) while loop

        (do-while or foreach-loop are not in python)

        1. for loop :-
        ------------
            This loop is executed based on collection-of-values
                ex:-
                    Strings, List, Tuple, Set, Dictionary, Arrays, Range etc.

                Syntax:-
                    for x in <coll-of-values>:  [11,22,33]
                        stmts...
                        .......
                        ........

                Here loop group-of-stmts are executed for each-value in collection
                (each time coll-value is assigned to loop-var(x))
        ---------------------------------------------------------------------------------------------------
        2. while loop :-
        --------------
            This loop-stmts is executed(block-of-code) based on a condition (till it is false)
            (here we use loop-var initial-value, condition-check, incre/decre)
                Syntax:-
                    loop-var-inital-value;		------> (1) once
	                while condition(T/F):		------> (2) T/F
		                stmts;
		                stmts;			--------------->(3) block/body
		                .....
		                incre/decre; ----------------->(4)

                step1(only-once)
                steps2,3,4 (exec-multi-times) till step2 is False

'''

# Program to demo for-loop
'''
str = "Hello"

for a in str:
    print(a)

print("End of For Loop")
'''
# demo2-----------------------------------
'''
for x in range(10):     #0 to 9
	print("Irfan");
'''

# Demo3 ------------------------------
'''
print()
#N-natural-nos
for x in range(1,101):     #1 to 100
	print(x);
'''

#for loop single-suite-stmt (header & suite in single-line)
'''
for x in range(1,11): print(x*x);
'''

#for loop with list-coll
'''
for x in [11,22,33,44,55,66,77,88]:
    print(x)

print("Comes out of the Loop");
'''
# =================================================================================================

# Program to demo using while-loop
#printing N-natural-no's
'''
i=1;

while i<=10000:
	print(i);
	i=i+1;
print("End of While Loop");
'''

#while loop single suite stmt
#Header & suite in single-line

i = 0;

while i<=100: print(i); i+= 5;
