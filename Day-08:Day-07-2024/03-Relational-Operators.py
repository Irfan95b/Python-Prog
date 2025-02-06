'''
    Relational Operators:-
    --------------------
        These operators compares 2-values and gives True or False
        These operators are also called as Comparison Operators
            <	(less-than	a<b)
	        > 	(greater-than	a>b)
	        <=	(less-than or equals to	a<=b)
	        >=	(greater-than or equals to	a>=b)
	        ==  (Equals-to  a==b)
	        !=  (Not-Equals to  a!=b)
            
'''

a=11
b=3
print("{} < {} : ".format(a,b),a<b)
print("{} > {} : ".format(a,b),a>b)

print("{} <= {} : ".format(a,b),a<=b)     #11<3(F) or 11==3(F) (any one of them)
print("{} >= {} : ".format(a,b),a>=b)     #11>3(T) or 11==3(F)

print("{} == {} : ".format(a,b),a==b)
print("{} != {} : ".format(a,b),a!=b)

