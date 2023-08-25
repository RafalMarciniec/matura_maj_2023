from collections import defaultdict

import numpy as numpy

path_to_file = r"data\pi.txt"

# path_to_file = r"data\pi_przyklad.txt"


def sanitize_input(is_digits=False):
    with open(path_to_file, "r") as f:
        if is_digits:
            return [int(item.replace("\n", "")) for item in f.readlines()]
        raw_input = [str(item.replace("\n", "")) for item in f.readlines()]
        pairs = []
        for idx in range(len(raw_input) - 1):
            pairs.append(int(raw_input[idx] + raw_input[idx + 1]))
        return pairs


def zad_3_1():
    pairs = sanitize_input()
    print(len(list((filter(lambda x: x > 90, pairs)))))


def zad_3_2():
    # here is a problem when 00 not exist but problem is only for not existing keys in example
    pairs = sanitize_input()
    ocurrences = defaultdict(int)
    for unique_number in set(pairs):
        ocurrences[unique_number] += pairs.count(unique_number)
    print(f"MAX key {max(ocurrences, key=ocurrences.get)}, value {max(ocurrences.values())}")
    print(f"MIN key {min(ocurrences, key=ocurrences.get)}, value {min(ocurrences.values())}")
    a = 1


def is_increasing(current_index, is_first_run, digits):
    if current_index == len(digits) - 1:
        return current_index + 1
    if digits[current_index] >= digits[current_index + 1]:
        if is_first_run:
            return ""
        return is_decreasing(current_index=current_index + 1, digits=digits)
    return is_increasing(current_index=current_index + 1, is_first_run=False, digits=digits)


def is_decreasing(current_index, digits):
    if current_index == len(digits) - 1 or digits[current_index] < digits[current_index + 1]:
        return current_index + 1
    return is_decreasing(current_index=current_index + 1, digits=digits)






def zad_3_3():
    digits = sanitize_input(True)
    all_sequences = {}
    for main_idx in range(len(digits) - 2):
        # if main_idx==9390:
        end_idx = is_increasing(current_index=main_idx, is_first_run=True, digits=digits)
        if not end_idx:
            continue
        all_sequences[main_idx] = ''.join(str(item) for item in digits[main_idx: end_idx])
        a = 1
    x = dict(filter(lambda item: len(item[1])>=6, all_sequences.items()))
    print(x)
    print(len(dict(filter(lambda item: len(item[1])>=6, all_sequences.items()))))
    # print(len(dict(filter(lambda item: len(item[1])==max(all_sequences.values(), key=len), all_sequences.items()))))
    inner_index = 1
    inner_index = 1











if __name__ == '__main__':
    zad_3_3()
