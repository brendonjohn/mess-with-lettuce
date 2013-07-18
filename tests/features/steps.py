__author__ = 'brendonjohn'

from lettuce import *
from fib import nth_fibonacci_number


@step("I want the (\d+)(\w+) fibonacci number")
def have_the_number(step, nth, suffix):
    print "requested %s%s" % (nth, suffix)
    world.nth = nth


@step("I calculate the nth fibonacci number")
def calculate_nth_fibonacci(step):
    world.nth_fibonacci = nth_fibonacci_number(int(world.nth))


@step("I obtain the number (\d+)")
def check_returned_number(step, expected):
    assert world.nth_fibonacci == int(expected), \
        "Got: %d, \nExpected: %s" % (world.nth_fibonacci, expected)