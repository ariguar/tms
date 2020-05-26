def log(func):
    def wrapper(d, *args):
        print(func.__name__,  func(d, *args))

    return wrapper


@log
def a(x):
    return -x


@log
def b(x, y):
    return x * y


@log
def c(x, y, *args):
    result = x + y
    for arg in args:
        result += arg
    return result


a(999)
b(-5, 6)
c(28, 10, 2, 69, 11)

# def log(a):
#     def wrapper(num):
#         print(a(num))
#     return wrapper
#
# @log
# def a(x):
#     return -x
#
# a(2222)

# def log(b):
#     def wrapper(x, y):
#         print(b(x, y))
#     return wrapper
#
# @log
# def b(x, y):
#     return x * y
# #
# b(5, 2)


# def log(c):
#     def wrapper(x, y, result, *args):
#             print(c(x, y, result, *args))
#     return wrapper
#
# @log
# def c(x, y, *args):
#     result = x + y
#     for arg in args:
#         result += arg
#     return result
#
# c(1, 2, 4, 6, 7, 10)
