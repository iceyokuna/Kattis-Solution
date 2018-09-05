def main():
    num_line = eval(input())
    answer = 0
    for i in range(num_line):
        num_input = input()
        answer += int(num_input[:-1]) ** int(num_input[-1])
    print(answer)

if __name__ == "__main__":
    main()
