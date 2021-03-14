def round02(func):
    def wrapper(*args, **kwargs):
        return round(func(*args, **kwargs)*5)/5
    return wrapper

def round0(func):
    def wrapper(*args, **kwargs):
        return round(func(*args, **kwargs))
    return wrapper