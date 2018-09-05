def main():
    contestants_list = []
    for i in range(5):
        input_list = [int(x) for x in input().split()]
        contestants_list.append(sum(input_list))
    max_score = max(contestants_list)
    print(contestants_list.index(max_score) + 1 , end = " ")
    print(max_score)


if __name__ == "__main__":
    main()
