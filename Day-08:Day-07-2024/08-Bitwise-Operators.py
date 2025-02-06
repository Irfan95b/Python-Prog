'''
    Bitwise Operators:-
        These operators perform operations on bit-levels of given-numbers
        (Binary format 0,1)
        They are applicable only on int-types and boolean-types
        On other types we get Error

        They are 6-types:
            
            &  (bitwise-and a&b)
                    all bits are 1 it gives 1 other wise 0

            |  (bitwise-or a|b)
                    any one-bit is 1 it gives 1 o.w 0
            
            ^  (bitwise exclusive-or a^b) nor-operator
                    all bits are same it gives 0 o.w 1
            
            ~  (bitwise-complement ~a)
                    1 is 0 and 0 is 1
            
            << (bitwise-left-shift a<<b)
                    shifts bit-levels to left-side
            
            >> (bitwise-right-shift a>>b)
                    shifts bit-levels to right-side

        
        Each value is stored in 8 bits
            ex:
                a = 10

              .------------------------------------------------------------------------------------.  
              |  2^7(128)    2^6(64)    2^5(32)    2^4(16)    2^3(8)    2^2(4)    2^1(2)    2^0(1) |
              '....................................................................................'                            
     a = 10   |     0           0          0          0         1         0         1         0    |
     a = 18   |     0           0          0          1         0         0         1         0    |
              |
              |
              '.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.'
                
                bits for a = 10 = 1010
                    Hence for each value bits are stored in 8 bits format 
                        
                        a = 0 0 0 0 1 0 1 0 ==> 8+2 ==> 10
                    
                    simillarly for b = 18
                        b = 0 0 0 1 0 0 1 0 ==> 16+2 ==> 18


'''

#--------------------------------------------------------------------------------------------------

'''
Bitwise and(&):-
--------------
    Explanation for Bitwise operation of a = 10 and b = 18
    (If bit of both a and b are 1 then only 1 other wise 0)

         8-bits           128  64  32  16  8  4  2  1
         ---------------------------------------------
         a = 10            0    0   0   0  1  0  1  0
         b = 18            0    0   0   1  0  0  1  0
         ---------------------------------------------
         a & b             0    0   0   0  0  0  1  0
         ---------------------------------------------

         a & b = 0 0 0 0 0 0 1 0 ==> 2

'''
# Program to understand bitwise and (&) operation.
a = 10
b = 18
print()
print("a :", a, "b :", b);
print("Value after Bitwise operation of a & b is :", a&b);

#--------------------------------------------------------------------------------------------------

'''
Bitwise or(|):-
-------------
    Explanation for Bitwise operation of a = 10 or b = 18
    (If bit of any one eighter a or b is 1 then 1 other wise 0)

         8-bits           128  64  32  16  8  4  2  1
         ---------------------------------------------
         a = 10            0    0   0   0  1  0  1  0
         b = 18            0    0   0   1  0  0  1  0
         ---------------------------------------------
         a | b             0    0   0   1  1  0  1  0
         ---------------------------------------------

         a | b = 0 0 0 1 1 0 1 0 ==> 16 + 8 + 2 = 26

'''
# Program to understand bitwise or (|) operation.
a = 10
b = 18
print()
print("a :", a, "b :", b);
print("Value after Bitwise operation of a | b is :", a | b);

#--------------------------------------------------------------------------------------------------

'''
Bitwise xor(^):-
--------------
    Explanation for Bitwise operation of a = 10 xor b = 18
    (If bit of any one eighter a or b is 1 then only 1 other wise 0)

         8-bits           128  64  32  16  8  4  2  1
         ---------------------------------------------
         a = 10            0    0   0   0  1  0  1  0
         b = 18            0    0   0   1  0  0  1  0
         ---------------------------------------------
         a ^ b             0    0   0   1  1  0  0  0
         ---------------------------------------------

         a ^ b = 0 0 0 1 1 0 1 0 ==> 16 + 8  = 24

'''
# Program to understand bitwise xor (^) operation.
a = 10
b = 18
print()
print("a :", a, "b :", b);
print("Value after Bitwise operation of a ^ b is :", a ^ b);

#--------------------------------------------------------------------------------------------------

