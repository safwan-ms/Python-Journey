class MyClass:
    def __init__(self, x):
        # This attribute is private
        self.__x = x

    def get_x(self):
        return self.__x


obj = MyClass(10)
print(obj.get_x())

print(obj._MyClass__x)
