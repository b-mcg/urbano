#!/usr/bin/env python2

# Imports
import argparse
from textwrap import wrap
from urbano.udcontentclass import UD


# Author and licensing
__Author__ = "b-mcg"
__Email__ = "b-mcg0890@gmail.com"
__License__ = """
Copyright (C) 2014-2016  b-mcg   <bmcg0890@gmail.com>

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

# Version number
VERSION     =       'v0.0.1-1'


def build_opts():
    """
    Builds and returns a parser object of command line arguments
    
    """
    parser      =       argparse.ArgumentParser(description='urbano command line options.')

    # Add word option
    parser.add_argument('word', type=str, nargs='+',
                help='word to lookup the definition for.',
                metavar=''
                )

    return parser


def arg_parser(parser):
    """
    Parses command line arguments and returns a dictionary
    of argument values

    parser  :   object containing valid command line options

    """
    
    # Parse arguments
    args        =       parser.parse_args()

    return {'w' : args.word}

def print_data(dct, count, tagkeys):
    """
    Prints out definition
    data contained in dct
    and returns a new count.

    @param dct: JSON data from ud api
    @param count: definition count number
    @param tagkeys: definition related keys for dct

    @return returns new definition count

    """

    print "{0:>5}:".format(count)

    for key in xrange(len(tagkeys)):
        
        print "\n\t{0}:\n\t\t{1}\n".format(tagkeys[key],
                '\n\t\t'.join(wrap(dct[tagkeys[key]].strip("\n").replace("\r", " ")))
                )

    count  +=  1
    return count


class _GetchUnix:
    """
    Class for grabbing unbuffered
    keyboard input.

    """
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def main():
    """
    main()

    """
    args    =   arg_parser(build_opts())

    ud      =   UD(' '.join(args['w']))


    json    =   ud.grabJSON()

    # JSON dictionary keys needed
    keys    =   ["word", "definition", "example", "author"]

    defcnt  =   1

    json_list   =   json['list']

    # Display first definition
    defcnt  =   print_data(json_list[0], defcnt, keys)

    json_list.pop(0)

    getch   =   _GetchUnix()

    # Loop until json_list is empty; show next definition upon spacebar event
    while True:

        ch  =   getch()

        if len(json_list) == 0:
            break

        elif ch == ' ':
            
            defcnt  =   print_data(json_list[0], defcnt, keys)
            
            json_list.pop(0)

        elif ch == 'q':
            break




if __name__ ==  '__main__':
    print "urabno {0} running by b-mcg...\n".format(VERSION)
    print "Press space to list more definitions.\n"
    main()
    print "\n"
