def load_report(filename):
    with open(filename) as f:
        return [int(x) for x in f.readlines()]
        

def search(arr, i, j, target):
    if i == j:
        return False 

    check_idx = i + (j - i) // 2
    curr = arr[check_idx]
    if curr == target:
        return True 
    elif curr < target:
        return search(arr, check_idx + 1, j, target)
    else:
        return search(arr, i, check_idx, target)


def find_expenses(report, total):

    for i, expense in enumerate(report):
        target = total - expense

        if search(report, i, len(report), target):
            return target * expense

    return -1


def find_expenses_3(report, total):
    for i, expense in enumerate(report):
        leftover = total - expense

        found = find_expenses(report, leftover)
        if found != -1:
            return expense * found

    return -1


def main():
    magic_number = 2020
    input_path = '../input/d1p1.txt'

    report = load_report(input_path)
    report.sort()

    problem1 = find_expenses(report, magic_number)
    print(f'PROBLEM 1: {problem1}')
    
    problem2 = find_expenses_3(report, magic_number)
    print(f'PROBLEM 2: {problem2}')


if __name__ == '__main__':
    main()
