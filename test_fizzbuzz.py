from fizzbuzz import FizzBuzz

def test_should_return_an_array():
    fizzbuzz = FizzBuzz()

    result = fizzbuzz.run(1)
    assert result == [1]

def test_should_return_an_array_with_range():
    fizzbuzz = FizzBuzz()

    result = fizzbuzz.run(2)
    assert result == [1, 2]
