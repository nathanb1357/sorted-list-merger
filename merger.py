import sys
import os
from pathlib import Path
from argparse import ArgumentParser


def read_file(file_path: str) -> list:
    try:
        if not file_path.endswith('.txt'):
            raise ValueError(f'ERROR: {file_path} is not a text file!')
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"ERROR: {file_path} not found!")
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)


def merge_lists(list1: list, list2: list) -> list:
    merged_list = []
    i, j = 0, 0
    len1, len2 = len(list1), len(list2)

    while i < len1 and j < len2:
        preference = input(
            f"Which entry do you prefer?\n"
            f"1.\t{list1[i]}\n"
            f"2.\t{list2[j]}\n> "
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


def get_output_file(file_name: str) -> str:
    directory = str(Path.home() / "Downloads")
    file_path = os.path.join(directory, file_name)
    if not os.path.exists(file_path):
        return file_path

    counter = 1
    base, extension = os.path.splitext(file_name)
    while True:
        file_name = f"{base} ({counter}){extension}"
        file_path = os.path.join(directory, file_name)
        if not os.path.exists(file_path):
            return file_path
        counter += 1


def output_file(output: list, file_name: str):
    file_path = get_output_file(file_name)
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in output:
                file.write(item + '\n')
        print(f"File has been saved to {file_path}")
    except Exception as e:
        print(f"ERROR: An error occurred while writing to {file_path}: {e}")
        sys.exit(1)


def main():
    parser = ArgumentParser()
    parser.add_argument('a', help='The first file')
    parser.add_argument('b', help='The second file')
    args = parser.parse_args()

    list1 = read_file(args.a)
    list2 = read_file(args.b)
    merged_list = merge_lists(list1, list2)

    output_file(merged_list, "sorted_list.txt")


if __name__ == '__main__':
    main()
