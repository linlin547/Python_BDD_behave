#encoding=utf-8
from behave import *

def data_sum(num):
    return num+2
@given('we have the number {number}')
def have_number(context,number):
    context.fib_number = int(number)

@when('we calc the fib')
def calc_fib(context):
    context.fib_number = data_sum(context.fib_number)

@then('we get the fib number {number}')
def get_number(context,number):
    context.expected_number = int(number)
    if cmp(context.fib_number,context.expected_number) == 0:
        assert True
    else:
        assert False
