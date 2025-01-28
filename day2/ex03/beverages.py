class HotBeverage:
    price = 0.30
    name = "hot beverage"

    def __init__(self):
        pass

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        res = f"{self.name.capitalize()} :\n"
        res += f"\tname : {self.name}\n"
        res += f"\tprice : {self.price:.2f}\n"
        res += f"\tdescription : {self.description()}\n"
        return res


class Tea(HotBeverage):

    name = "tea"

    def __init__(self):
        super().__init__()


class Chocolate(HotBeverage):

    name = "chocolate"
    price = 0.50

    def __init__(self):
        super().__init__()

    def description(self):
        return "Chocolate, sweet chocolate..."


class Capuccino(HotBeverage):

    name = "capuccino"
    price = 0.45

    def __init__(self):
        super().__init__()

    def description(self):
        return "Un po’ di Italia nella sua tazza!"


class Coffee(HotBeverage):

    name = "coffee"
    price = 0.40

    def __init__(self):
        super().__init__()

    def description(self):
        return "A coffee, to stay awake."
