def main():
    total_art, impact = [int(x) for x in input().split()]
    if(total_art == 0):
        print(impact)
        return
    print((total_art * (impact - 1)) + 1)


if __name__ == "__main__":
    main()
