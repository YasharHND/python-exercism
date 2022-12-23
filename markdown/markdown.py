import re


def replace_styles(line):
    while True:
        match = re.search("__(.+)__", line)
        if not match:
            break
        line = line.replace(match.group(0), f"<strong>{match.group(1)}</strong>")
    while True:
        match = re.search("_(.+)_", line)
        if not match:
            break
        line = line.replace(match.group(0), f"<em>{match.group(1)}</em>")
    return line


def parse_line(line, last_line_bullet):
    header_match = re.search("^(#{1,6}) (.+)$", line)
    if header_match:
        tag = f"h{header_match.group(1).count('#')}"
        return f"<{tag}>{replace_styles(header_match.group(2))}</{tag}>", False
    bullet_match = re.search("^\\* (.+)$", line)
    if bullet_match:
        return f"{'' if last_line_bullet else '<ul>'}<li>{replace_styles(bullet_match.group(1))}</li>", True
    return f"<p>{replace_styles(line)}</p>", False


def parse(markdown):
    out = []
    last_line_bullet = False
    for line in markdown.split('\n'):
        line, this_line_bullet = parse_line(line, last_line_bullet)
        if last_line_bullet and not this_line_bullet:
            out[-1] += "</ul>"
        last_line_bullet = this_line_bullet
        out.append(line)
    else:
        if last_line_bullet:
            out[-1] += "</ul>"
    return "".join(out)
