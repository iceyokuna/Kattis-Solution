def main():
    n = eval(input())
    if(n == 1):
        print("Alice")
        return
    if(n%2 == 0):
        print("Bob")
        return
    print("Alice")

if __name__ == "__main__":
    main()
