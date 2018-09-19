def main():
    card = input()
    t = card.count('T')
    c = card.count('C')
    g = card.count('G')
    bonus = 0
    
    if(t > 0 and c > 0 and g > 0):
        temp = min(t,c)
        bonus = min(temp,g)

    print(pow(t,2) + pow(c,2) + pow(g,2) + (7 * bonus))


if(__name__ == "__main__"):
    main()
    
