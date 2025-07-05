class MyClass:
    def __init__(self, x):
        # 👇 This attribute is public
        self.x = x

        # 👇 This method is public

    def get_x(self):
        return self.x


obj = MyClass(10)
print(obj.get_x())
print(obj.x)
