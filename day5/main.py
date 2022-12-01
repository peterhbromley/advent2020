def read_input(filename):
    with open(filename) as f:
        return [line[:-1] for line in f]


def narrow_range(inst, low, hi):
    diff = (hi - low) // 2
    if inst in ['F', 'L']:
        return low, low + diff
    else:
        return hi - diff, hi


def get_row_or_col(insts, low, hi):
    for inst in insts:
        low, hi = narrow_range(inst, low, hi)

    return low


def get_seat_id(boarding_pass):
    rows = boarding_pass[:7]
    cols = boarding_pass[7:]
    row = get_row_or_col(rows, 0, 127)
    col = get_row_or_col(cols, 0, 7)
    return row * 8 + col


def get_highest_seat_id(passes):
    return max([get_seat_id(p) for p in passes])


def get_all_seat_ids(passes):
    return [get_seat_id(p) for p in passes]


def find_missing_seat(passes):
    ids = get_all_seat_ids(passes)
    ids.sort()
    for i in range(len(ids) - 1):
        if ids[i+1] == ids[i] + 2:
            return ids[i] + 1


def main():
    input_path = '../input/d5p1.txt'
    passes = read_input(input_path)
    highest = get_highest_seat_id(passes)
    missing = find_missing_seat(passes)

    print(f"PROBLEM 1: {highest}")
    print(f"PROBLEM 2: {missing}")


if __name__ == '__main__':
    main()


