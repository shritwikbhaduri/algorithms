from typing import List


def insertion_sort(input_list: List, order_by_decending: bool = False) -> List:
    """
    sort the input list in ascending or descending order according to insertion_sort algorithm
    :param order_by_decending: flag if true arrange the list in decending order
    :param input_list:
    :return:  list of sorted elements
    """
    for j in range(1, len(input_list)):
        key = input_list[j]
        i = j - 1
        while i >= 0 and key < input_list[i]:
            if order_by_decending:
                input_list[i] = input_list[i + 1]
                input_list[i] = key
            else:
                input_list[i+1] = input_list[i]
                input_list[i] = key
            i -= 1
    return input_list
