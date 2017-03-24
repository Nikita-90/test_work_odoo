sex_list = ['м', 'ж']
data_list = []  # This list is used for def open_file()


def input_num():
    while True:
        try:
            num = int(input('Enter the number of strings\n> '))
        except ValueError:
            print('Enter number!')
        else:
            return num


def select_input():
    while True:
        input_ = input('Select input:\n'
                       '1 -- keyboard\n'
                       '2 -- open file\n')
        if input_ == '1':
            return keyboard_input
        elif input_ == '2':
            return open_file


def keyboard_input():
    return input('Enter form:\nname sex(м/ж) age\n> ')


def open_file():
    while not data_list:
        file_address = input('File address\n> ')
        try:
            with open(file_address, 'rt') as file:
                for string in file:
                    data_list.append(string)
                break
        except (FileNotFoundError, IsADirectoryError):
            print('%s -- file not found.' % file_address)
    return data_list.pop(0)


def counter(num):
    findings = []
    select = select_input()
    for n in range(num):
        while True:
            input_ = select()
            data = validation(input_)
            if data is not None:
                findings.append(data)
                break
    return findings


def validation(input_):
    try:
        *name, sex, age = input_.split()
    except (SyntaxError, ValueError):
        print('%s   Incorrect input.' % input_)
    else:
        name = validation_name(name, input_)
        age = validation_age(age, input_)
        sex = validation_sex(sex, input_).lower()
        return name, sex, age
    return None


def validation_age(age, input_):
    while True:
        try:
            age = int(age)
        except ValueError:
            print('%s -- Incorrect age in %s' % (age, input_))
        else:
            return age
        age = input('Age:\n> ')


def validation_sex(sex, input_):
    while True:
        if sex.lower() in sex_list:
            return sex
        print('%s -- incorrect sex in %s' % (sex, input_))
        sex = input('Sex:\n> ')


def validation_name(name, input_):
    while not name:
        print('%s -- incorrect name in %s' % (''.join(name), input_))
        name = input('Name:\n>').split()
    return name


def dec(output):
    def wrapp(data):
        if data[1] == 'м':
            print('Г-н ', end='')
        else:
            print('Г-жа ', end='')
        output(data[0])
    return wrapp


@dec
def f(name):
    print(' '.join(name))


def main():
    num = input_num()
    data = counter(num)
    data.sort(key=lambda x: x[2])
    for d in data:
        f(d)


if __name__ == "__main__":
    main()
