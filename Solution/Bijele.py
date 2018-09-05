#1 1 2 2 2 8 = valid
def main():
    input_list = [int(x) for x in input().split()]
    valid_list = [1,1,2,2,2,8]
    ans_list = []
    for i in range(6):
        if(i == 5):
            print(valid_list[i] - input_list[i])
            return
        print(valid_list[i] - input_list[i], end = " ")

if __name__ == "__main__":
    main()
