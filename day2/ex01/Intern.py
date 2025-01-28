class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

        def __init__(self):
            pass

    def __str__(self):
        return self.name

    def work(self):
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        return Intern.Coffee()


def main():
    no_name_intern = Intern()
    mark = Intern("Mark")
    print("testing Intern Mark")
    print(mark.__str__())
    print(mark.make_coffee())
    print("\n\nTesting No name intern : ")

    print(no_name_intern.__str__())
    try:
        no_name_intern.work()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
