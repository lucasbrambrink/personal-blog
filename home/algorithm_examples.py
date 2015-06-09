# coding=utf-8
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
        magnitude = len(max(numbers, key=len))
        for index in range(magnitude):
            array_sum = sum(s.nth_digit_array((n[::-1] for n in numbers), index))
            current_sum = array_sum + remainder
            if index + 1 < magnitude:
                final_sum += str(current_sum)[-1]
                remainder = int(str(current_sum)[:-1]) if len(str(current_sum)) > 1 else 0
            else:
                final_sum += str(current_sum)[::-1]
        return final_sum[::-1]



class Multiplier(object):

    @staticmethod
    def nth_digit_array(numbers=None, index=None):
        return [int(x[index]) for x in numbers if len(x) > index]

    @staticmethod
    def sum(numbers=[], ):
        s = Summation
        numbers = list(map(str, numbers))
        final_sum = ''  # built as a string
        remainder = 0
        magnitude = len(max(numbers, key=len))
        for index in range(magnitude):
            array_sum = sum(s.nth_digit_array((n[::-1] for n in numbers), index))
            current_sum = array_sum + remainder
            if index + 1 < magnitude:
                final_sum += str(current_sum)[-1]
                remainder = int(str(current_sum)[:-1]) if len(str(current_sum)) > 1 else 0
            else:
                final_sum += str(current_sum)[::-1]
        return final_sum[::-1]

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




class Palindrome(object):

    @staticmethod
    def is_palindrome(num):
        num = str(num)
        for x in range(int(len(num) / 2)):
            if num[x] != num[len(num) - 1 - x]:
                return False
        return True

    @staticmethod
    def highest_palindrome():
        max_palindrome = 0
        count = 0
        for x in range(999, -1, -1):
            new_range = x - 100 if x - 100 > -1 else -1
            for y in range(999, new_range, -1):
                product = x * y
                if Palindrome.is_palindrome(product):
                    if product > max_palindrome:
                        max_palindrome = product
        return max_palindrome



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

    @staticmethod
    def smallest_multiple(num):
        test = num + 1
        match = False
        while not match:
            match = True
            for x in range(num, 0, -1):
                if test % x:
                    match = False
                    break
            if not match:
                test += 1
        return test

    @staticmethod
    def sum_square_difference(num):
        sum_sqr = sum(x ** 2 for x in range(num + 1))
        sqr_sum = sum(x for x in range(num + 1)) ** 2
        delta = sqr_sum - sum_sqr
        return delta

    @staticmethod
    def nth_digit_fibonacci_index(n):
        pair, sum = [1, 2], '3'
        index = 4
        while len(sum) < n:
            pair = [pair[1], sum]
            sum = Summation.sum(pair)
            index += 1
        return index

    @staticmethod
    def pythagorean_triplet():

        def is_triplet(a, b, c):
            return a ** 2 + b ** 2 == c ** 2

        for x in range(1000):
            for y in range(x, 1000):
                z = 1000 - x - y
                if x < y < z and x + y + z == 1000:
                    if is_triplet(x, y, z):
                        return x, y, z, x * y * z


    @staticmethod
    def collatz_sequence(num):

        def process(n):
            if not n % 2:
                return n / 2
            else:
                return 3 * n + 1

        def collatz_sequence(num):
            original_num = int(num)
            length = 1
            while num != 1:
                num = process(num)
                length += 1
            return original_num, length


        max_length = (0, 0)
        for x in range(1000001):
            num, length = collatz_sequence(num=x)
            if length > max_length[1]:
                max_length = (num, length)

        return max_length[0]


    @staticmethod
    def circular_primes(n):
        pass



















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


def nth_power_of_two(n):
    product = 1
    for x in range(n):
        product = Multiplier.multiply_as_string(product, 2)
    return product, sum(int(x) for x in product)



# if __name__ == "__main__":
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
    # sum_digits = Euler.sum_digits_factorial(int(sys.argv[1]))
    # print(sum_digits)
    # prod = 1
    # for x in range(10):
    #     prod *= sum_digits[x]
    #     print(prod)
    # print(nth_power_of_two(int(sys.argv[1])))
    # print(Palindrome.is_palindrome('1001001'))
    # print(Palindrome.highest_palindrome())
    # print(Euler.sum_square_difference(int(sys.argv[1])))
    # print(Euler.nth_digit_fibonacci_index(int(sys.argv[1])))
    # print(Euler.collatz_sequence(int(sys.argv[1])))


class TestContainer:

    class Algorithms(object):
        """
        There are many online sources for fun and quick algorithm challenges to
        get our code-juices flowing and keep our CPUs busy.

        Examples:
            - codeeval.org
            - coderbyte.com

        These are great! Indeed, they form the foundation of my programming career.
        I remember writing my first is-prime function, and running through the house
        rejoicing, screaming late at night when all my assert statements passed.

        From that point on I was hooked on programming!


        """

        @staticmethod
        def is_prime(num=None):
            """
            :param num: ``int`` to be assessed
            :return: ``bool`` if argument is prime
            """
            # throw out negative numbers and zero
            if num <= 0:
                return False

            # upper range can be half of num --> we know that no number
            # greater than num/2 will ever be evenly divisible
            # adding one ensures proper inclusion of our range function
            for test in range(2, (num / 2) + 1):
                if num % test == 0:
                    return False
            return True

