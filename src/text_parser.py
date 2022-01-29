from typing import List

from os.path import exists
import re
import csv


def save_to_csv(words: List):
    with open('words.csv', 'w') as f:
        csv.writer(f).writerows(w for w in words)


def parse(file_path: str, pattern: str = r"\w+"):
    words = []
    with open(file_path, 'r') as f:
        
        while line := f.readline():
            new_words = re.findall(pattern, line)
            distinct_words = list(filter(lambda x: x not in words, new_words))
            words.extend(distinct_words)

    return words


def check_file(file_path: str):
    return exists(file_path)


def parse_test():
    file_path = '01.txt'
    
    if check_file(file_path):
        result = parse(file_path)
        save_to_csv(result)


if __name__ == '__main__':

    parse_test()
    print("The End.")
