from typing import Callable
import time


def decor_count(func):

    count_call = 0

    def inner_count(*args, **kwargs):
        nonlocal count_call
        count_call += 1
        return count_call

    return inner_count


decorated_functions = []


def decor_reg(func):

    def inner_reg(*args, **kwargs):
        decorated_functions.append(func)
        return func(*args, **kwargs)

    return inner_reg


def decor_str(method):

    def inner_str(self, *args, **kwargs):

        file_name = f"{type(self).__name__}.txt"
        with open(file_name, "w") as f:
            f.write(method(self))

        return method(self)

    return inner_str


def timing(n: int, file: str):

    def time_decor(func):

        def time_inner(*args, **kwargs):

            start = time.time()
            start_time = time.strftime("Started at: %d-%b-%Y, %H:%M:%S", time.localtime(start))

            for i in range(1, n):
                func(*args, **kwargs)

            stop = time.time()
            period = stop - start
            stop_time = time.strftime("Finished at: %d-%b-%Y, %H:%M:%S", time.localtime(stop))

            with open(file, "a") as f:
                f.write(f"The function \"{func.__name__}\" has been executed {n} times during {period}s.\n")
                f.write(f"{start_time}\n")
                f.write(f"{stop_time}\n")

        return time_inner

    return time_decor
