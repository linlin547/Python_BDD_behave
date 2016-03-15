#encoding=utf-8
from behave import *

def data_sum(num):
    return num+2
@given('we have the number {number}')
def have_number(context,number):
    context.fib_number = int(number)

@when('we calc the fib')
def calc_fib(context):
    """此处context.before_data为environment.py中的变量,
    before_all函数在step之前运行,所以在运行step时变量已被赋值"""
    context.fib_number = data_sum(int(context.fib_number)+context.before_data)

@then('we get the fib number {number}')
def get_number(context,number):
    context.expected_number = int(number)
    if cmp(context.fib_number,context.expected_number) == 0:
        assert True
    else:
        assert False
