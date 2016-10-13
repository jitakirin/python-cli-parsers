#!/usr/bin/env python
# -*- coding: utf-8 -*-

from defopt import run


def hello(msg):
    """hello

    :param str msg: message to return
    """
    print(msg)


if __name__ == '__main__':
    run(hello)
