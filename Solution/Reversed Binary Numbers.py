def main():
    decimal = eval(input())
    binary = bin(decimal)
    binary = str(binary)
    reverse = "0b" + binary[-1:1:-1]
    print(int(reverse,2))


if(__name__ == "__main__"):
    main()
