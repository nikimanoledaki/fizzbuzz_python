import numbers
import sys

class FizzBuzzError(Exception):
    """An exception class for fizzbuzz."""

class FizzBuzz:
    """A fizzbuzz-ifying programme."""
     
    def run(self, number):
        self._check_operand(number)
        result = []
        x = range(start=1, end=number + 1)
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

if __name__ == '__main__':
    print("Lets FizzBuzz-ify numbers!")
    fizzbuzz = FizzBuzz() 
    programme = [fizzbuzz.run]

    while True:
        print("q: quit")
        programme = input("Pick a number, any number: ")
        if programme == 'q':
            sys.exit()
