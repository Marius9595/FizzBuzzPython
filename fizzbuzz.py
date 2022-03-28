
def fizz_buzz():
    pass

def evaluate_number(number):

    value = ''

    if number % 3 == 0:
        value += 'Fizz'
    if number % 5 == 0:
        value += 'Buzz'
    if value == '':
        value = str(number)

    return value

fizz_buzz()
