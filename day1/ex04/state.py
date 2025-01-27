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


def main():
    if len(sys.argv) > 2:
        print("Too much args")
        exit(1)
    elif len(sys.argv) < 2:
        print("one arg missing")
        exit(1)
    cc = get_capital_cities()
    st = get_states()
    key = sys.argv[1]
    for k in cc:
        if cc[k] == key:
            for k2 in st:
                if st[k2] == k:
                    print(k2)
                    return (0)
    try:
        print(cc[st[key]])
    except KeyError:
        print("Unknown state")
        exit()


if __name__ == "__main__":
    main()
