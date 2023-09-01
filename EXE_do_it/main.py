


def sum(a, b):
    result  = a + b

    with open('result.txt', 'w', encoding='cp1251') as file:
        file.write(str(result))

def main():
    a  = int(input("Enter a: "))
    b  = int(input("Enter b: "))

    sum(a, b)



if __name__ == '__main__':
    main()