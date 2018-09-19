def main():
    case = eval(input())
    for i in range(case):
        num = eval(input())
        if(num % 2 == 0):
            print(num, "is even")
        else:
            print(num, "is odd")


if(__name__ == "__main__"):
    main()
