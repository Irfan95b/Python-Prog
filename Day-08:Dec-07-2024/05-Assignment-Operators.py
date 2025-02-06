'''
    Assignment Operators:- (=)
    --------------------------
        It is used to assign a value to variable
        It is single(=) operator
        LHS=RHS (RHS-value is assigned to LHS-var)
            
            Example :-
            -------
                a = 10;
                b = 20;
                sum = a+b;

        Note:-
            We can perform multiple-var-assignments in single-statements.

                Example:-
                    a=b=c=10;
                    x,y,z=10,20,30;

        Special Case:-
            Compound Assignments: (operate and assign)
            It provides compound-assignments (Combine Assignments)
            Here we combine assignment-operator with other-operators

                Example:-
                    +=		(a+=b => a=a+b)
                    -=		(a-=b => a=a-b)
                    *=		(a*=b => a=a*b)
                    /=		(a/=b => a=a/b)
                    %=		(a%=b => a=a%b)
                    //=		(a//=b => a=a//b)
                    **=		(a**=b => a=a**b)
                
                Note:- Here in all-case b-value is not changed
                
'''

# Program to show assignment operation.
'''
a = 10;     # a is assigned with value 10
b = 20;     # b is assigned with value 20
sum = a+b;  # sum is assigned with value a+b i,e 30

print("a value is : {}".format(a));
print("b value is : {}".format(b));

print("a + b is : {}".format(sum));

'''


# Program to show multiple variables assignment in a single statment.
'''
# multiple variables same value
a = b = c = 25.63

print("Value assigned to a is : {}".format(a));
print("Value assigned to b is : {}".format(b));
print("Value assigned to c is : {}".format(c));

print()

# multiple variables different values
a, b, c = 100, "All the Best", 26.4+6j

print("Value assigned to a is : {}".format(a));
print("Value assigned to b is : {}".format(b));
print("Value assigned to c is : {}".format(c));

'''


# Program to show compound assignments.
a = 10
b = 3
a += b
print("For a += b value of a : {} value of b : {}\n".format(a,b))

a = 10
b = 3
a -= b
print("For a -= b value of a : {} value of b : {}\n".format(a,b))

a = 10
b = 3
a *= b
print("For a *= b value of a : {} value of b : {}\n".format(a,b))

a = 10
b = 3
a /= b
print("For a /= b value of a : {} value of b : {}\n".format(a,b))

a = 10
b = 3
a %= b
print("For a %= b value of a : {} value of b : {}\n".format(a,b))

a = 10
b = 3
a //= b
print("For a //= b value of a : {} value of b : {}\n".format(a,b))

a = 10
b = 3
a **= b
print("For a **= b value of a : {} value of b : {}\n".format(a,b))


