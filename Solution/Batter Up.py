def main():
    num_case = input()
    input_list = [int(x) for x in input().split() if int(x) >= 0]
    print(sum(input_list) / len(input_list))

if __name__ == "__main__":
    main()
