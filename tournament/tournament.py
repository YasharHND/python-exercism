def tally(rows):
    out = {}
    for row in rows:
        split = row.split(";")
        team_a = split[0]
        team_b = split[1]
        match_result = split[2]
        team_a_values = get_or_default(team_a, out)
        team_b_values = get_or_default(team_b, out)
        update_value(team_a_values, "MP", 1)
        update_value(team_b_values, "MP", 1)
        if match_result == "win":
            update_value(team_a_values, "W", 1)
            update_value(team_a_values, "P", 3)
            update_value(team_b_values, "L", 1)
        elif match_result == "loss":
            update_value(team_a_values, "L", 1)
            update_value(team_b_values, "W", 1)
            update_value(team_b_values, "P", 3)
        else:
            update_value(team_a_values, "D", 1)
            update_value(team_a_values, "P", 1)
            update_value(team_b_values, "D", 1)
            update_value(team_b_values, "P", 1)
        out[team_a] = team_a_values
        out[team_b] = team_b_values
    out = {k: v for k, v in sorted(sorted(out.items(), key=lambda item: item[0]), key=lambda item: item[1]["P"], reverse=True)}
    out_list = ["Team                           | MP |  W |  D |  L |  P"]
    for k, v in out.items():
        line = k + (" " * (31 - len(k))) + "".join([print_cell(values) for values in v.values()]).rstrip()
        out_list.append(line)
    return out_list


def get_or_default(team, team_results):
    if team in team_results:
        return team_results.get(team)
    else:
        return {
            "MP": 0,
            "W": 0,
            "D": 0,
            "L": 0,
            "P": 0
        }


def update_value(values, key, increment):
    values.update({key: values.get(key) + increment})


def print_cell(value):
    string = str(value)
    return "|" + (" " * (3 - len(string))) + string + " "
