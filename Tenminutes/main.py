import importlib
import os
import threading
import time


def run_func(modules: list):
    global call_func
    for module in modules:
        for func in dir(module):
            if func.startswith("action_") and (call_func := getattr(module, func)) and callable(call_func):
                thread = threading.Thread(target=call_func)
                thread.start()
                thread.join()


def compute():
    package_name = "package"
    time_start = time.time()
    run_func([importlib.import_module(package_name + "." + file[:-3])
            for file in os.listdir(importlib.import_module(package_name).__path__[0]) if file.startswith("module_")])
    print(time.time() - time_start)


if __name__ == '__main__':
    compute()
