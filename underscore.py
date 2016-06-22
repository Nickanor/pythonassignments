# In the code above, you just created your own custom Python module/library that others can use!  How can others use the methods in your library?  By calling the properties stored in the class you defined (e.g. _.map(), _. reduce(), _.find(), etc).
#
# Your assignment is to implement the 5 methods above using delegating callbacks. You will have to modify the 5 methods to take in an array and a callback. Use what you learned in the previous chapter about callbacks to complete the assignment.
#
# One important concept that we want you to learn through this assignment is  how to pass data to and from callbacks. You pass data to a callback with a parameter and you pass data from the callback back to the parent function with a return. While you are going through this assignment pay close attention to this relationship.
#
# To understand what each method does, please refer to the underscore library.  Note that your method does not have to be as robust as underscore's; you just need to get the base functionality working. Therefore for most methods you will only have the list and a lambda as parameters, and for the lambda you will pass in each element and potentially a "memo" also known as a "collector".


class Underscore(object):
    def filter(self, a):
        b = []
        for i in a:
            if i % 2 == 0:
                b.append(i)
        print(b)


_ = Underscore()
_.filter([1, 2, 3, 4, 5])
