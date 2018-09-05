def main():
    num_input = eval(input())
    temp_list = [negative_list for negative_list in input().split() if int(negative_list) < 0]
    print(len(temp_list))



if __name__ == "__main__":
    main()
