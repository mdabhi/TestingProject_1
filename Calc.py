#!/usr/bin/env python2.7

def addition(x, y):
    """Add function"""
    return x + y


def subtract(x, y):
    """Subtract function"""
    return x - y


def multiply(x, y):
    """Multiply function"""
    return x * y


def divide(x, y):
    """Division function"""
    if y == 0:
        raise ValueError("Can not divide by the zero!")
    return x / y

