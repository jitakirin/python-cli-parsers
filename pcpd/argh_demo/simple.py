#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argh


@argh.arg('msg', help='message to return')
def hello(msg):
    """hello"""
    yield msg


if __name__ == '__main__':
    argh.dispatch_command(hello)
