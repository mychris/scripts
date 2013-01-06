#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ft=python :
# pylint: disable=C0103,W0622,W0702,W1401

from __future__ import print_function

if __name__ == "__main__":
    try:
        range = xrange
    except:
        pass

    for i in range(2):
        for j in range(30, 38):
            for k in range(40, 48):
                print("\33[%d;%d;%dm%d;%d;%d\33[m " %
                        (i, j, k, i, j, k), end="")
            print()

