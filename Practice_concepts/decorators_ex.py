"""
-   We’ll use a decorator when we need to change the behavior of a function
    without modifying the function itself.
❏  You can also use one when you need to run the same code on multiple
    functions.
❏  A few good examples are when you want to add logging, authorization, test
    performance, perform caching, verify permissions, and so on.

"""

# Logging for cron jobs
from datetime import datetime
import time

def log_date_time_decorator(func):
    def wrapper_func():
        print("Function name: ", func.__name__)
        print("Run on: ", datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        func()
        print('---------')
    return wrapper_func()

@log_date_time_decorator
def day_time_job():
    time.sleep(5)
    print('day time job finished')

@log_date_time_decorator
def week_time_job():
    time.sleep(5)
    print('week time job finished')

@log_date_time_decorator
def month_time_job():
    time.sleep(5)
    print('month time job finished')

"""
Syntax:

def decorator_func(func):
    def wrapper_func():
        # do somethin bfr
        func()
        # do somethin after
    return wrapper_func

@decorator_func
def my_func():
    # do something

"""