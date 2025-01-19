
'''
    In Python we also write Single statement in multiple lines.

    using (\) --> Back-Slash (Known as continuation charector)

    (we can also use De-limiter(;) to end the statement) can also work without De-limiter(;) also

    Note:
    ====
        Collection statements like [list], {set}, (tuple) in multiline does not required (\) continuation-char.
        Because these statements start and end with opening and closing brasses and also each data is supperated
        by other using a superator(,) .


'''
# Single Statement Multi Line.
a = 10
b = 5
c = 20

Sum = \
      a+\
      b+\
      c

print(Sum)

# Using List in MultiLine Statement.

Months = ["Jan", 'Feb', 'Mar', 
          'Apr', 'May', 'Jun', 
          'Jul', 'Aug', "Sep",
          '''Oct''',
          """Nov""", 'Dec']


print(Months)


