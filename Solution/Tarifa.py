def main():
    limit_mb = eval(input())
    num_months = eval(input())
    mb_stack = 0
    for i in range(num_months):
        mb_spend = eval(input())
        mb_stack += limit_mb - mb_spend
    print(mb_stack + limit_mb)


if __name__ == "__main__":
    main()
