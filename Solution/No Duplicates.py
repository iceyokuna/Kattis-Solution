def main():
    sentence = input()
    lt = sentence.split()
    for word in lt:
        if(lt.count(word) >= 2):
            print("no")
            return
    print("yes")


if(__name__ == "__main__"):
    main()
