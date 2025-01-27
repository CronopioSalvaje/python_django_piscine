def main():
    with open("numbers.txt") as file:
        line = file.readline()
        while (len(line) != 0):
            nb = line[:line.find(",")]
            print(nb)
            line = line[line.find(",") + 1:]
            if line.find(",") == -1:
                print(line)
                break


if __name__ == "__main__":
    main()
