def select_input():
    while True:
        input_ = input('Select input:\n'
                       '1 -- keyboard\n'
                       '2 -- open file\n')
        if input_ == '1':
            return keyboard_input_string
        elif input_ == '2':
            return read_from_file


def read_from_file(quantity, var):
    string_mas = []
    while True:
        file_address = input('Enter file address for %s:\n> ' % var)
        try:
            with open(file_address, 'rt') as file:
                for f in file.readlines():
                    string_mas.append(f.rstrip())
        except (FileNotFoundError, IsADirectoryError):
            print('Incorrect address.')
        else:
            return string_mas[:quantity]


def get_quantity(var):
    while True:
        try:
            quan = int(input('Enter quantity string for %s:\n> ' % var))
        except ValueError:
            print('Enter number')
        else:
            return quan


def keyboard_input_string(quantity, var):
    string_mas = []
    for quan in range(quantity):
        string_mas.append(input('%s%s:\n> ' % (var, quan+1)))
    return string_mas


def check(string_mas, request_mas):
    counter = [[req, 0] for req in request_mas]
    for i in range(len(request_mas)):
        for string in string_mas:
            if request_mas[i] == string:
                counter[i][1] += 1
    return counter


def main():
    input_ = select_input()
    quantity_string = get_quantity('X')
    string_mas = input_(quantity_string, 'X')
    quantity_request = get_quantity('Y')
    request_mas = input_(quantity_request, 'Y')
    counter = check(string_mas, request_mas)
    for k in counter:
        print(k[1])


if __name__ == '__main__':
    main()
