from datetime import datetime

def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        execution_time = end_time - start_time
        print(f"Час виконання функції {func.__name__}: {execution_time}")
        return result
    return wrapper

@calculate_execution_time
def func1():
    for _ in range(1000000):
        pass

@calculate_execution_time
def func2():
    for _ in range(500000):
        pass

func1()
func2()
