def strong(func):
    def wrapper():
        print('1')
        return '<strong>' + func() + '</strong>'

    return wrapper


def emphasis(func):
    def wrapper():
        print('2')
        return '<em>' + func() + '</em>'

    return wrapper


# top to bottom flow
@strong
@emphasis
def say_hello1():
    return 'Hi Arun!'


print(say_hello1())


def dec_func(func):
    def wrapper(*args, **kwargs):
        s = func()
        return s.upper()

    return wrapper


# say_hello = dec_func(say_hello) -> decorator format

@dec_func
def say_hello():
    return 'Hi Arun!'


print(say_hello())


from functools import wraps


def make_number_double_dec(func):
    @wraps(func)
    def wrapper(n, m):
        # for x in args:
        # 	x *= 2
        # for k, v in kwargs.items():
        # 	v *= 2
        # print(x, kwargs)
        n *= 2
        m *= 2
        return func(n, m)

    return wrapper


@make_number_double_dec
def num_counter(n, m=10):
    """add given number with updated value"""
    return n + m


if __name__ == '__main__':
    print(num_counter)
    print(num_counter(10, m=20))
    print(num_counter.__name__)
    print(num_counter.__doc__)
    print(num_counter.__module__)
