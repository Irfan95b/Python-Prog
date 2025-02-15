'''
    Infinite While-Loop:-
        A loop which is always true is called Infinite Loop
        (never-ending-loop)
            Ex:-
                while True:		#while 10==10: (10): ("hi"):
		            ....
		            body;
		            ....
    NOTE:-
        (Ctrl+c) is used to break or come out of infinite loop
        (ctrl+Pause-break-key)

'''

# (Program to demo Infinite-Loop while)
'''
i = 1;
while True:
    print(i)
    i += 1;

print("Out of loop\n");
'''
#--------------------------------------------------------------------------------------------------

'''
    Nested Loops:-
        Using a particular loop inside another loop is called Nested-Loop
        (loop with-in loop)
            Syntax:-
                outer-loop:             # represents no.of.rows
                    stmts.....;
                    inner-loop: 	    # represents no.of.cols
                        stmts;
                        '
                        '
        NOTE:-
            Nested-Loops are mainly used to represent data in the form of rows and columns, table-data, matrices data etc..
            Here outer-loop represents no.of rows and inner-loop represents no.of columns

'''

# Program to demo Nested-Loops
'''
for i in range(5):			                #outer-loop(0,1,2,3,4) => rows(i)
	for j in range(5):		                    #inner-loop(0,1,2,3,4) => cols(j)
		print(i,",",j,sep="",end="\t");
	print("\n");

print("End of Program")
'''
#--------------------------------------------------------------------------------------------------

'''
    (Transfer Stmts) in Control Statements:-
    (Jump Stmts)
        (jumping from one-line to another-line in prog...)
            3 - Types
                a. break
                b. continue
                c. pass

    break stmt:- 
    ----------
        (mainly used in loops(for/while) with if-cond...)
        It is used to STOPs-loop & comes out of looping-stmts using some condition
        (Termination/Exit of Loop)
            Syntax:-
                loop:
	                if cond:
		                break;
        it skips remaining stmts of current-iteration(cycle) & also skips remaining all iterations(cycles)
    Note:-
        The best-way(correct-way) to stop (or) come out of Infinite-Loop is with break-stmt(using cond..)

'''
# Program to demo break-stmt in Loops
'''
i=1
while i<=100:
	if i==51:
		break;
	print(i)        #odd-nums
	i=i+2;

print("\nBreaked out of loop")
'''

#using infinite while loop
'''
i=2
while True:
	if i==52:
		break;
	print(i)        #even-nums
	i=i+2;

print("\nBreaked out of infinite-loop")
'''
#--------------------------------------------------------------------------------------------------
'''
    continue stmt:-
        (mainly used in loops(for/while) with if-cond...)

        Syntax:-
            loop:
                stmts.....
                '
                '
                if cond:
                    continue;
                stmts.....
                '
                '

        It is used to skip current-cycle-stmts and continues with next-iteration(cycle)
    
'''

# Program to demo continue-stmt in Loops

#using while-loop
'''
i=1
while(i<=100):
    if i%2==1:  #odd-continue
        i=i+1;
        continue
    print(i)
    i=i+1
'''

# using for loop
'''
for x in range(1,101,1):
    if x%2==0:  #even-continue
        continue
    print(x)
'''
#--------------------------------------------------------------------------------------------------
'''
    pass statement:-
    --------------
        Syntax:-
            if (cond):
                pass;		----> suite(body w.o stmts)
    
    A pass statement in Python is used to do "nothing". It is a null statement that returns no operation. 
    Occasionally, a pass statement plays the role of a placeholder when implementing new methods.

    The pass statement is generally not that useful in Python and does not make a difference in the code 
    except for making it shorter.
'''

# Program to demo pass-stmt in program with Loops
'''
for x in range(1,101):
	if x%3==0:
		print(x);
	else:
		pass;

'''

