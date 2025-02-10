'''
    if-elif-else:-
        Syntax:-
        	if condition1:
		        stmts1;
	        elif condtion2:
		        stmts2;
	        elif condtion3:
		        stmts3;
	        ....
	            ....
	        else:
		        F/stmts;
	        next-line;(comes-out-of-CS)
            ......

Here linearly one after the other conditions are checked.
Whichever condition is true, corresponding stmts are executed and remaining conditions are skipped till end.
If no-condition is true then last else part is executed.

'''
#Program to accept 5 subject marks of a student and print the grade Distinction,1st-class,2nd-class,3rd-class or Fail
#Program to demo If-elif-else
'''
print("***** Enter marks of 5 subjects of Student *****\n");

sub1 = int(input("Enter subject1 marks : "));
sub2 = int(input("Enter subject2 marks : "));
sub3 = int(input("Enter subject3 marks : "));
sub4 = int(input("Enter subject4 marks : "));
sub5 = int(input("Enter subject5 marks : "));

print("Total scored out of 500 is : ",sub1+sub2+sub3+sub4+sub5)

Total = (sub1+sub2+sub3+sub4+sub5)//5

if Total>=75 :
    print("Passed with Distinction")
elif Total >= 60:
    print("Passed with 1st class grades")
elif Total >= 55:
    print("Passed with 2nd class grades")
elif Total >= 45:
    print("Passed with 3rd class grades")
else:
    print("Got failed, Try harder in next exams")

'''

#WAP to accept age of person and print following msgs
#(Baby, Kid, Teenage, Adult, Oldage)

age = int(input("Enter the age : "))

if(age >= 65):
    print("\n..I Think he is old person")
elif(age>=18):
    print("\n..I Think he is an adult")
elif(age>=12):
    print("\n..I Think he is a Teenager")
elif(age>=5):
    print("\n..I Think he is a kid")
else:
    print("..I Think he is baby")


'''
    NOTE:-
        if-elif-else stmt is very efficient & fast when compared to multiple-if-stmts (or) nested-if-stmts because here other-conditions are not-checked un-necessarily
'''
