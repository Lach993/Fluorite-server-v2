def get(data, keys, default=0):
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data


def ratio(a, b):
    return 0 if b == 0 else round(a / b, 2)

def xp_to_level(xp):
    return round((((2 * xp) + 30625)**0.5 / 50) - 2.5)
