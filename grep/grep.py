def add_to_matches(collection, file_name, line):
    if file_name in collection:
        lines = collection.get(file_name)
        lines.append(line)
    else:
        lines = [line]
    collection.update({file_name: lines})


def grep(pattern, flags, files):
    if "-i" in flags:
        pattern = pattern.lower()
    full_line_match = "-x" in flags
    need_line_number = "-n" in flags
    inverter = "-v" in flags
    matches = {}
    for file_name in files:
        with open(file_name, "r") as file:
            for i, line in enumerate(file.readlines()):
                line_to_check = line.lower().strip() if "-i" in flags else line.strip()
                line_does_match = pattern == line_to_check if full_line_match else pattern in line_to_check
                if line_does_match ^ inverter:
                    add_to_matches(matches, file_name, f"{i + 1}:{line}" if need_line_number else line)
    if "-l" in flags:
        result = "\n".join(matches.keys())
        if result:
            result += "\n"
        return result
    need_file_name = len(files) > 1
    out = []
    for key, value in matches.items():
        for line in value:
            out.append(f"{key}:{line}" if need_file_name else line)
    return "".join(out)
