class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # protected attribute
        self.__address = "Unknown"  # private attribute

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("Address:", self.__address)


person = Person("John", 30)
person.display_info()

