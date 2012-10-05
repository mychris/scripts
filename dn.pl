#!/usr/bin/env perl

print int(rand($ARGV[0])) + 1 . "\n" if ($ARGV[0] && $ARGV[0] =~ /^[0-9]+$/);
