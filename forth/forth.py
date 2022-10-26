import re


class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message


arithmetic = {
    "+",
    "-",
    "*",
    "/"
}

manipulation = {
    "DUP",
    "DROP",
    "SWAP",
    "OVER"
}


def new_operation(definition):
    result = re.search(": ([^ ]+) ([^;]+) ;", definition)
    return [result.group(1), result.group(2)]


def apply(ops, operation):
    operation[1] = ops[operation[1]]


def apply_all(ops, data):
    for key, value in ops.items():
        data = data.replace(key, value)
    return data


def evaluate(input_data):
    if len(input_data) > 1:
        new_operations = {}
        for i in input_data[:-1]:
            operation = new_operation(i.upper())
            new_operations[operation[0]] = apply_all(new_operations, operation[1])
        data = input_data[-1].upper()
        data = apply_all(new_operations, data)
    else:
        if re.match(": ([^ ]+) ([^;]+) ;", input_data[0]):
            raise ValueError("illegal operation")
        data = input_data[0].upper()
    stack = []
    for statement in data.split(" "):
        if statement in arithmetic:
            if len(stack) != 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            if statement == "/":
                if stack[1] == 0:
                    raise ZeroDivisionError("divide by zero")
                statement = "//"
            stack = [eval(str(stack[0]) + statement + str(stack[1]))]
        elif statement in manipulation:
            if statement == "DUP":
                if len(stack) < 1:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack[-1])
            elif statement == "DROP":
                if len(stack) < 1:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack.pop()
            elif statement == "SWAP":
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                temp = stack[-1]
                stack[-1] = stack[-2]
                stack[-2] = temp
            else:
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack[-2])
        else:
            try:
                stack.append(int(statement))
            except ValueError:
                raise ValueError("undefined operation")
    return stack
