class MyClass:
    def __init__(self, name):
        self.name = name

    def some_method(self, param1):
        print(f"param: {param1} and {self.name}")

    @staticmethod
    def some_static_method():  # pragma: no coverage
        pass