'''
Bitwise compliment(~) :-
----------------------
    Explanation for Bitwise operation of compliment a = 10 and compliment b = 18
    it will change the bits of given value as 1's to 0's and 0's to 1's

         8-bits           128  64  32  16  8  4  2  1
         ---------------------------------------------
         a = 10            0    0   0   0  1  0  1  0
         ---------------------------------------------
           ~a              1    1   1   1  0  1  0  1
         ---------------------------------------------
            ~a =  0 0 0 0 0 1 0 1  = 4+1 = 5
                    Here sign bit is at 5 position i,e 2^4 = 16
                    when the sign bit is 0 it means it is a positive value
                    and when it is 1 it means the value is -ve
                            
                            10 = 0 1 0 1 0
                                 |
                              sign bit

                           ~10 = 1 0 1 0 1
                                 |
                              sign bit
                        When sign bit is negetive we get -2^4 = -16 => -16+4+1 = -11

                        so the compliment of 10 (~10) is -11
                                                            

         8-bits           128  64  32  16  8  4  2  1
         ---------------------------------------------
         b = 18            0    0   0   1  0  0  1  0
         ---------------------------------------------
           ~ b             1    1   1   0  1  1  0  1
         ---------------------------------------------
            ~b =  0 0 0 0 1 1 0 1  = 8+4+1  = 13
                
                simillerly: -2^5+13 = -32+13 = -19

'''
# Program to understand bitwise compliment (~) operation.
a = 10
b = 18
print()
print("a :", a, "b :", b);
print("Value after Bitwise operation of ~a :", ~a);
print("Value after Bitwise operation of ~b :", ~b);

#--------------------------------------------------------------------------------------------------

'''
Bitwise Left shift (<<) :-
----------------------
    Explanation for Bitwise left shift operation of a = 10 and b = 18
    it will shift the position of each bit of the value to the given number of times to the left hand side.
    (moving out of order bits are ignored and empty left bits are replaced with 0)

         8-bits           128  64  32  16  8  4  2  1
         ---------------------------------------------
         a = 10            0    0   0   0  1  0  1  0
         ---------------------------------------------
           a<<2  0    0    0    0   1   0  1  0       
                           0    0   1   0  1  0  0  0
         ---------------------------------------------
           a<<2  =  0 0 1 0 1 0 0 0  = 32+8 = 40
  

         8-bits           128  64  32  16  8  4  2  1
         ---------------------------------------------
         b = 18            0    0   0   1  0  0  1  0
         ---------------------------------------------
         b << 2   0   0    0    1   0   0  1  0
                           0    1   0   0  1  0  0  0
         ---------------------------------------------
         b << 2 =   0 1 0 0 1 0 0 0  = 64+8  = 72

'''
# Program to understand bitwise Left shift (<<) operation.
a = 10
b = 18
print()
print("a :", a, "b :", b);
print("Value after Bitwise operation of a << 2 :", a << 2);
print("Value after Bitwise operation of b << 2 :", b << 2);
print()

#--------------------------------------------------------------------------------------------------

'''
Bitwise Right shift (>>) :-
----------------------
    Explanation for Bitwise Right shift operation of a = 10 and b = 18
    it will shift the position of each bit of the value to the given number of times to the Right hand side.
    (moving out of order bits are ignored and empty left bits are replaced with 0)

         8-bits           128  64  32  16  8  4  2  1
         ---------------------------------------------
         a = 10            0    0   0   0  1  0  1  0
         ---------------------------------------------
           a>>3                         0  0  0  0  1  0  1  0
                           0    0   0   0  0  0  0  1
         ---------------------------------------------
           a>>3  =  0 0 1 0 1 0 0 0  = 1 


         8-bits           128  64  32  16  8  4  2  1
         ---------------------------------------------
         b = 18            0    0   0   1  0  0  1  0
         ---------------------------------------------
         b >> 1                 0   0   0  1  0  0  1  0
                           0    0   0   0  1  0  0  1
         ---------------------------------------------
         b >> 2 =   0 1 0 0 1 0 0 0  = 8+1  = 9

'''
# Program to understand bitwise Right shift (>>) operation.
a = 10
b = 18
print()
print("a :", a, "b :", b);
print("Value after Bitwise operation of a >> 3 :", a >> 3);
print("Value after Bitwise operation of b >> 1 :", b >> 1);
print()
