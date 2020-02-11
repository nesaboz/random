"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

import timeit


elements = [1, 2, 3, 4, 5]


def method_1():
    # the first pass will just multiply all the numbers
    # the second pass will just divide the each number with the element
    product = 1
    for element in elements:
        product *= element

    result = [int(product/element) for element in elements]

    return result

def method_2():
    product = 1
    result = [0] * len(elements)
    for idx, element in enumerate(elements):
        copy = [x for x in elements]
        copy.remove(element)
        product = 1
        for element in copy:
            product *= element

        result[idx] = product

    return result


def method_3():
    #  with the first pass each result element will

    result = [1] * len(elements)
    for idx, element in enumerate(elements):
        for idx2, element2 in enumerate(elements):
            if idx2 != idx:
                result[idx] *= element2
    return result


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("method_3()", setup="from __main__ import method_3"))
