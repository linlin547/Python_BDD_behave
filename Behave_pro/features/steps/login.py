#encoding=utf-8
from behave import *

#coding=utf-8

from nose.tools import *
from behave import *
def cm(st):
    return st

@given(u'我在{text_field_id}输入{text}')
def step_impl(context, text_field_id, text):
    context.text_field = text_field_id
    context.text = text

@when(u'我点击{text_on_button}按钮')
def step_impl(context, text_on_button):
    context.driverx = cm(text_on_button)


@then(u'我应该看到{label_id}是{expected_text}')
def step_impl(context, label_id, expected_text):
    assert label_id == expected_text