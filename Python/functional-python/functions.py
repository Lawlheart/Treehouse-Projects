def log_and_run(func):
    print("I just got {}".format(func.__name__))
    return func()


def log_and_return(func):
    print("I just got {}".format(func.__name__))
    return func


def say_hello():
    print("Hello!")

dicto = {
    'a': 1,
    'b': 2,
    'c': 3
}

print(dicto)
