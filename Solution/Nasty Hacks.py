def main():
    case = eval(input())
    for i in range(case):
        r,e,c = [int(x) for x in input().split()]
        if(r < e-c):
            print("advertise")
        elif(r > e-c):
            print("do not advertise")
        else:
            print("does not matter")


if(__name__ == "__main__"):
    main()
