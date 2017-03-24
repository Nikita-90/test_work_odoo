sex_list = ['м', 'ж']


def input_num():
    while True:
        try:
            num = int(input('Enter num\n> '))
        except ValueError:
            print('Enter number!')
        else:
            return num


def input_name(num):
    data = []
    for n in range(num):
        name = input('Enter name\n> ')
        while True:
            try:
                age = int(input('Age\n> '))
            except ValueError:
                print('Enter Age!!!')
            else:
                break
        while True:
            sex = input('Sex: М/Ж\n> ').lower()
            if sex in sex_list:
                break
        data.append((name, age, sex))
    return data


def dec(output):
    def wrapp(data):
        if data[2] == 'м':
            print('Г-н ', end='')
        else:
            print('Г-жа ', end='')
        output(data)
    return wrapp


@dec
def f(data):
    print(data[0], data[2], data[1])


def main():
    num = input_num()
    date = input_name(num)
    for d in date.sort(key=lambda x: x[1]):
        f(d)


if __name__ == "__main__":
    main()
