import math

def main():
    n,w,l = [int(x) for x in input().split()]
    diagonal = math.sqrt(pow(l,2) + pow(w,2))
    for i in range(n):
        match = eval(input())
        if(match <= diagonal):
            print("DA")
        else:
            print("NE")

if __name__ == "__main__":
    main()
