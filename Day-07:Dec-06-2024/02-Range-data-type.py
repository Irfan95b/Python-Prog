'''
    Range Data Type:
    ================
      Range data type is a derived data type used to generate range of values or sequence of values.
      Here range() --> function is used to define a range data type.

      Syntax:
        range(begining-value, end-value, step-value)
            
            begining value is by default is zero.
            end value is to be mentiond compalsary.
            step value is by default set to +1.

      Example:
        r1 = range(11, 66, 11)

            r1 = [11, 22, 33, 44, 55]

            range data type always takes 1 value less than the given limit.
            Here 66 is the given limit, so 55 will be the last value in range.

      We can access the values from range coll, using indexes.

                                Index
                                  |
            |''''''''''''''''''''''''''''''''''''''''''''|
     +ve indexing                                -ve indexing
     (0 - n-1)                                   (-1 - n)
     First to Last                               Last to First
     Forword direction                           Backword direction


        r1 = [11, 22, 33, 44, 55]
              0   1   2   3   4  --> +ve indexing or Forword indexing.
              -5  -4  -3  -2  -1 --> -ve indexing or Backword indexing.

        r1[0] = 11 = r1[-5]
        r1[1] = 22 = r1[-4]
        r1[2] = 33 = r1[-3]
        r1[3] = 44 = r1[-2]
        r1[4] = 55 = r1[-1]

    range values are immutable (original data of range in any index cannot be modified)
        
        Example:
            r1[3] = 20   # Type error (range values are immutable).


    NOTE:-
        ***= best-way to access values of range-coll is with loops
        Ex:-
	        for i in r:		#each-value from "r" is assigned to "i"
		        print(i);   (#when no-values in range(r) then come out of loop)

    NOTE:-
        1)	range(Begin-value,End-value,Step-value)
            Begin-value(not-compulsory) -> default-value(0)
            End-value(compulsory) -> not-included
            Step-value(not-compulsory) -> default-value(+1) [+ve or -ve]

        2) best-way to access values of range-coll is with loops
            Ex:-
	            for i in r1:	#each-value from "r1" is assigned to "i"
		            print(i);	#and loop-stmts are exec.
                                (#when no-values in range(r1) then come out of loop)


        3) Trying to access, range-coll-value with index-out-of-range, we get "IndexError"

'''
#---------------------------------------------------------------------------------
'''
# 01. Simple program to define and print range data type.

r1 = range(1, 6, 1)
print(r1)
print(type(r1))


# 02. Program to print the values in given range using indexes access

print(r1[0])
print(r1[1])
print(r1[2])
print(r1[3])
print(r1[4])
#print(r1[100])		#IndexError (index out-of-range)
print()
print(r1[-1])
print(r1[-2])
print(r1[-3])
print(r1[-4])
print(r1[-5])
#print(r1[-100])	#IndexError
print()
'''
# different casses and observations of definig a range
#----------------------------------------------------------------------------------
'''
# The best way to access the range values is using loops.


r1 = range(1, 10, 2)        # (step value is 2 i.e, 1, 3, 5, 7, 9)
print("Range values using loops")
j = 0
for i in r1:
    print ("r1[{}] : ".format(j),i)
    j += 1
print("Out of the loop")
'''
#------------------------------------------------------------------------------------
'''
r1 = range(10,20,2);     # 10,12,14,16,18 (begining from 10 and Step-value=2)
j = 0
for i in r1:
    print ("r1[{}] : ".format(j),i)
    j += 1
print("Out of the loop")
'''
#------------------------------------------------------------------------------------
'''
r1 = range(20)          # default begining value is 0, and default step value is +1

j = 0
for i in r1:
    print ("r1[{}] : ".format(j),i)
    j += 1
print("Out of the loop")
'''
#------------------------------------------------------------------------------------
'''
r1 = range(1, 20, -3) # there wont be any error but due to step value is negetive range will not be generated.
j = 0
for i in r1:
    print ("r1[{}] : ".format(j),i)
    j += 1
print("Out of the loop")

print(type (r1))
'''
#------------------------------------------------------------------------------------
'''
r1 = range(-10, -20, -2)    # -10, -12, -14, -16, -18
j = 0
for i in r1:
    print ("r1[{}] : ".format(j),i)
    j += 1
print("Out of the loop")
'''
#------------------------------------------------------------------------------------
'''
r1 = range(20,1,2);     #range not generated
for i in r1:	        #20,1(backward-range) but +2(Farward-step)
	print(i);
print("Out of the loop")
'''
#------------------------------------------------------------------------------------
'''
r1 = range(-10) # default step value is +1
j = 0           # range will not be generated.
for i in r1:
    print ("r1[{}] : ".format(j),i)
    j += 1
print("Out of the loop")
'''
#------------------------------------------------------------------------------------
'''
r1 = range(1,11)    # range is immutable, means organized data cannot be modified.
print(r1[0])
print(r1[9])

r1[0] = 10      # otherwise TypeError

print(r1[0])
'''
#------------------------------------------------------------------------------------
'''
r1 = range(-1, -6, -1)      # -1, -2, -3, -4, -5
j = 0
for i in r1:
    print ("r1[{}] : ".format(j),i)
    j += 1
print("Out of the loop")
'''


