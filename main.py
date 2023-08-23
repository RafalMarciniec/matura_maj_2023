from collections import defaultdict

path_to_file = r"data\pi.txt"


path_to_file = r"data\pi_przyklad.txt"


def sanitize_input(is_digits=False):
    with open(path_to_file, "r") as f:
        if is_digits:
            return [int(item.replace("\n", "")) for item in f.readlines()]
        x = [str(item.replace("\n", "")) for item in f.readlines()]
        pairs = []
        for idx in range(len(x) - 1):
            pairs.append(int(x[idx] + x[idx + 1]))
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


def zad_3_3():
    digits = sanitize_input(True)
    all_sequences = []
    is_increasing = True
    end_index = 0
    start_index = 0
    while end_index < len(digits) - 1:
        if is_increasing:
            if digits[end_index] < digits[end_index + 1]:
                end_index += 1
            else:
                end_index += 1
                is_increasing=False
        else:
            if digits[end_index] < digits[end_index + 1]:
                all_sequences.append("".join([str(digit) for digit in digits[start_index:end_index + 1]]))
                start_index = end_index
                is_increasing = True
            else:
                end_index += 1
    print(list(filter(lambda x: len(x)==6, all_sequences)))
    a = 1
    a = 1

if __name__ == '__main__':
    zad_3_3()
