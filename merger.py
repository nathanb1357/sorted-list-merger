from argparse import ArgumentParser


def read_file(file_path: str) -> list:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"{file_path} not found")


def merge_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    len1, len2 = len(list1), len(list2)

    while i < len1 and j < len2:
        preference = input(
            f"Which entry do you prefer?\n"
            f"1.\t{list1[i]}\n"
            f"2.\t{list2[j]}\n"
            f"> "
        )
        while preference not in {'1', '2'}:
            preference = input("Invalid input. Please enter 1 or 2.\n> ")
        if preference == '1':
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list


def output_file():
    pass


def main():
    parser = ArgumentParser()
    parser.add_argument('a', help='The first file')
    parser.add_argument('b', help='The second file')
    args = parser.parse_args()

    list1 = read_file(args.a)
    list2 = read_file(args.b)
    merged_list = merge_lists(list1, list2)

    print(merged_list)


if __name__ == '__main__':
    main()
