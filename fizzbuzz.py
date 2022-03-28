
def fizz_buzz():
    for number in range(1,101):
        print(evaluate_number(number))

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
