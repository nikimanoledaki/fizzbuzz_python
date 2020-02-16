from fizzbuzz import FizzBuzz

def test_should_return_an_array():
    fizzbuzz = FizzBuzz()

    result = fizzbuzz.run(1)
    assert result == [1]

def test_should_return_an_array_with_range():
    fizzbuzz = FizzBuzz()

    result = fizzbuzz.run(2)
    assert result == [1, 2]

def test_should_fizz_for_multiples_of_3():
    fizzbuzz = FizzBuzz()

    result = fizzbuzz.run(3)
    assert result == [1, 2, 'Fizz']

def test_should_buzz_for_multiples_of_5():
    fizzbuzz = FizzBuzz()

    result = fizzbuzz.run(5)
    assert result == [1, 2, 'Fizz', 4, 'Buzz']

def test_should_fizzbuzz_for_multiples_of_15():
    fizzbuzz = FizzBuzz()

    result = fizzbuzz.run(15)
    assert result == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
