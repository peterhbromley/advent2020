def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    answers = [[]]
    for line in lines:
        if line == '\n':
            answers.append([])
        else:
            answers[-1].append(line[:-1])

    return answers


def sum_of_counts(answers):
    return sum(map(lambda x: len(set(''.join(x))), answers))


def sum_of_alls(answers):
    answers_setified = [list(map(set, x)) for x in answers]
    return sum(map(lambda x: len(set.intersection(*x)), answers_setified))

def main():
    input_path = '../input/d6p1.txt'
    answers = read_input(input_path)
    sum_counts = sum_of_counts(answers)
    sum_alls = sum_of_alls(answers)

    print(f"PROBLEM 1: {sum_counts}")
    print(f"PROBLEM 2: {sum_alls}")


if __name__ == '__main__':
    main()