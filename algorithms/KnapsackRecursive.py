values = [1, 2, 3]
weights = [1, 2, 3]

weight = 3


def knapsack(weight, index):
    if weight == 0 or index == 0:
        return 0
    if weights[index] <= weight:
        return max(values[index] + knapsack(weight - weights[index], index - 1), 
                   knapsack(weight, index - 1))

    return knapsack(weight, index - 1)