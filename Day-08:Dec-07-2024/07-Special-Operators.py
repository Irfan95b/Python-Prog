'''
    Special Operators :-
        We have two types of special operators:

            1. Identity Operator (is, is not)   
                checks address is same or not, if same returns True else False.
                It is used for address comparison

                    Ex:-
                        a is b      (if addr of a and b is same return True)
                        a is not b  (if addr of a and b is not same we get True)
            
            2. Membership Operator (in, not in) 
                checks given-value is in collection or not if available return True else False
                It checks whether given value/obj is present or not in given collection
                we can check the use it with collection of data in (String, List, Set, Tuple or Dict)
                    
                    Ex:-
                        "h" in "hello" (True)
                        10 not in [20, 10, 30, 40] (False)

        In both cases we get True / False


'''

# Program to show Identity operator.
'''
# is | is not

a = 10
b = 10

print("addr of a :",id(a),"a is b :",a is b)
print("addr of b :",id(b),"a is not b :",a is not b)

print();

c = 100
d = 20

print("addr of c :",id(c),"c is d :",c is d)
print("addr of d :",id(d),"c is not d :",c is not d)
'''

# Program to show membership operator.

# in | not in

string = "Hello and Welcome";

print("\nGiven string is :",string);
print();

print("'H' in string :", 'H' in string)
print("'z' in string :",'z' in string);
print("'x' not in string :",'x' not in string);
print("'and' in string :",'and' in string);
print("'or' in string :",'or' in string);
print("'HW' in string :",'HW' in string); #takes single-word(F)
print("' ' in string :"," " in string);
print()

list1=[10,20,30,"Sai",6.0,True];
print("Given List is :", list1);
print();

print("10 in list :", 10 in list1);
print("100 not in list :", 100 not in list1);
print("'Sai' in list :", "Sai" in list1);
print("'Ram' not in list :", "Ram" not in list1);
print("True not in list :", True not in list1);
print("'S' in list :", "S" in list1)
print("'sai' in list :", "sai" in list1)
print("6.0 not in list :", 6.0 not in list1)
print("'ai' in list[3]", 'ai' in list1[3])
print();
