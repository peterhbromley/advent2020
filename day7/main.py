import re


def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    return [line[:-1] for line in lines]


def _parse(rule):
    top_bag_color = rule[:rule.find('bags contain') - 1]

    if bool(re.search(r'no other bags', rule)):
        return top_bag_color, []

    children = []
    contain_colors = re.findall(r'[0-9]+ [a-z ]+bag', rule)
    for hit in contain_colors:
        bags = hit[:-4]
        split_idx = re.match(r'[0-9]+', bags).end()
        children.append([bags[split_idx + 1:], int(bags[:split_idx])])

    return top_bag_color, children


def parse_rules(rules):
    graph = {}
    for rule in rules:
        key, val = _parse(rule)
        graph[key] = val
    return graph


def search(graph, key, target):
    if not graph[key]:
        return False
    elif key == target:
        return True
    else:
        children = [x[0] for x in graph[key]]
        return any(search(graph, k, target) for k in children)


def find_bag(graph, bag):
    # Don't count the shiny gold bag itself
    return sum(search(graph, k, bag) for k in graph.keys()) - 1


def main():
    input_path = '../input/mock.txt'
    rules = read_input(input_path)
    graph = parse_rules(rules)
    num_contain = find_bag(graph, 'shiny gold')

    print(f"PROBLEM 1: {num_contain}")


if __name__ == '__main__':
    main()
