#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click


@click.command()
@click.argument('msg')
def hello(msg):
    """Return specified message."""
    click.echo(msg)
    return 0


if __name__ == '__main__':
    hello()
