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


def get_left_boundary(peak_index, digits):
    pass


def get_right_boundary(peak_index, digits):
    pass


def get_end_index(main_idx, digits, is_increasing=True, is_first_recursion=False):
    if len(digits) - 1 == main_idx:
        return main_idx +1
    if is_first_recursion:
        if digits[main_idx] >= digits[main_idx + 1]:
            return
        return get_end_index(main_idx=main_idx + 1, digits=digits)
    if is_increasing:
        if digits[main_idx] < digits[main_idx + 1]:
            return get_end_index(main_idx=main_idx + 1, digits=digits)
        elif digits[main_idx] == digits[main_idx + 1] and digits[main_idx+1] < digits[main_idx + 2]:
            return
        else:
            return get_end_index(main_idx=main_idx + 1, digits=digits, is_increasing=False)
    else:
        if digits[main_idx] <= digits[main_idx + 1]:
            return main_idx + 1
        else:
            return get_end_index(main_idx=main_idx + 1, digits=digits, is_increasing=False)

def kurwa_mac(xxxx):
    l = []
    for idx, a in enumerate(xxxx):
        x= [1]
        for b in range(1, len(a)-1):
            x.append(numpy.sign(a[b+1] - a[b]))
        l.append(x)
    a =1


def zad_3_3():
    # digits = sanitize_input(True)[9390:9398]
    digits = sanitize_input(True)
    all_sequences = {}
    for main_idx in range(len(digits) - 2):
        end_index = get_end_index(main_idx=main_idx, digits=digits, is_first_recursion=True)
        if end_index:
            all_sequences[main_idx] = digits[main_idx: end_index]
    max_6 = list(filter(lambda x: len(x)>=6, all_sequences.values()))
    print(len(max_6))
    print(max(all_sequences.items(), key = lambda x: len(x[1])))


if __name__ == '__main__':
    zad_3_3()
