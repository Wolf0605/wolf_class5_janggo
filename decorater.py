def decorator(func):
    def decorated(length, width):
        func(length, width)
        if True:
            volume = (float(length) * float(width)) / 2
            return volume
    return decorated

# decorate 는 우선순위를 늦춤
@decorator
def triangle(length, width):
    if float(length) > 0 and float(width) > 0:
        return True
    else:
        return False

a = triangle(1,2)
b = triangle(2, 4)
print(a)
print(b)

class User:
    def decorator(func):
        def decorated(length, width):
            func(length, width)
            if True:
                volume = (float(length) * float(width)) / 2
                return volume

        return decorated
    @decorator
    def triangle(length, width):
        if float(length) > 0 and float(width) > 0:
            return True
        else:
            return False


