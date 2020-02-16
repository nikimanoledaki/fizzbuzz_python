class FizzBuzz:
    """A fizzbuzz-ifying programme."""
    
    def run(self, number):
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
