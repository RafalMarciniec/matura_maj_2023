from collections import defaultdict

path_to_file = r"data\pi.txt"


# path_to_file = r"data\pi_przyklad.txt"

def sanitize_input(is_digits=False):
    with open(path_to_file, "r") as f:
        if is_digits:
            return [int(item.replace("\n", "")) for item in f.readlines()]
        raw_input = [str(item.replace("\n", "")) for item in f.readlines()]
        sanitized = []
        for idx in range(len(raw_input) - 1):
            sanitized.append(int(raw_input[idx] + raw_input[idx + 1]))
        return sanitized

def ex_3_1(pairs):
    print(f"Exercise 3.1 {len(list((filter(lambda x: x > 90, pairs))))}")


def ex_3_2(pairs):
    # here is a problem when 00 not exist but problem is only for not existing keys in example
    ocurrences = defaultdict(int)
    for unique_number in set(pairs):
        ocurrences[unique_number] += pairs.count(unique_number)
    print("Exercise 3.2")
    print(f"MAX key {max(ocurrences, key=ocurrences.get)}, value {max(ocurrences.values())}")
    print(f"MIN key {min(ocurrences, key=ocurrences.get)}, value {min(ocurrences.values())}")


def get_end_index(main_idx, digits, is_increasing=True, is_first_recursion=False):
    if len(digits) - 1 == main_idx:
        return main_idx + 1
    if is_first_recursion:
        if digits[main_idx] >= digits[main_idx + 1]:
            return
        return get_end_index(main_idx=main_idx + 1, digits=digits)
    if is_increasing:
        if digits[main_idx] < digits[main_idx + 1]:
            return get_end_index(main_idx=main_idx + 1, digits=digits)
        elif digits[main_idx] == digits[main_idx + 1] and digits[main_idx + 1] < digits[main_idx + 2]:
            return
        return get_end_index(main_idx=main_idx + 1, digits=digits, is_increasing=False)
    else:
        if digits[main_idx] <= digits[main_idx + 1]:
            return main_idx + 1
        return get_end_index(main_idx=main_idx + 1, digits=digits, is_increasing=False)


def ex_3_3_and_4(digits):
    all_sequences = {}
    for main_idx in range(len(digits) - 2):
        end_index = get_end_index(main_idx=main_idx, digits=digits, is_first_recursion=True)
        if end_index:
            all_sequences[main_idx] = digits[main_idx: end_index]
    max_6 = list(filter(lambda x: len(x) >= 6, all_sequences.values()))
    print(f"Exercise 3.3 {len(max_6)}")
    print(f"Exercise 3.4 {(max(all_sequences.items(), key=lambda x: len(x[1])))}")


if __name__ == '__main__':
    input_for_ex_1_2 = sanitize_input()
    ex_3_1(input_for_ex_1_2)
    ex_3_2(input_for_ex_1_2)
    input_for_ex_3_4 = sanitize_input(True)
    ex_3_3_and_4(input_for_ex_3_4)
