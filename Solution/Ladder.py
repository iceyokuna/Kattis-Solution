import math

def main():
    h,v = [int(x) for x in input().split()]
    print(math.ceil(h/math.sin(math.radians(v))))

if(__name__ == "__main__"):
    main()
