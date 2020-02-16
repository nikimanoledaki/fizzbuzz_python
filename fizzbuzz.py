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
            raise FizzBuzzError('"{operand}" is not a number')

if __name__ == '__main__':
    print("Lets FizzBuzz-ify some numbers!")
    print("Press Ctrl+C to quit.")
    fizzbuzz = FizzBuzz()
    
    while True:
        number = int(input("Up to what number would you like to Buzzify? "))
        print(fizzbuzz.run(number))
