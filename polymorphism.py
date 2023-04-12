class Parent:
    def method(self, attribute1, attribute2):
        pass


class Child1(Parent):
    def method(self, attribute1, attribute2):
        # using attribute1
        print("Child1 method using attribute1:", attribute1)


class Child2(Parent):
    def method(self, attribute1, attribute2):
        # using attribute2
        print("Child2 method using attribute2:", attribute2)


# create instances of both child classes
child1 = Child1()
child2 = Child2()

# call the method on both child instances with different attributes
child1.method("attribute1_value", "unused_attribute2_value")
child2.method("unused_attribute1_value", "attribute2_value")
