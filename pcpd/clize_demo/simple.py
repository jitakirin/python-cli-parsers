#!/usr/bin/env python
# -*- coding: utf-8 -*-

from clize import run


def hello(msg):
    """hello

    msg: message to return
    """
    return msg


if __name__ == '__main__':
    run(hello)
