class Readonly(object):
    def __init__(self, change):
        self.change = change

    def __get__(self, instance, owner):
        return self.change(instance)

    def __set__(self, instance, value):
        return self.change(value)


class Test(object):
    def __init__(self):
        self.__val = 1

    @Readonly
    def val(self):
        return self.__val


test = Test()
print(test.val)  # OK, выводит 1
test.val = 2  # AttributeError




