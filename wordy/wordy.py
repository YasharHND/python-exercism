valid_operations = {"+", "-", "*", "/"}


def to_int(number):
    try:
        return int(number)
    except ValueError:
        raise ValueError("syntax error")


def operate(so_far, number, operation):
    if operation == "":
        return number
    if operation == "+":
        return so_far + number
    if operation == "-":
        return so_far - number
    if operation == "*":
        return so_far * number
    if operation == "/":
        return so_far / number


def answer(question):
    if not question.startswith("What is"):
        raise ValueError("unknown operation")
    question = question[8:-1]
    question = question.replace("plus", "+")
    question = question.replace("minus", "-")
    question = question.replace("multiplied by", "*")
    question = question.replace("divided by", "/")
    if any(i.isalpha() for i in question):
        raise ValueError("unknown operation")
    departed = question.split(" ")
    if len(departed) % 2 == 0:
        raise ValueError("syntax error")
    operation = ""
    out = 0
    for i in range(len(departed)):
        if i % 2 == 0:
            out = operate(out, to_int(departed[i]), operation)
        else:
            operation = departed[i]
            if operation not in valid_operations:
                raise ValueError("syntax error")
    return out
