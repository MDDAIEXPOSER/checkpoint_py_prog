def get_numbers():
    list_numbers = []
    while True:
        n = int(input())
        if n != 0:
            list_numbers.append(n)
        else:
            break
    prepared_list = sorted(list_numbers)
    print(prepared_list)
    for element in prepared_list:
        print(element)





def main():
    get_numbers()

if __name__ == "__main__":
    main()
