import sys


def get_states():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    return states


def get_capital_cities():
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    return capital_cities


def formatLowerCities(lst):
    newlst = {}
    for k in lst:
        newlst[k] = lst[k].lower()
    return newlst


def formatLowerStates(lst):
    newlst = {}
    for k in lst:
        newlst[k.lower()] = lst[k]
    return newlst


def get_city_from_state(key):

    cc = formatLowerCities(get_capital_cities())
    st = formatLowerStates(get_states())
    try:
        val = cc[st[key.lower()]]
    except KeyError:
        return ("Unknown")
    return val.capitalize()


def get_state_from_city(key):
    cc = get_capital_cities()
    st = get_states()
    for k in cc:
        if cc[k].lower() == key.lower():
            for k2 in st:
                if st[k2] == k:
                    return k2
    return "Unknown"


def args_check():
    if len(sys.argv) > 2:
        print("Too much args")
        exit(1)
    elif len(sys.argv) < 2:
        print("one arg missing")
        exit(1)


def hasupper(val):
    for char in range(len(val)):
        if char != 0 and val[char].isupper():
            return True
    return False


def cleanup(val):
    val = val.strip()
    if len(val) == 0:
        return val
    if hasupper(val):
        val = val.capitalize()
    return val


def parse_args():
    data = []
    arg = sys.argv[1]
    while (len(arg) != 0):
        val = arg[:arg.find(",")]
        val = cleanup(val)
        if len(val) > 0:
            data.append(val)
        arg = arg[arg.find(",") + 1:]
        if arg.find(",") == -1:
            arg = cleanup(arg)
            data.append(arg)
            break
    return data


def capitalise_all(string):
    new_str = ""
    while (len(string) > 0):
        new_str += string[:string.find(" ")].capitalize() + " "
        string = string[string.find(" ") + 1:].strip()
        if string.find(" ") == -1:
            new_str += string.capitalize()
            break
    return new_str


def main():
    args_check()
    keys = parse_args()

    for key in keys:
        test = get_state_from_city(key)
        test2 = get_city_from_state(key)
        if test != "Unknown":
            print(key, "1is the capital of", test)
        elif test2 != "Unknown":
            print(test2, "2is the capital of", capitalise_all(key))
        else:
            print(key, "is neither a capital city nor a state")


if __name__ == "__main__":
    main()
