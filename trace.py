import sys
from time import time

from dataclasses import dataclass


@dataclass
class Record:
    start_s: float
    func_name: str
    filename: str
    line_number: int


class FunctionInterceptor:
    def __init__(self):
        self.call_stack: list[Record] = []

    def trace_calls(self, frame, event, arg):
        filename = frame.f_code.co_filename
        if 'site-packages' in filename or (
            'scenarios/' not in filename and 'helpers/' not in filename and 'interfaces/' not in
            filename and 'contexts/' not in filename):
            return
        should_log = (
            'scenarios/' in filename
            or 'helpers/' in filename
            # or 'interfaces/' in filename
            or 'contexts/' in filename
        )
        if event == 'call' and should_log:
            func_name = frame.f_code.co_name
            filename = frame.f_code.co_filename
            line_number = frame.f_lineno

            # print(f" > CALL: {func_name} at {filename}:{line_number}")
            self.call_stack.append(Record(time(), func_name, filename, line_number))

        elif event == 'return' and should_log:
            func_name = frame.f_code.co_name
            filename = frame.f_code.co_filename
            if self.call_stack and self.call_stack[-1].func_name == func_name:
                verbose = f'-> {arg}' if False else ''
                a= "| "
                print(
                    f" > {int(time() * 1000 - self.call_stack[-1].start_s * 1000):>10} ms :: "
                    f"{a * len(self.call_stack)}{func_name} {verbose} ::: {filename}")
                self.call_stack.pop()

        return self.trace_calls


# Usage
interceptor = FunctionInterceptor()
sys.settrace(interceptor.trace_calls)

