from functools import reduce


def multiply(show):
    def wrapper(*args):
        result = reduce(lambda x, y: x * y, args)
        # result = 1
        # for i in args:
        #     result *= i
        show(result)

    return wrapper


@multiply
def func(x):
    print(x)


numbers = map(int, input().split())
func(*numbers)
