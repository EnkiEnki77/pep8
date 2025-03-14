# Code is read much more than it is written, Therefore pep8 is meant to make code consistently more
# readable across code bases.

# Consistency with a style guide such as this is important, consistency in a project is more important
# consistency within a module/function is most important.


# Use 4 spaces when indenting:
if True:
    print("Hello World")


var_one = 1
var_two = 2
var_three = 3
var_four = 4

# An extra level of indentation should be added to distinguish params from the body of the function
# with hanging indentation
def long_function_name(
        one, two, three,
        four):
    return 42

# If values in brackets need to wrap you have two choices:

# Wrap them to next line starting at opening bracket
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Utilize hanging indent, if using hanging indent first line cannot be on same line as opening bracket.
# it must be put to the next line.
foo_2 = long_function_name(
    var_one, var_two,
    var_three, var_four)


# Arguments on first line are forbidden when using trailing indents
foo_3 = long_function_name(var_one, var_two,
    var_three, var_four)


# Additional layer of indents require to distinguish arguments from body.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)


this_is_one_thing = None
that_is_another_thing = None

def do_something():
    pass


# With if statements whose conditionals wrap to another line its fine to not add extra indent for body
if (this_is_one_thing and
    that_is_another_thing):
    do_something()



# Closing brace of a construct should line up under the first character of last line of the items
my_list = [
    1, 2, 3,
    4, 5, 6
    ]

# Or it can line up to first letter of the label
my_list_2 = [
    1, 2, 3,
    4, 5, 6
]