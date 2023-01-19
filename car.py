class Car:

    # TODO: After class definition there should be one empty line
    # TODO: Avoid "type" variable or arguments
    #  as this is Python's default naming for the system
    def __init__(self, name, type, color, power):
        self.name = name
        self.type = type
        self.color = color
        self.power = power


# TODO: Where do you actually use the Track and make a Track object?
#  I did not find it
class Track:

    # TODO: After class definition there should be one empty line
    def __int__(self, line):
        self.line = line

    # TODO: if you return something/get from the class,
    #  the method's name should start with "get_", like "get_line()"

    # TODO: You have not learned yet, but this method is static.
    #  It does not use "self" or class instance in itself,
    #  so it is not necessary to pas "self" as an argument
    @staticmethod
    def get_line():
        # TODO: Why you need __init__ and why you are not returning self.line here?
        return '_'



