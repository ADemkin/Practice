def make_printer(string):
    def inner():
        print(string)
    
    return inner


# create a function
a = make_printer('Hello')


# look inside a function
# print(type(a))
# -> <class 'function'>
# print(a)
# -> <function make_printer.<locals>.inner at 0x102448598>

# finally, open function
# a()
# -> Hello
# open function again
# a()
# -> Hello


# def print_text(string):
#     print(string)

def print_charcode(string):
    charcode = ''
    for letter in string:
        charcode += str(ord(letter))
    print(charcode)


def make_string_upper(func):
    def inner(string):
        func(string.upper())
    
    return inner


# print_upper_string = make_string_upper(print_text)
# print_upper_string('hellooo')
#
# print_upper_charcode = make_string_upper(print_charcode)
# print_upper_charcode('Hello')


@make_string_upper
def print_text(string):
    print(string)


# print_text('hello')
# -> HELLO

# b = print_text

# print(b)
# -> <function make_string_upper.<locals>.inner at 0x101a638c8>

# b('blabla')
# ->BLABLA


def html_tag(tag):
    def print_text(text):
        print('<%s>%s</%s>' % (tag, text, tag))
    
    return print_text


print_h1 = html_tag('h1')

# print(print_h1)
# <function html_tag.<locals>.print_text at 0x101d63950>
# print(type(print_h1))
# <class 'function'>

print_h1('Hello world!')

print_p = html_tag('p')

print_p('This is typical paragraph.')