from argparse import ArgumentParser, Namespace


def read_files(args: Namespace):
    pass


def merge_lists(list1, list2):
    pass


def output_file():
    pass


def main():
    parser = ArgumentParser()
    parser.add_argument('a', help='The first file')
    parser.add_argument('b', help='The second file')
    args = parser.parse_args()


if __name__ == '__main__':
    main()
