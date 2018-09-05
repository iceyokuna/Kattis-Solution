def isPositive(num):
    if(num > 0):
        return True

def main():
    x = eval(input())
    y = eval(input())
    if(isPositive(x) and isPositive(y)):
        print(1)
    elif(not isPositive(x) and isPositive(y)):
        print(2)
    elif(not isPositive(x) and not isPositive(y)):
        print(3)
    else:
        print(4)




if __name__ == "__main__":
    main()
