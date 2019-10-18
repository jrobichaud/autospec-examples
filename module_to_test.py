from my_module import MyClass
import my_module


def signature_problem():
    instance = my_module.MyClass("Foo")
    instance.some_method("Bar", "Buzz")
    return instance.name


def my_method_to_test():
    instance = my_module.MyClass("Foo")
    instance.some_method("Bar")
    return instance.name


def incorrect_import():
    instance = MyClass("Foo")
    instance.some_method("Bar")
    return instance.name
