def main():
    num_iteration = eval(input())
    num_point = 2 
    for i in range(num_iteration):
        num_point = (num_point * 2) -1
    print(num_point ** 2)    

if __name__ == "__main__":
    main()
