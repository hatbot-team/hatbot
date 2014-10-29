# -*- coding: utf-8 -*-
"""
A Python wrapper of the Yandex Mystem 3.0 morphological analyzer.
"""

from __future__ import print_function

import os
import select
import subprocess
import sys
from .constants import (MYSTEM_BIN, MYSTEM_EXE, MYSTEM_DIR)
from .installer import autoinstall
from .parsedinfo import WordInfo


if sys.version_info[0] < 3:
    from cStringIO import StringIO
else:
    from io import BytesIO as StringIO

try:
    import ujson as json
except ImportError:
    import json

_NL = bytes('\n', 'utf-8')
_POSIX = os.name == 'posix'
_PIPELINE_MODE = _POSIX and '__pypy__' not in sys.builtin_module_names



def _set_non_blocking(fd):
    """
    Set the file description of the given file descriptor to non-blocking.
    """

    if _PIPELINE_MODE:
        import fcntl
        flags = fcntl.fcntl(fd, fcntl.F_GETFL)
        flags = flags | os.O_NONBLOCK
        fcntl.fcntl(fd, fcntl.F_SETFL, flags)


class Mystem(object):

    """
    Wrap mystem binary to be able it use from Python.

    The two main methods you may use are the :py:meth:`__init__` initializer,
    and the :py:meth:`analyze` method to process your data and get mystem
    output results.

    :param  mystem_bin: path to mystem binary
    :type   mystem_bin: str
    :param  grammar_info: glue grammatical information for same lemmas in output.
    :type   grammar_info: bool
    :param  disambiguation: apply disambiguation
    :type   disambiguation: bool
    :param  entire_input: copy entire input to output
    :type   entire_input: bool

    .. note:: Default value of :py:attr:`mystem_bin` can be overwritted by :envvar:`MYSTEM_BIN`.
    """

    def __init__(self, mystem_bin=None, grammar_info=True, disambiguation=True, entire_input=False):
        self._mystem_bin = mystem_bin
        self._grammar_info = grammar_info
        self._disambiguation = disambiguation
        self._entire_input = entire_input
        self._procin = None
        self._procout = None
        self._procout_no = None
        self._proc = None

        if self._mystem_bin is None:
            self._mystem_bin = os.environ.get("MYSTEM_BIN", None)

        if self._mystem_bin is None:
            autoinstall()
            self._mystem_bin = MYSTEM_BIN

        self._mystemargs = ["--format", "json", "-f", "--eng-gr"]

        if self._grammar_info is True:
            self._mystemargs.append('-i')

        if self._disambiguation is True:
            self._mystemargs.append('-d')

        if self._entire_input is True:
            self._mystemargs.append('-c')

    def start(self):
        """
        Run mystem binary.

        .. note:: It is not mandatory to call it. Use it if you want to avoid waiting for mystem loads.
        """
        if self._proc is None:
            self._start_mystem()


    def _start_mystem(self):
        self._proc = subprocess.Popen([self._mystem_bin] + self._mystemargs,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE,
                                      bufsize=0,
                                      close_fds=True if _POSIX else False)

        self._procin, self._procout = self._proc.stdin, self._proc.stdout
        self._procout_no = self._procout.fileno()
        _set_non_blocking(self._procout)

    def analyze_word(self, text):
        """
        Make morphology analysis for a one word.

        :param  text:   text to analyze
        :type   text:   str
        :returns:       result of morphology analysis.
        :rtype:         dict
        """

        return WordInfo(self._analyze_impl(text.splitlines()[0])[0])


    def analyze_text(self, text):
        """
        Make morphology analysis for a text.

        :param  text:   text to analyze
        :type   text:   str
        :returns:       result of morphology analysis.
        :rtype:         dict
        """

        result = []
        for line in text.splitlines():
            result.extend([WordInfo(x) for x in self._analyze_impl(line)])
        return result

    if _PIPELINE_MODE:
        def _analyze_impl(self, text):
            self.start()

            self._procin.write(bytes(text, 'utf-8'))
            self._procin.write(_NL)
            self._procin.flush()

            sio = StringIO()
            obj = None
            select.select([self._procout_no], [], [])
            while True:
                try:
                    out = self._procout.read()
                    sio.write(out)
                    obj = json.loads(sio.getvalue().decode('utf-8'))
                    break
                except (IOError, ValueError):
                    rd, _, _ = select.select([self._procout_no], [], [], 30)
                    if self._procout_no not in rd:
                        raise RuntimeError("Problem has been occured. Current state:\ntext:\n%s\nout:\n%s\nsio:\n%s" %
                                           (text, out, sio.getvalue()))

            return obj
    else:
        def _analyze_impl(self, text):
            self.start()

            self._procin.write(bytes(text, 'utf-8'))
            self._procin.write(_NL)

            out, _ = self._proc.communicate()
            self._proc = None
            try:
                obj = json.loads(out.decode('utf-8'))
            except (IOError, ValueError):
                raise RuntimeError("Problem has been occured. Current state:\ntext:\n%s\nout:\n%s" %
                                   (text, out))

            return obj

