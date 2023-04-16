from abc import ABC, abstractmethod

# creating an abstract class
class AbstractClass(ABC)
    @abstractmethod # abstract method
    def abstract_method(self):
        pass

    # regular method
    def regular_method(self):
        print("This is a regular method in the abstract class.")


class ChildClass(AbstractClass):
    def abstract_method(self):
        print("This is the implementation of the abstract method")

# creating and object
obj = ChildClass()
obj.abstract_method()
obj.regular_method
