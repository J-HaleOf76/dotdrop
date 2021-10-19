"""
author: deadc0de6 (https://github.com/deadc0de6)
Copyright (c) 2017, deadc0de6

provide logging functions
"""

import sys
import inspect


class Logger:
    """logging facility for dotdrop"""

    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    LMAGENTA = '\033[35m'
    RESET = '\033[0m'
    EMPH = '\033[33m'
    BOLD = '\033[1m'

    def __init__(self, debug=False):
        self.debug = debug

    def log(self, string, end='\n', pre='', bold=False):
        """normal log"""
        cstart = self._color(self.BLUE)
        cend = self._color(self.RESET)
        if bold:
            bold = self._color(self.BOLD)
            fmt = '{}{}{}{}{}'.format(pre, cstart, bold,
                                      string, cend)
            fmt += '{}{}'.format(end, cend)
        else:
            fmt = '{}{}{}{}{}'.format(pre, cstart, string, end, cend)
        sys.stdout.write(fmt)

    def sub(self, string, end='\n'):
        """sub log"""
        cstart = self._color(self.BLUE)
        cend = self._color(self.RESET)
        sys.stdout.write('\t{}->{} {}{}'.format(cstart, cend, string, end))

    def emph(self, string, stdout=True):
        """emphasis log"""
        cstart = self._color(self.EMPH)
        cend = self._color(self.RESET)
        content = '{}{}{}'.format(cstart, string, cend)
        if not stdout:
            sys.stderr.write(content)
        else:
            sys.stdout.write(content)

    def err(self, string, end='\n'):
        """error log"""
        cstart = self._color(self.RED)
        cend = self._color(self.RESET)
        msg = '{} {}'.format(string, end)
        sys.stderr.write('{}[ERR] {}{}'.format(cstart, msg, cend))

    def warn(self, string, end='\n'):
        """warning log"""
        cstart = self._color(self.YELLOW)
        cend = self._color(self.RESET)
        sys.stderr.write('{}[WARN] {} {}{}'.format(cstart, string, end, cend))

    def dbg(self, string, force=False):
        """debug log"""
        if not force and not self.debug:
            return
        frame = inspect.stack()[1]
        mod = inspect.getmodule(frame[0]).__name__
        func = inspect.stack()[1][3]
        cstart = self._color(self.MAGENTA)
        cend = self._color(self.RESET)
        clight = self._color(self.LMAGENTA)
        bold = self._color(self.BOLD)
        line = '{}{}[DEBUG][{}.{}]{}{} {}{}\n'
        sys.stderr.write(line.format(bold, clight,
                                     mod, func,
                                     cend, cstart,
                                     string, cend))

    def dry(self, string, end='\n'):
        """dry run log"""
        cstart = self._color(self.GREEN)
        cend = self._color(self.RESET)
        sys.stdout.write('{}[DRY] {} {}{}'.format(cstart, string, end, cend))

    @classmethod
    def raw(cls, string, end='\n'):
        """raw log"""
        sys.stdout.write('{}{}'.format(string, end))

    def ask(self, query):
        """ask user for confirmation"""
        cstart = self._color(self.BLUE)
        cend = self._color(self.RESET)
        query = '{}{}{}'.format(cstart, query + ' [y/N] ? ', cend)
        resp = input(query)
        return resp == 'y'

    @classmethod
    def _color(cls, col):
        """is color supported"""
        if not sys.stdout.isatty():
            return ''
        return col
