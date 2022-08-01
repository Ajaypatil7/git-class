# 136 What is pylint.
#            Pylint is a plugin or extension that checks for syntax errors.
#            Also, it tries to enforce coding standards according to PEP8 style guide.
#            It can give recommendations/suggestions/hints about types.

# 137 What is the output of the below program.
#[1, 2, 3, 4] * 2
# op:-  [1,2,3,4,1,2,3,4]

# 138 What is the difference between the is and == operators
#            "==" operator checks if both objects have same value.
#            "is" operator checks if identity or memory address of two objects are same.

# 139 What is "self" in class.
#            "self" is called as Instance or data.
#            Every instance method of a class has "self" as first argument.
#            During runtime, "self" will be replaced with object instance of the class.
#            e.g.
#            class Point:
#               def __init__(self, a, b):
#                   self.a = a
#                   self.b = b
#
#            p1 = Point(1, 2)
#            p2 = Point(3, 4)
#
# when you say, p1.a, "self" will be replaced with p1 and when you say p2.a, "self" will be replaced with p2.
# Internally p1 and p2 will be pointing to a dictionary which is also called instance dictionary.
# the instance dicitonary canbe accessed via __dict__ attribute.
# e.g. p1.__dict__ , p2.__dict__

# 140 What is assert statement. What is the difference between assert and if/else statement.
#            1. An assert statement is used to valdate the actual result against expected result.
#            2. If the actual result does not match with the expected result, AssertionError is raised.
#            3. if/else is not used for validating the actual result against expected result.
#            4. if/else statement will not raise any exception.
