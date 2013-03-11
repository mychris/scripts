#!/usr/bin/env perl

use warnings;
use strict;

print int(rand($ARGV[0])) + 1 . "\n" if ($ARGV[0] && $ARGV[0] =~ /^[0-9]+$/);

