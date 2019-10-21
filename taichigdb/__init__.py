#!/usr/bin/env python

import gdb
import re
import itertools
import numpy as np
from bisect import bisect_left

logfile = open('/tmp/taichigdb.log', 'w')


def log(msg):
    logfile.write(str(msg) + '\n')
    logfile.flush()


class TaichiMatrixPrinter:
    "Print Taichi Matrix or Array of some kind"

    def __init__(self, val):
        "Extract all the necessary information"

        # The gdb extension does not support value template arguments - need to extract them by hand
        type = val.type
        if type.code == gdb.TYPE_CODE_REF:
            type = type.target()
        self.type = type.unqualified().strip_typedefs()
        tag = self.type.tag
        regex = re.compile('\<.*\>')
        m = regex.findall(tag)[0][1:-1]
        template_params = m.split(',')
        template_params = [x.replace(" ", "") for x in template_params]

        self.dim = int(template_params[0])
        self.rows = self.cols = self.dim
        self.scalar = self.type.template_argument(1)
        self.val = val

    def to_string(self):
        mat = np.zeros((self.rows, self.cols), dtype=np.float64)
        for row in range(self.rows):
            for col in range(self.cols):
                mat[row, col] = float(self.val['d'][col]['d'][row])

        return "taichi::MatrixND<%d,%s>\n%s\n" % (self.dim, self.scalar, mat)


class TaichiVectorPrinter:
    "Print Taichi Vector of some kind"

    def __init__(self, val):
        "Extract all the necessary information"

        # The gdb extension does not support value template arguments - need to extract them by hand
        type = val.type
        if type.code == gdb.TYPE_CODE_REF:
            type = type.target()
        self.type = type.unqualified().strip_typedefs()
        tag = self.type.tag
        regex = re.compile('\<.*\>')
        m = regex.findall(tag)[0][1:-1]
        template_params = m.split(',')
        template_params = [x.replace(" ", "") for x in template_params]

        self.dim = int(template_params[0])
        self.rows = self.dim
        self.cols = 1
        self.scalar = self.type.template_argument(1)
        self.val = val

    def to_string(self):
        mat = np.zeros((self.rows, self.cols), dtype=np.float64)
        for row in range(self.rows):
            for col in range(self.cols):
                mat[row, col] = float(self.val['d'][row])

        return "taichi::VectorND<%d,%s>\n%s\n" % (self.dim, self.scalar, mat)


def build_taichi_dictionary():
    pretty_printers_dict[re.compile(
        '^taichi::MatrixND<.*>$')] = lambda val: TaichiMatrixPrinter(val)
    pretty_printers_dict[re.compile(
        '^taichi::VectorND<.*>$')] = lambda val: TaichiVectorPrinter(val)


def register_taichi_printers(obj):
    "Register taichi pretty-printers with objfile Obj"

    if obj == None:
        obj = gdb
    obj.pretty_printers.append(lookup_function)


def lookup_function(val):
    "Look-up and return a pretty-printer that can print va."

    type = val.type

    if type.code == gdb.TYPE_CODE_REF:
        type = type.target()

    type = type.unqualified().strip_typedefs()

    typename = type.tag
    if typename == None:
        return None

    for function in pretty_printers_dict:
        if function.search(typename):
            return pretty_printers_dict[function](val)

    return None


pretty_printers_dict = {}

build_taichi_dictionary()
