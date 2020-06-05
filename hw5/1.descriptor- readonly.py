class Readonly(object):
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError
        self.fset(obj, value)


class Test(object):
    def __init__(self):
        self.__val = 1

    @Readonly
    def val(self):
        return self.__val


test = Test()
print(test.val)  # OK, выводит 1
test.val = 2  # AttributeError

# class Readonly(object):
#     def __init__(self, change):
#         self.change = change
#
#     def __get__(self, instance, owner):
#         return self.change(instance)
#
#     def __set__(self, instance, value):
#         return self.change(value)
