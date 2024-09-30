"""
:Date: 2024-09-30
:Version: 1
:Authors:
    - wjh
"""

import sys
import math


def rewrite(data: list[int], rules: dict[int, list[int]]) -> list[int]:
    """
    Rewrites provided list of data according to rules
    :param data: list to rewrite
    :param rules: dictionary which maps possible list elements to lists to which the elements will be expanded
    :returns: rewritten data according to rules
    """
    retval = []
    for num in data:
        if num in rules:
            retval.extend(rules[num])
        else:
            retval.append(num)
    return retval


def iterate_rewrite(data: list[int], rules: dict[int, list[int]], iterations_amount: int) -> list[int]:
    """
    Iterates the rewrite function using provided arguments the provided amount of times
    ..seealso:: rewrite
    :param data: list to rewrite
    :param rules: dictionary which maps possible list elements to lists to which the elements will be expanded
    :iterations_amount: amount of times the rewrite function should be called on data from previous iteration xor provided data
    :returns: rewritten data according to rules after provided amount of iterations
    """
    if iterations_amount < 0:
        raise RuntimeError("Amount of iterations specified smaller than 0: " + str(iterations_amount))
    retval = [d for d in data]
    for _ in range(iterations_amount):
        retval = rewrite(retval, rules)
    return retval


def list_to_str(data: list[int], conversions: dict[int, str]) -> str:
    """
    Converts provided list to a string using conversion rules
    ..seealso:: rewrite
    :param data: list to rewrite
    :param conversions: dictionary which maps possible list elements to strings to which the elements will be expanded
    :returns: list converted to a string according to conversion rules
    """
    retval = ""
    for element in data:
        if element in conversions:
            retval += conversions[element]
        else:
            raise RuntimeError("Encountered element " + str(element) + " was not covered by conversions dictionary " + str(conversions))
    return retval


def main():
    rules = {1: [1, 0, 1], 0: [0, 0, 0]}
    data = [1]
    line_width = 81
    if (len(sys.argv) > 1):
        for iterations_amount in sys.argv[1:]:
            iterations_amount = int(iterations_amount)
            rewritten_data = iterate_rewrite(data, rules, int(iterations_amount))
            conversions = {0: "_" * math.ceil(line_width / len(rewritten_data)), 1: "#" * math.ceil(line_width / len(rewritten_data))}
            print(list_to_str(rewritten_data, conversions))
    else:
        print("Usage:\npython " + sys.argv[0] + " <iterations_amount_0> <iterations_amount_1> ... <iterations_amount_n>")


if __name__ == "__main__":
    main()
