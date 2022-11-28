def get_list_of_wagons(*args):
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    train = each_wagons_id[2:] + each_wagons_id[:2]
    return train[0:1] + missing_wagons + train[1:]


def add_missing_stops(route, **stops):
    route.update({"stops": list(stops.values())})
    return route


def extend_route_information(route, more_route_information):
    return route | more_route_information


def fix_wagon_depot(wagons_rows):
    out = []
    length = len(wagons_rows)
    for i in range(length):
        out.append([wagons_rows[j][i] for j in range(length)])
    return out
