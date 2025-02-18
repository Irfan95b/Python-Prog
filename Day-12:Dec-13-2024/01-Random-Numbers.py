'''
    Random Number Generation Functions:-
    -----------------------------------
        Random number generation function is available in library name "random" need to import first.
            Ex:-
                import random
        Basically used to generate random numbers.
'''
#--------------------------------------------------------------------------------------------------
'''
    choice(sequence):-
        It gives random number or value from list, tuple, string.
        This function is present in random-module.

'''
# Program to demo ramdom.choice() :-
'''
import random

list1 = [11, 23, 32, 65, 1, 7, 88, 10];
print(random.choice(list1))

str1 = "Hello Welcome to python programming"
print(random.choice(str1))

# set1 = {1,2,3,4,5};
# print(random.choice(set1));	#set does not have indexes

list1 = ['azeem', 'Hakeem', 'Irfan', 'aleem', 'Muqeet']
print(random.choice(list1))
'''
#--------------------------------------------------------------------------------------------------
'''
    randrange(Start, Stop, Step) :-

        It gives random value from given range of values.
        This function is present in random-module.
        Here stop value is not-included in range or one less than the given range.
        step-value generates range of values with the given step jumps after each value.

'''
# Program to Demo randrange() :-
'''
import random

num = random.randrange(0, 100, 7)
print(num);

num = random.randrange(20)
print(num);

#num = random.randrange(20, -1)  # empty range error
#print(num);

#num = random.randrange(-15)     # empty range error
#print(num)

num = random.randrange(-20,-1)
print(num)
'''
#--------------------------------------------------------------------------------------------------
'''
    random() :-
        It generates a random float number b/w 0 to 1 (i,e till     0.0000  -  0.999999)
        This function is present in random-module.
'''
# Program to demo random():-
'''
import random

print(random.random());
print(random.random());
print(random.random());
'''
#--------------------------------------------------------------------------------------------------
'''
    uniform(x,y):-
        It gives a random float value between x and y or (less than y)
        This function is present in random-module

'''
# program to demo uniform(x, y) :-
'''
import random

num = random.uniform(0, 50);
print(num);

num = random.uniform(20, 0);
print(num);

# num = random.uniform(20);     # required two limits.
# print(num);
'''
#--------------------------------------------------------------------------------------------------
'''
    shuffle(variable_name) :-
        It will shuffle the values in a list
        It shuffles the values randomly
        This function is present in random-module
'''
# Program to demo shuffle() :-

import random

list1 = [21, 23, 34, 43, 54, 56, 72, 86, 33];
print(list1)

random.shuffle(list1);
print(list1)
random.shuffle(list1);
print(list1)
random.shuffle(list1);
print(list1)

list1 = ['azeem', 'Hakeem', 'Irfan', 'aleem', 'Muqeet']
random.shuffle(list1)
print(list1)

# str1 = "Hello Welcome to python programming"
# random.shuffle(str1);                             # Not supported.
# print(str1)

# set1 = {1,2,3,4,5};
# random.shuffle(set1)                                # Not Supported
# print(set1)

#--------------------------------------------------------------------------------------------------

