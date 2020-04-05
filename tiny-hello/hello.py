#!/usr/bin/env python3
"""
Author: kemokemo <t2wonderland@gmail.com>
Purpose: Say hello
"""

import argparse

def greet(name: str) -> str:
    """ greet returns a greeting message for 'name'. """
    return f'Hello, {name}!'

def test_greet() -> None:
    """ test for greet functionb. """
    assert greet('World') == 'Hello, World!'
    assert greet('KemoKemo') == 'Hello, KemoKemo!'

def main() -> None:
    """ endpoint of this app. """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('name', help='Name to greet')
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == '__main__':
    main()
