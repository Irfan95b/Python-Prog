'''
    String Operations:-
    -----------------
        Strings supports indexes.
        Python supports both +ve or -ve indexes
        +ve indexes are First to Last (L->R) (Forward) (0 to n-1)
        -ve indexes are Last to First (R->L) (Backward) (-1 to -n)
        we use index with [] subscript-operator/index-oper
            Ex:-
                str = "Hello"
                      [01234]   --> 0 to n-1     (Forword indexing) (Left to Right) +ve indexing
                      H e l l o  
                    [-5-4-3-2-1] --> -1 to -n    (Backword indexing) (Right to Left) -ve indexing
        
        Getting or Accessing chars from string is done in 2-ways
            a). using indexes.
                    Syntax:
                        str[index_num]
            b). using slicing
                    Syntax:
                        str[big-index : end-index : step-index]
                            
                          ->  This acts like sub-string
                          ->  beginIndex is starting-index with in the string.
                          ->  endIndex is (last-index - 1) with in the string or where to stop.
                          ->  step-index is increment-value or jumping the index (default is +1)
                    Note:-
                        If beginIndex is not given then it will take from 0-index.
                        If endIndex is not given then it will take till last-index.
                        Default step-Index is +1.

        Note:-
            The best way to access elements of any collection is with loops(For-loop)
            
'''
# Demo program to show string indexing.
'''
ss = "Hello";
print(ss);
print(ss[0]);   # 0,1,2,3,4
print(ss[-1]);  #  -1,-2,-3,-4,-5
# print(s[10]);	#IndexError (string index out of range)
print(ss[0]); 
print(ss[1]); 
print(ss[2]); 
print(ss[3]); 
print(ss[4]); 
print()
print(ss[-1]); 
print(ss[-2]); 
print(ss[-3]); 
print(ss[-4]); 
print(ss[-5]); 
#print(ss[10]);	    #IndexError (out-of-range) 
#print(ss[-10]);	#IndexError 

# Demo using loops

for x in ss:
	print(x);
'''

# Demo program to show string slicing.
'''
str = "Welcome to Python";
print(str[::])
print(str[1::])
print(str[:6:])     # end index is always n-1
print(str[::2])
print(str[:])
# print(str[])        # Error
print(str[4:12:1])
print(str[4:12:3])  # o 
print(str[::-1])    # print in backword order
print(str[14:3:-2]) # hy teo
print(str[::-2])    # nhy teolw
print(str[-1:-9:-1])# nohtyp o
print(str[-1:-9:-2])# nhy 
print(str[-9:-1:-1])# no output
print(str[1:0:2]); # no output
'''
#--------------------------------------------------------------------------------------------------

'''
    Strings with Mathematical Operators:-
        + operator is used for string concatenation(addition)
        * operator is used for string repeatition

'''
# Demo program to show string mathematical operations in python.
'''
F_Name = 'Mohammed '
M_Name = 'Irfan '
L_Name = 'Mohiuddin\n'

Full_Name = "My name is ";

Full_Name += F_Name + M_Name + L_Name;

print(Full_Name)

print(Full_Name * 5);

# print(F_Name * L_Name); # Error
'''
#--------------------------------------------------------------------------------------------------
'''
    Length of a String:-
        To get number of charectors in a string.
        len() function  gives length of a string.

    Ex:-
        str = 'this is string'
        print(len(str)).
'''
# Program to demo string length function.
'''
F_Name = 'Mohammed '
print(len(F_Name))
M_Name = 'Irfan'
print(len(M_Name))
L_Name = 'Mohiuddin\n'
print(len(L_Name))
'''
#--------------------------------------------------------------------------------------------------
'''
    Checking/Finding/Searching String:-
        To Check whether given string or char is present in original-string or not
        It is done with "in" or "not in" operator. (membership-operators) True/False.
'''
# Program to work with strings(check/find/search) in, not-in operator
'''
str = "Hello Students, Welcome to Python Class";

print("to" in str);         # True
print("," in str);          # True
print("hi" in str);         # False
print("hello" in str)       # False     #case-sensitive
print("Python" not in str); # False
print("HW" in str)          # False     #2-diff-chars but not single-word
print()
print("welcome" not in str) # True      #case-sensitive
print(" " in str)           # True
print(" " not in str)       # False
print("" in str)            # True      #empty-str in str

# print("" in str) because an empty string is considerd a sub string for every sring.
# an empty sring is considered to be present at every position in any string, i.e before and after each charecter in string.
'''
#--------------------------------------------------------------------------------------------------

'''
    Counting all sub-strings in main-string:-
        It is done with count() method/function (beginIndex & endIndex also taken)
        it gives count of sub-string in original-string

            str = "Hello Welcome to Python Hello users"
        Syntax:-
            str.count("sub-string", big-index, end-index)
            Ex:-
                print(str.count("Hello",6,23));

'''

# Program to work with string-functions or methods
'''
str = "Hello Welcome to Python Hello users";
print(str.count("Hello"));
print(str.count("Hello",6));
print(str.count("Hello",6,23));
print(str.count("Hello",2,25));
print(str.count("Welcome",6));
print(str.count("Welcome",8));
# print(str.count("Hello", ,13));   # Error invalid syntax.
'''
#--------------------------------------------------------------------------------------------------
'''
    Replacing a String with another string:-
        It is done with below method
            Syntax:
                str.replace(old-str, new-str)

                it replaces old string with new string in original-string and we get new-string.

            Note:
                String value(object) are immutable-obj
                org-str cannot be modified but can be re-assigned.
                Any changes done to org-str, new str-obj is created.
                Hence in replace(), we got new-str after replace

'''
# Replacing old-str with new-str

str = "Hello, Welcome to Python, Hello users";
print("Before replace : ", id(str))
str = str.replace("e", '*');
print(str)
print("After replace : ", id(str))

str1 = str.replace('H*llo', 'Hi');
print(str)
print(str1)

