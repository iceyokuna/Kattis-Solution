def main():
    l = eval(input())
    d = eval(input())
    x = eval(input())
    n = 10000
    m = 0
    
    for i in range(l,d + 1):
        string = str(i)
        result = 0
        for c in string:
            result += int(c)
        if(result == x):
            if(i < n):
                n = i
            if(i > m):
                m = i
    print(n)
    print(m)
    

if __name__ == "__main__":
    main()
