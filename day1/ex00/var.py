def displayType(obj):
    print(obj, "est de type", type(obj))


def main():
    nb = 42
    displayType(nb)
    str = "42"
    displayType(str)
    str2 = "quarante-deux"
    displayType(str2)
    nb2 = 42.0
    displayType(nb2)
    boolean = True
    displayType(boolean)
    lst = [42]
    displayType(lst)
    dct = {42: 42}
    displayType(dct)
    tpl = (42,)
    displayType(tpl)
    displayType(set())


if __name__ == "__main__":
    main()
