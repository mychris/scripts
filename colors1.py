#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103,W0622,W0702,W1401

import os
import sys

if __name__ == "__main__":
  for i in range(2):
    for j in range(30, 38):
      for k in range(40, 48):
        sys.stdout.write("\33[{0};{1};{2}m{0};{1};{2}\33[m ".format(i, j, k))
      sys.stdout.write(os.linesep)

# vim: ft=python ts=2 sts=2 sw=2 et:
