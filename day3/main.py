TREE = '#'


def read_input(filename):
    with open(filename) as f:
        return [list(line[:-1]) for line in f.readlines()]


def traverse_trees(tree_map, right, down):
    row = 0
    col = 0
    width = len(tree_map[0])
    height = len(tree_map)

    tree_count = 0
    while row < height - down:
        row += down
        col = (col + right) % width

        if tree_map[row][col] == TREE:
            tree_count += 1

    return tree_count


def traverse_all_slopes(tree_map, slopes):
    product = 1
    for right, down in slopes:
        product *= traverse_trees(tree_map, right, down)

    return product


def main():
    input_path = '../input/d3p1.txt'
    tree_map = read_input(input_path)
    count = traverse_trees(tree_map, 3, 1)

    print(f"PROBLEM 1: {count}")

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = traverse_all_slopes(tree_map, slopes)

    print(f"PROBLEM 2: {product}")

if __name__ == '__main__':
    main()
