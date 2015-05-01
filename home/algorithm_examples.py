__author__ = 'lb'

import sys

def algorithm_container():

    def nth_fibonacci(n, index=0, fib=0, next_fib=1):
        """
        :param n, index, fib, next_fib: ``int``
        :return: ``int`` describing the n-th fibonacci number
        """
        return fib if index == n else nth_fibonacci(
            n, index=index + 1, fib=next_fib, next_fib=fib + next_fib
        )

    def convert_from_hex(hexadecimal):
        """
        :param hexadecimal: ``str`` of number in base-16   (e.g. 3f4)
        :return: base-10 num
        """
        MAP = {
            'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
        }
        return sum((16 ** index) * (int(num) if num.isdigit() else MAP[num])
                   for index, num in enumerate(hexadecimal[::-1]))

    """
    Starting with any positive integer, replace the
    number by the sum of the squares of its digits,
    and repeat the process until the number equals 1 (where it will stay),
    or it loops endlessly in a cycle which does not include 1.
    """
    def is_happy(num, iteration=0, seen=()):
        if num == 1:
            return 1
        elif num in seen:
            return 0
        else:
            return is_happy(
                num=sum(int(x) ** 2 for x in str(num)),
                iteration=iteration + 1,
                seen=seen + (num,)
            )

    def reduce_and_count(array, aggregator=1):
        """
        :param array: ``list`` to be shortened
        :param aggregator: ``int`` acting as counter
        :return: ``list``-- rest of array
                 ``int``-- counter
                 ``int``-- symbol we have been counting
        """
        if len(array) == 1 or array[0] != array[1]:
            return array[1:], aggregator, array[0]
        else:
            return reduce_and_count(
                array=array[1:],
                aggregator=aggregator + 1
            )

    def build_sequence(sequence=None, interpreted=()):
        """
        :param sequence: ``list`` we want to compress
        :return: ``list`` of properly compressed sequence
        """
        if len(sequence) == 0:
            return interpreted
        else:
            array, count, elem = reduce_and_count(array=sequence)
            return build_sequence(
                interpreted=interpreted + ((str(count), elem),),
                sequence=array
            )


    list_comp = [x for x in range(10) if x % 2 == 0]

    # same as
    list_comp = []
    for x in range(10):
        if x % 2 == 0:
            list_comp.append(x)


    # generators
    summation = sum(x for x in range(10) if x % 2 == 0)


    # ternary operators


    # dealing with ranges
    if 0 < a < 10:
        pass

## suppose we only need to read this once
def square_map_generator(max):
    for x in range(max + 1):
        square = x ** 2
        if square <= max:
            yield square



def build_square_map(max):
    map = []
    for x in range(max + 1):
        square = x ** 2
        if square <= max:
            map.append(square)
        else:
            break
    return map

def double_squares(number):
    double_squares_found = []
    SQUARES_MAP = build_square_map(max=number)
    for square in reversed(SQUARES_MAP):
        step_one = number - square
        for next_square in SQUARES_MAP:
            step_two = step_one - next_square
            if step_two == 0:
                pair = (square, next_square)
                if pair not in double_squares_found and pair[::-1] not in double_squares_found:
                    double_squares_found.append(pair)
    return len(double_squares_found)

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases.read().splitlines()[1:]:
            if len(test):
                print double_squares(int(test))