import re


def parse_input(filename):
    with open(filename) as f:
        records = []
        for line in f.readlines():
            nums = list(map(int, re.findall(r'[0-9]+', line)))
            letter = re.findall(r'\ ([a-z])\:', line)
            password = re.findall(r'\ ([a-z]+)\n', line)

            records.append(nums + letter + password)

    return records


def valid_p1(record):
    lower, upper, letter, password = record
    if lower <= password.count(letter) <= upper:
        return True
    else:
        return False


def valid_p2(record):
    idx1, idx2, letter, password = record
    a = (password[idx1 - 1] == letter)
    b = (password[idx2 - 1] == letter)
    return a != b


def count_valid(records, valid_fn):
    return sum(map(valid_fn, records))


def main():
    input_path = '../input/d2p1.txt'
    records = parse_input(input_path)
 
    n_valid_p1 = count_valid(records, valid_p1)
    print(f"PROBLEM 1: {n_valid_p1}")

    n_valid_p2 = count_valid(records, valid_p2)
    print(f"PROBLEM 2: {n_valid_p2}")


if __name__ == '__main__':
    main()
