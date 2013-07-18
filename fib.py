__author__ = 'brendonjohn'


def nth_fibonacci_number(n, latest_number=1, previous_number=0):
    if n is not 1:
        new_number = latest_number + previous_number
        return nth_fibonacci_number(n - 1, new_number, latest_number)

    return latest_number
