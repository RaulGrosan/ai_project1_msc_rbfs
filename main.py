from missionaries_and_cannibals import MissionariesAndCannibals
from search import recursive_best_first_search


def main():
    problem = MissionariesAndCannibals()
    result = recursive_best_first_search(problem)
    print_path(result.path())


def print_path(path):
    for node in path:
        print(node.state.value)


if __name__ == '__main__':
    main()