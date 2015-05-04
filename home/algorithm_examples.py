__author__ = 'lb'

import sys


class Summation(object):

    @staticmethod
    def nth_digit_array(numbers=None, index=None):
        return [int(x[index]) for x in numbers if len(x) > index]

    @staticmethod
    def sum(numbers=[]):
        s = Summation
        numbers = list(map(str, numbers))
        final_sum = ''  # built as a string
        remainder = 0
        magitude = len(max(numbers, key=len))
        for index in range(magitude):
            array_sum = sum(s.nth_digit_array((n[::-1] for n in numbers), index))
            current_sum = array_sum + remainder
            if index + 1 < magitude:
                final_sum += str(current_sum)[-1]
                remainder = int(str(current_sum)[:-1]) if len(str(current_sum)) > 1 else 0
            else:
                final_sum += str(current_sum)[::-1]
        return final_sum[::-1]



class Multiplier(object):

    @staticmethod
    def multiply_as_string(num1, num2):
        m = Multiplier
        s = Summation

        individual_sum = []
        for index, digit in enumerate(reversed(str(num2))):
            this_sum = m.multiply_through(int(digit), num1)
            individual_sum.append(this_sum + '0' * index)

        grand_sum = s.sum(individual_sum)

        return grand_sum


    @staticmethod
    def multiply_through(digit, num):
        digit, num = int(digit), str(num)
        remainder = 0
        product = ''
        for index in range(len(num)):
            current_sum = str(int(num[::-1][index]) * digit + int(str(remainder)[-1]))
            if index < len(num) - 1:
                product += current_sum[-1]
                remainder = int(current_sum[:-1]) if len(str(current_sum)) > 1 else 0
            else:
                product += current_sum[::-1]
        return product[::-1]






class Euler(object):

    def __init__(self, input_file=None, numbers=None):
        self.file = input_file
        self.numbers = self.load_numbers() if not numbers else numbers

    def load_numbers(self):
        if self.file:
            with open(self.file, 'r') as numbers:
                return [n for n in numbers.read().splitlines() if len(n)]


    def nth_digit_array(self, n=None):
        return [int(x[n]) for x in self.numbers]

    @property
    def grand_sum(self):
        final_sum = '' # built as a string
        remainder = 0
        for digit in range(len(self.numbers[0]) - 1, -1, -1):
            array_sum = sum(self.nth_digit_array(digit))
            if digit > 0:
                current_sum = array_sum + remainder
                final_sum += str(current_sum)[-1]
                remainder = int(str(current_sum)[:-1])
            else:
                current_sum = array_sum + int(str(remainder))
                final_sum += str(current_sum)[::-1]
        return final_sum[::-1]

    @property
    def first_ten(self):
        return self.grand_sum[:10]

    @staticmethod
    def sum_digits_factorial(num):
        if type(num) is not int:
            num = int(num)
        pairs = []
        for x in range(1, int((num / 2) + 1)):
            opposite = num + 1 - x
            pairs.append(opposite * x)

        print(pairs)
        m = Multiplier
        current_product = pairs[0]
        for product in pairs[1:]:
            current_product = m.multiply_as_string(current_product, str(product))
            print(current_product)

        return sum(map(int, current_product))

        # return pairs


























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
    # number1, number2 = 6112312231223423423423423424331231231231233, 43412312312312332342342342342342342341235
    # number = number1 * number2
    # print(number)
    # e = Multiplier.multiply_as_string(number1, number2)
    # print(e)
    # assert e == str(number)
    # e = Euler(sys.argv[1])
    # print(e.grand_sum)
    # print(len(e.grand_sum))
    # print(e.first_ten)
    sum_digits = Euler.sum_digits_factorial(int(sys.argv[1]))
    print(sum_digits)
    # prod = 1
    # for x in range(10):
    #     prod *= sum_digits[x]
    #     print(prod)