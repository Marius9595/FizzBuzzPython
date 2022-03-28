from unittest import TestCase


from fizzbuzz import evaluate_number

class TestFizzBuzz(TestCase):

    def test_if_number_is_not_divisible_by_3_neither_5_returns_the_number(self):

        number1 = evaluate_number(1)
        number2 = evaluate_number(22)
        number3 = evaluate_number(52)
        number4 = evaluate_number(77)
        number5 = evaluate_number(97)

        self.assertEqual(number1, 1)
        self.assertEqual(number2, 22)
        self.assertEqual(number3, 52)
        self.assertEqual(number4, 77)
        self.assertEqual(number5, 97)

