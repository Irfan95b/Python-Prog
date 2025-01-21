'''
    Python supports 4 types of integer data as Input.

        1. Decimal (0-9) --> Base-10 --> It is default number system.
        2. Binary (0 and 1) --> Base2 --> To provide Binary as input use 0b before value (0b1010 or 0B1010)
        3. Octal (0-7) --> Base8 --> To provide Octal as input use  0o before value ( 0o123 or 0O123 )
        4. Hexa-Decimal (0-9,a,b,c,d,e,f) --> Base16 --> To provide Hexa-Decimal as a input use 0x before value (0x1ae or 0X1ae)


    Since providing data in diffrent formats is very confusing and time consuming.
    In python we have built-in predefined functions to convert one number system to another.

        1. bin() --> converts to Binary
        2. oct() --> converts to octal
        3. hex() --> converts to Hexa-Decimal.

'''

a = 10

b = bin(a)
print("Binary value of a is {}".format(b))

b = oct(a)
print("Octal value of a is {}".format(b))

b = hex(a)
print("Hexa-Decimal value of a is {}".format(b))

