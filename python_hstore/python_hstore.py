__author__ = "danishabdullah"

def guess_val_type(val):
    if not val:
        return None
    try:
        val = int(val)
        return val
    except ValueError as e:
        pass
    try:
        val = float(val)
        return val
    except ValueError as e:
        pass
    return None


def parse_numeric_value_hstore(string):
    tmp = a.replace('"',"").split(",")
    res = {}
    for i in tmp:
        key, value = map(str.strip, i.split("=>"))
        res[key] = guess_val_type(value)
    return res


def dict_to_hstore_text(dic):
    res = ''
    for key, value in dic.items():
        res += '"{}"=>"{}",'.format(key, value)
    if res:
        res = res[:-1]
    return res
