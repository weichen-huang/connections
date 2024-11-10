import itertools
from itertools import combinations
from scipy.optimize import linear_sum_assignment


def create_subsets(words, n=2):
    return list(itertools.combinations(words, n))


def min_swaps(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same number of sets")

    cost_matrix = []

    for set1 in list1:
        row = []
        for set2 in list2:
            diff1 = set1 - set2
            diff2 = set2 - set1
            swaps_needed = max(len(diff1), len(diff2)) // 2
            row.append(swaps_needed)
        cost_matrix.append(row)

    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    min_swaps = sum(cost_matrix[i][j] for i, j in zip(row_ind, col_ind))

    return min_swaps


