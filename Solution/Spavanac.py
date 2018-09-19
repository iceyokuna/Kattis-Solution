def main():
    h,m = [int(x) for x in input().split()]
    if(m < 45):
        h -= 1
        m += 60
        if(h < 0):
            h += 24
    print(h,m-45)


if __name__ == "__main__":
    main()
        
