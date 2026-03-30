def recursive_fibonacci(sequence_index):
    if sequence_index < 0:
        return
    if sequence_index <= 0:
        return 0
    if sequence_index == 1:
        return 1
    return recursive_fibonacci(sequence_index - 1) + recursive_fibonacci(sequence_index - 2)


print(recursive_fibonacci(5))


def iterative_fibonacci(sequence_index):
    if sequence_index < 0:
        return
    if sequence_index == 0:
        return 0
    if sequence_index == 1:
        return 1

    last_number = 1
    second_to_last_number = 0
    for i in range(sequence_index - 1):
        last_number += second_to_last_number
        second_to_last_number = last_number - second_to_last_number
    return last_number


print(iterative_fibonacci(5))
