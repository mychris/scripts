#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SYNOPSIS

    colors.py

DESCRIPTION

    Prints a simple color table

LICENSE

    Copyright (C) 2011 Christoph Göttschkes <just.mychris@googlemail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import print_function

if __name__ == "__main__":
    try:
        range = xrange
    except NameError:
        pass

    for i in range(2):
        for j in range(30, 38):
            for k in range(40, 48):
                print("\33[%d;%d;%dm%d;%d;%d\33[m " % (i, j, k, i, j, k, ), end="")
            print()
