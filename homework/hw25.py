
class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs.update({'extra_field': 'Вы добавили новый аттрибут'})

        def extra_method(self):
            print(f"Метод находиться в {name}")

        attrs.update({'extra_method': extra_method})

        return type.__new__(cls, name, bases, attrs)


class Test(metaclass=Meta):
    def __init__(self, value):
        self.value = value


obj1 = Test(1)
print(obj1.extra_field)
obj1.extra_method()
print(obj1.value)


class Test1(metaclass=Meta):
    def __init__(self, value):
        self.value1 = value


obj2 = Test1(2)
print(obj2.extra_field)
obj2.extra_method()
print(obj2.value1)