from unittest import TestCase


from fizzbuzz import evaluate_number

class TestFizzBuzz(TestCase):

    def test_if_number_is_not_divisible_by_3_neither_5_returns_the_number(self):

        number1 = evaluate_number(1)
        number2 = evaluate_number(22)
        number3 = evaluate_number(52)
        number4 = evaluate_number(77)
        number5 = evaluate_number(97)

        self.assertEqual(number1, '1')
        self.assertEqual(number2, '22')
        self.assertEqual(number3, '52')
        self.assertEqual(number4, '77')
        self.assertEqual(number5, '97')

    def test_if_number_is_divisible_by_3_returns_fizz_word(self):

        number1 = evaluate_number(3)
        number2 = evaluate_number(33)
        number3 = evaluate_number(99)

        self.assertEqual(number1, 'Fizz')
        self.assertEqual(number2, 'Fizz')
        self.assertEqual(number3, 'Fizz')

    def test_if_number_is_divisible_by_5_returns_fizz_word(self):

        number1 = evaluate_number(5)
        number2 = evaluate_number(55)
        number3 = evaluate_number(70)
        number4 = evaluate_number(100)

        self.assertEqual(number1, 'Buzz')
        self.assertEqual(number2, 'Buzz')
        self.assertEqual(number3, 'Buzz')
        self.assertEqual(number4, 'Buzz')

    def test_if_number_is_divisible_by_5_and_by_3_returns_fizzbuzz_word(self):

        number1 = evaluate_number(15)
        number2 = evaluate_number(75)

        self.assertEqual(number1, 'FizzBuzz')
        self.assertEqual(number2, 'FizzBuzz')