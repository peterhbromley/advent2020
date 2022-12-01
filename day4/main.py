import re


def get_passports(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines.append('\n')

    passports = []
    p = []
    for line in lines:
        if line == '\n':

            p_dict = {}
            for kv_pair in p:
                k, v = kv_pair.split(':')
                p_dict[k] = v

            passports.append(p_dict)
            p = []
        else:
            p += line.split()

    return passports


def is_valid(passport):
    if len(passport) == 8:
        return True
    elif (len(passport) == 7) and ('cid' not in passport.keys()):
        return True
    return False


def value_error_handler(fn):
    def valid_fn(*args, **kwargs) :
        try:
            return fn(*args, **kwargs)
        except ValueError:
            return False
    return valid_fn


@value_error_handler
def valid_byr(passport):
    byr = passport['byr']
    return len(byr) == 4 and 1920 <= int(byr) <= 2002


@value_error_handler
def valid_iyr(passport):
    iyr = passport['iyr']
    return len(iyr) == 4 and 2010 <= int(iyr) <= 2020


@value_error_handler
def valid_eyr(passport):
    eyr = passport['eyr']
    return len(eyr) == 4 and 2020 <= int(eyr) <= 2030


@value_error_handler
def valid_hgt(passport):
    hgt = passport['hgt']
    if hgt[-2:] == 'cm':
        return 150 <= int(hgt[:-2]) <= 193
    elif hgt[-2:] == 'in':
        return 59 <= int(hgt[:-2]) <= 76
    else:
        return False


def valid_hcl(passport):
    return bool(re.search(r'^#[0-9a-f]{6}$', passport['hcl']))


def valid_ecl(passport):
    regex = r'^(amb|blu|brn|gry|grn|hzl|oth)$'
    return bool(re.search(regex, passport['ecl']))


def valid_pid(passport):
    return bool(re.search('^[0-9]{9}$', passport['pid']))


def is_valid_strict(passport):
    if not is_valid(passport):
        return False

    valid_fns = [valid_byr,
                 valid_iyr,
                 valid_eyr,
                 valid_hgt,
                 valid_hcl,
                 valid_ecl,
                 valid_pid]

    return all([f(passport) for f in valid_fns])


def num_valid(passports, is_valid_fn):
    return sum(map(is_valid_fn, passports))


def main():
    input_path = '../input/d4p1.txt'
    passports = get_passports(input_path)
    valid = num_valid(passports, is_valid)
    valid_strict = num_valid(passports, is_valid_strict)

    print(f'PROBLEM 1: {valid}')
    print(f'PROBLEM 2: {valid_strict}')


if __name__ == '__main__':
    main()
