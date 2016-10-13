#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from argparse import ArgumentParser


def hello(args=sys.argv[1:]):
    argp = ArgumentParser(description='hello')
    argp.add_argument('msg', help='message to return')
    args = argp.parse_args(args)
    print(args.msg)
    return 0


if __name__ == '__main__':
    sys.exit(hello())
