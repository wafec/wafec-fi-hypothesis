import sys


class Test:
    def __init__(self):
        self.a = 10


def my_tracer(frame, event, arg=None):
    # extracts frame code
    code = frame.f_code

    # extracts calling function name
    func_name = code.co_name

    # extracts the line number
    line_no = frame.f_lineno

    print("A {} encountered in {}() at line number {}".format(event, func_name, line_no))

    return my_tracer


sys.settrace(my_tracer)
x = Test()
