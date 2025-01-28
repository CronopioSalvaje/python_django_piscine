import random


from beverages import Coffee, Tea, Chocolate, Capuccino, HotBeverage


class CoffeeMachine:
    obsolescence = 0

    def __init__(self):
        pass

    def repair(self):
        self.obsolescence = 0

    def serve(self, Beverage):
        success = random.randint(0, 1)
        if self.obsolescence >= 10:
            raise
        CoffeeMachine.BrockenMachineException(
            "This coffee machine has to be repaired.")
        self.obsolescence += 1
        if success == 0:
            return CoffeeMachine.EmptyCup()
        return Beverage()

    class EmptyCup(HotBeverage):
        price = 0.90
        name = "empty cup"

        def description(self):
            return "An empty cup?! Gimme my money back!"

        def __init__(self):
            super().__init__()

    class BrockenMachineException(Exception):
        def __init__(self, *args):
            super().__init__(*args)


def main():
    machine = CoffeeMachine()

    for z in range(0, 3):
        try:
            for i in range(0, 3):
                print(machine.serve(Coffee).__str__())
                print(machine.serve(Tea).__str__())
                print(machine.serve(Chocolate).__str__())
                print(machine.serve(Capuccino).__str__())
        except CoffeeMachine.BrockenMachineException as e:
            print(e)
        machine.repair()


if __name__ == "__main__":
    main()
