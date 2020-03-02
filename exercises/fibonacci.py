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

# Fibonacci series:
a, b = 0, 1
while a < 10000:
    print("Fn = {}".format(a))
    a, b = b, a + b
