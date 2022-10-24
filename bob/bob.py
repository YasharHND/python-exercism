def response(hey_bob):
    is_question = hey_bob.strip().endswith('?')
    is_shout = hey_bob.isupper()
    is_empty = len(hey_bob.strip()) == 0
    if is_question and is_shout:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return "Sure."
    if is_shout:
        return "Whoa, chill out!"
    if is_empty:
        return "Fine. Be that way!"
    return "Whatever."
