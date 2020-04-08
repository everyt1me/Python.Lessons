if __name__ == "__main__":
    add,
    subtract,
    multiply,
    divide


def add(*params):
    result = 0
    for i in params:
        result += i
    return result


def subtract(*params):
    result = params[0]
    for i in params[1:]:
        result -= i
    return result


def multiply(*params):
    result = 1
    for i in params:
        result *= i
    return result


def divide(*params):
    result = params[0]
    for i in params[1:]:
        result /= i
    return result
