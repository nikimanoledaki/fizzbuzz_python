class FizzBuzz:
    """A fizzbuzz-ifying programme."""
    
    def run(self, number):
        result = []
        x = range(1, number + 1)
        for n in x:
            if n % 3 == 0:
                result.append('Fizz')
            else:
                result.append(n)

        return result
