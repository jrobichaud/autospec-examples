class MyClass:
    def __init__(self, name):
        self.name = name

    def some_method(self, param1):
        print("param: {param} and {name}".format(param=param1, name=self.name))

    @staticmethod
    def some_static_method():  # pragma: no coverage
        pass
