from collections import defaultdict

def get_unique_pairs(array_value):
    result = []
    if not array_value:
        return result
    sum_pairs_map = defaultdict(list)
    
    for a in range(len(array_value)):
        for b in range(a + 1, len(array_value)):
            pair = (array_value[a], array_value[b])
            pair_sum = sum(pair)
            sum_pairs_map[pair_sum].append(pair)

    sorted_pair_values = sorted(sum_pairs_map.items())
    for sum_pairs, pairs in sorted_pair_values:
        if len(pairs) >= 2:
            sorted_pairs = sorted(pairs)
            format_pairs = " ".join(f"( {a}, {b})" for a, b in sorted_pairs)
            result.append(f"Pairs : {format_pairs} have sum : {sum_pairs}")

    return result


def print_output(output):
    if output:
        print("Results:")
        for line in output:
            print(line)
    print()

if __name__ == "__main__":
    
    arr1 = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]
    output1 = get_unique_pairs(arr1)
    print("Input1 : ", arr1)
    print_output(output1)

    arr2 = [4, 23, 65, 67, 24, 12, 86]
    output2 = get_unique_pairs(arr2)
    print("Input2 : ", arr2)
    print_output(output2)