class ProjectEuler(object):

    """
    I recently stumbled upon Project Euler and instantly fell in love.

    From their website (projecteuler.net):

        'Project Euler is a series of challenging mathematical/computer programming problems
         that will require more than just mathematical insights to solve. Although mathematics
         will help you arrive at elegant and efficient methods, the use of a computer and
         programming skills will be required to solve most problems.'


    I want to draw attention to PEs difference from other, perhaps more popular sources:

        ``Most PE problem CANNOT be solved by brute force.``

    This constraint alone is so significant to our approach that one is FORCED to earnestly
    think about the problem. Awesome!

        “If I had an hour to solve a problem I'd spend 55 minutes thinking about the problem
         and 5 minutes thinking about solutions.”
            -- Albert Einstein

    Intrigued? Let's jump right in!
    """

    def large_sum(self):
        """
        Problem 13

        "Work out the sum of the following one-hundred 50-digit numbers."

            37107287533902102798797998220837590246510135740250
            46376937677490009712648124896970078050417018260538
            74324986199524741059474233309513058123726617309629
            etc.
        """

        ###---< Notes on the Problem >---###

        ### Order of Magnitude ###
        #  A fifty digit number, 10E50, is much larger than an int
        #       -- (maximum value 2^63 - 1, which is ~10E20) --
        #  Summing about 100 of these numbers puts our answer in the 10E52 range.
        #  While Python could perhaps handle such a number (as a long), we must set out do solve this
        #  analytically. What if we had to multiply these numbers?!
        #  After all, this could prove to be a very useful module for performing math with
        #  unreasonably big numbers.

        ### Thoughts on Approaches ###
        #  How could we do this?
        #  Well, what about the way we learned summation in elementary school?
        #  You know, work backwards digit by digit, summing each column, and carry the one!
        #  Except of course in this case, our remainder is much, much larger than 1...

        ### Elements of the Problem ###
        #  (1) Parse our input in a sensible way.
        #  (2) Pull out individual 'columns' at a given index (e.g. the tenth, or hundredth place, etc)
        #  (3) Sum these columns
        #  (4) Add the remainder to our total in a sensible way.
        #  (5) Return our final sum once we have iterated through every place value

        # Lets do this!
        pass

    """
    Let's knock out the first two:
         (1) parsing
         (2) pulling out individual columns per given place value
    """
    @staticmethod
    def load_numbers(path=None):
        """
        We can house our numbers in a .txt file, each separated by new lines ('\n')
        Thus we load them into python as strings. This is good.

        :param path: ``str`` to file
        :return: ``list`` containing our 50-digit numbers as ``str``

        """
        with open(path, 'r') as numbers_file:
            # note: splitlines() is a nice, pythonic way of splitting text into individual lines
            return [n for n in numbers_file.read().splitlines() if len(n)]

    @staticmethod
    def nth_digit_column(numbers=None, index=None):
        """
        :param numbers: ``list`` containing our numbers as ``str``
        :param index: ``int`` indicating place value of the column we need
        :return: ``list`` of ``int``, comprising of one vertical column for our summation
        """
        # note: by checking len, we can sum numbers of non-uniform length
        # (i.e. throw in a 20-digit number)
        return [int(x[index]) for x in numbers if len(x) > index]

    """
    Now for the fun part!!
        (3) Sum our columns
        (4) Add the remainder to our total in a sensible way.
        (5) Return our final sum once we have iterated through every place value
    """
    def sum(self, numbers=None):
        """
        :param numbers: ``list`` of ``str`` containing large numbers
        :return: ``str`` of our sum
        """
        total = ''     # let's build is as a string
        remainder = 0  # we start with a remainder of 0
        max_order_of_magnitude = len(max(numbers, key=len))  # establish our range

        # let's iterate through our summation backwards!
        for index in range(max_order_of_magnitude):
            # fetch our column at our specified index, from the back
            column_sum = sum(self.nth_digit_column((n[::-1] for n in numbers), index))
            # establish a working sum for this place value
            current_sum = column_sum + remainder

            # if we are NOT at the very last column
            if index + 1 < max_order_of_magnitude:
                # we want to add ONLY the LAST digit of our working sum!
                # we are moving digit by digit, after all
                total += str(current_sum)[-1]
                # now let's carry the one! Let's redefine our remainder!
                # from 13, you would carry 1, from 145 you need 14.
                # hence, we want up to the last digit, so we slice appropriately
                # note: we can use a ternary operator to deal with a remainder < 10 situation,
                remainder = int(str(current_sum)[:-1]) if current_sum > 9 else 0
            # if we ARE in fact at the last column
            else:  # we add the entire working sum!
                # note: because we are building our total backwards, we must invert our working sum!
                total += str(current_sum)[::-1]
        # since we built our total backwards, we need to re-map it forwards
        return total[::-1]

def stuff():


    """
    Let's see if it works!
    """
    if __name__ == "__main__":
        pe = ProjectEuler()
        numbers = pe.load_numbers(path=sys.argv[1])
        print(pe.sum(numbers))
        # 5537376230390876637302048746832985971773659831892672
        # This is indeed the right answer, as confirmed at projecteuler.net























