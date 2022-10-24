def transform(legacy_data):
    out = {}
    for point, letters in legacy_data.items():
        for i in letters:
            out.update({i.lower(): point})
    return out
