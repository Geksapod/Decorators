"""This module provide access to f-decorators"""

from typing import Callable, Any
import time

func_call_num = {}
func_call = 0


def decor_count(func: Callable[[Any], Any]) -> Any:
    """
    Return number of calls of func.

    :param func: Callable object this function apply to.
    """

    def inner_count(*args, **kwargs):

        func_name = func.__name__
        global func_call

        if func_name not in func_call_num:
            func_call = 1
            func_call_num[func_name] = func_call
        else:
            func_call += 1
            func_call_num[func_name] = func_call

        return func(*args, **kwargs)

    return inner_count


decorated_functions = []


def decor_reg(func: Callable[[Any], Any]) -> Any:
    """
    Add reference of func to decorated_functions list.

    :param func: Callable object this function apply to.
    """

    def inner_reg(*args, **kwargs):
        decorated_functions.append(func)
        return func(*args, **kwargs)

    return inner_reg


def decor_str(method: Callable[[object], str]) -> str:
    """
    Call a method and write a result into txt file named the same as the Callable argument (object).

    :param method: Callable object this function apply to.
    """

    def inner_str(self: object, *args, **kwargs):

        res = method(self)
        file_name = f"{type(self).__name__}.txt"
        with open(file_name, "a") as f:
            f.write(res)

        return res

    return inner_str


def timing(n: int, file: str) -> str:
    """
    Write timing of definite quantity of execution of callable into txt file.

    :param n: Quantity of executions.
    :param file: Name of the txt file.
    """

    def time_decor(func: Callable[[Any], Any]) -> Any:

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
