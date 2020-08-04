import functools
from pprint import pprint

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        print()
        for a in args:
            print(a)
            pprint(vars(a))
            print()

        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        print('---------------------------------------------------------------------')
        return value
    return wrapper_debug