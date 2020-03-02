# -*- encoding: utf-8 -*-
#
# Author: Eduardo Estevez <estevez121@gmail.com>
# Last Updated: 12/21/2019
# @version
# @package
# @subpackage
# @copyright
# @license
#
# !/usr/bin/env python3.8

__version__ = "0.1"

import getopt
import sys

"""
Main Method
"""


def main():

    print("main")

    # Read command line args
    myopts, args = getopt.getopt(sys.argv[1:], "d:a")

    ###############################
    # o == option
    # a == argument passed to the o
    ###############################

    ###############################
    # -d == Only these domains
    # -a == All domains except the domains "exclude_domains" select in the file config.cgf
    ###############################

    for o, a in myopts:
        if o == '-d':
            print("Option -d");


if __name__ == "__main__":
    """
    main method
    """
    #main()

    print("""\
    Usage: thingy [OPTIONS]
         -h                        Display this usage message
         -H hostname               Hostname to connect to
    """)
