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
    if peak_index - 1 == 0:
        return 0
    if digits[peak_index] > digits[peak_index - 1]:
        return get_left_boundary(peak_index=peak_index - 1, digits=digits)
    return peak_index


def get_right_boundary(peak_index, digits):
    if peak_index + 1 == len(digits) - 1:
        return peak_index + 1
    if digits[peak_index] > digits[peak_index + 1]:
        return get_right_boundary(peak_index=peak_index + 1, digits=digits)
    return peak_index + 1


def i_have_no_idea_how_to_name_that_function(peak_index, is_upland, digits):
    right_peak = peak_index
    if is_upland:
        right_peak += 1
    return digits[get_left_boundary(peak_index=peak_index, digits=digits): get_right_boundary(peak_index=right_peak,
                                                                                              digits=digits)]


def zad_3_3():
    digits = sanitize_input(True)
    all_sequences = {}
    for main_idx in range(len(digits) - 2):
        if digits[main_idx] == digits[main_idx + 1]:
            result = i_have_no_idea_how_to_name_that_function(peak_index=main_idx, is_upland=True,
                                                                               digits=digits)
            # if len(result)<3:
                # continue
            all_sequences[main_idx] = result
        if digits[main_idx] > digits[main_idx + 1] and digits[main_idx - 1] < digits[main_idx]:
            all_sequences[main_idx] = i_have_no_idea_how_to_name_that_function(peak_index=main_idx, is_upland=False,
                                                                               digits=digits)
    len_6 = list(filter(lambda val: len(val)>=6, all_sequences.values()))
    print(len(len_6))

if __name__ == '__main__':
    zad_3_3()
