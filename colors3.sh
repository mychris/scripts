#!/usr/bin/env bash
#
#   This file displays a bunch of color codes to the 
#   terminal to demonstrate what's available.  Each 
#   line is the color code of one forground color,
#   out of 17 (default + 16 escapes), followed by a 
#   test use of that color on all nine background 
#   colors (default + 8 escapes).
#

T='gYw'   # The test text

printf "\n                 40m     41m     42m     43m     44m     45m     46m     47m\n";

for FGs in '    m' '   1m' '  30m' '1;30m' '  31m' '1;31m' '  32m' \
           '1;32m' '  33m' '1;33m' '  34m' '1;34m' '  35m' '1;35m' \
           '  36m' '1;36m' '  37m' '1;37m'; do
  FG=${FGs// /}
  printf " %s \x1B[%s  %s  " "$FGs" "$FG" "$T"
  for BG in 40m 41m 42m 43m 44m 45m 46m 47m; do
      printf "%s \x1B[%s\x1B[%s  %s  \x1B[0m" "$EINS" "$FG" "$BG" "$T"
  done
  printf "\n"
done
printf "\n"

# vim: ft=sh ts=2 sts=2 sw=2 et:
