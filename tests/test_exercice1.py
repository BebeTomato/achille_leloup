import pytest
import os
from subprocess import check_output, PIPE
from nose.tools import assert_equal

os.chdir('..')
command = ['./exercice1.py']

def test_add():
    expected = "10"
    args = ["5", "5"]
    output = check_output(command + args, stderr=PIPE).decode()
    assert_equal(output.split('\n')[0], expected)

def test_subtract():
    expected = "2"
    args = ["7", "5"]
    output = check_output(command + args, stderr=PIPE).decode()
    assert_equal(output.split('\n')[1], expected)

def test_multiply():
    expected = "15"
    args = ["3", "5"]
    output = check_output(command + args, stderr=PIPE).decode()
    assert_equal(output.split('\n')[2], expected)

def test_divide():
    expected = "2.0"
    args = ["10", "5"]
    output = check_output(command + args, stderr=PIPE).decode()
    assert_equal(output.split('\n')[3], expected)

def test_power():
    expected = "8"
    args = ["2", "3"]
    output = check_output(command + args, stderr=PIPE).decode()
    assert_equal(output.split('\n')[4], expected)

def test_sqrt():
    expected = "2.0"
    args = ["4"]
    output = check_output(command + args, stderr=PIPE).decode()
    assert_equal(output.split('\n')[5], expected)