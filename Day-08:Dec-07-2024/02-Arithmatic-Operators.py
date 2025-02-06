'''
    A) Arithmetic Operators:-
        They take 2-values to perform the operation
        They are also called as (Binary Operators) -> 7-types, They are
            +   (Addition a+b)
        	-   (Subtraction a-b)
        	*   (Multiplication a*b)
	        /   (Division a/b) #Quot, till Rem is 0(approx) (deci-point)
	        %   (Modulo a%b)	 #Rem, if it is not-div 
	        //  (Floor-Division a//b) #Quot,if Rem is not div.. (only-int)
	        **  (Exponent or Power a**b, x power y)

'''

a=11;
b=3;
print("{} + {} : ".format(a,b),a+b);
print("{} - {} : ".format(a,b),a-b);
print("{} * {} : ".format(a,b),a*b);
print("{} / {} : ".format(a,b),a/b);		#Quot, till Rem is Zero(approx)
print("{} % {} : ".format(a,b),a%b);		#Rem, if Rem is not-divisible
print("{} // {} : ".format(a,b),a//b);	    #Quot, if Rem is not-divisible
print("{} ** {} : ".format(a,b),a**b);      # Exponent : 11x11x11 = 1331
print("------------------------------------------------------------------------------\n")

#--------------------------------------------------------------------------------------------------

# special cases :
# ---------------
'''
    1) Arithmetic-Operators(+,*) also supports string-additions & String-repetitions
        + oper supports str-additions
        * oper supports str-repetition
'''

a = "Hello"
b = "Welcome"

print(a + b);
print(a*3)
print(b*3)
print("------------------------------------------------------------------------------\n")

#--------------------------------------------------------------------------------------------------

'''
    2) Division(or Modulo) by 0:- 
        (div/0 or mod%0 ----> ZeroDivisionError)
            =-->    In python, anything divided by 0 (or) anything modulo by 0 is "ZeroDivisionError"
                    (it is not-def in python)

'''

a = 10
#print("{} / 0 : ".format(a),a/0)    # ZeroDivisionError
#print("{} % 0 : ".format(a),a%0)    # ZeroDivisionError

b = 10.34
#print("{} / 0 : ".format(b),b/0)   # ZeroDivisionError
#print("{} / 0 : ".format(b),b%0)   # ZeroDivisionError

