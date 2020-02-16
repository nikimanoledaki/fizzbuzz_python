import numbers

class FizzBuzzError(Exception):
    """An exception class for fizzbuzz."""

class FizzBuzz:
    """A fizzbuzz-ifying programme."""
     
    def run(self, number):
        self._check_operand(number)
        result = []
        x = range(1, number + 1)
        for n in x:
            if n % 3 == 0 and n % 5 == 0:
                result.append('FizzBuzz')
            elif n % 3 == 0:
                result.append('Fizz')
            elif n % 5 == 0:
                result.append('Buzz')
            else:
                result.append(n)

        return result

    def _check_operand(self, operand):
        if not isinstance(operand, numbers.Number):
            raise FizzBuzzError(f'"{operand}" was not a number')
