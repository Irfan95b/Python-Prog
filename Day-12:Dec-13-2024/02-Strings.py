'''
    Strings in Python:-
        String is collection-of-chars, represented in quotes.
            Example:-
                single-quotes'...'  (Use single-quotes for single-word)
	            double-quotes"..." (Use double-quotes for multi-words or 1-line)
	            triple-quotes '"...."' (multi-line-text) #compulsory triple qoutes for """.....""" for multi lines text.
	                (single-triple-quotes/double-triple-quotes)

        Note 1:-
            Python does not support char-dtype.
            Even single-char is also taken as string-dtype

        Note 2:-
            in triple-quotes string, no need to use \t or \n chars. they are taken auto. wrt given-text
            inside triple-quot-str # is taken as single-char but not single-line-comment.
            to represent quotes with-in quotes,
                use one-type-quotes in another(but not same type of quotes) #combination(diff) of quotes
            However we can use same-type-of quotes inside same-type of quotes using \ (ESC-SEQ-char) or (Back shash char)
'''
# Program to demo Data Type of charecter or strings in python.
'''
# charecter.
char = 'z'

print(char, type(char));

# Single line string.
str = "welcome to python"
print(str, type(str))

# multi line string.

str = """
        Hello
        Wellcome to
        Python.
        """
print(str, type(str))
'''

# quotes with-in quotes

# Str = 'Hi Hello Welcome 'Irfan'' # Error
# print(Str);


Str = 'Hi Hello Welcome \'Irfan\''
print(Str);

Str = 'Hi Hello Welcome "Irfan"' 
print(Str);

Str = '''
        Hi
        'Welcome'
        to
        "Python"
        """programming"""
        '''
print(Str)

Str = """
        Hi
        'Welcome'
        to
        "Python"
        \"""programming\"""
        """
print(Str)

Str = """
        Hi
        'Welcome'
        to
        "Python"
        '''programming'''
        """ 
print(Str)


