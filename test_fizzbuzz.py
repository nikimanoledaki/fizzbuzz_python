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
