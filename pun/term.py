# BSD 2-Clause License
#
# Copyright (c) 2019, felixnaredi
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import curses


def init():
    """Initalizes curses as intended for the game. Returns stdscr.a"""

    stdscr = curses.initscr()
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(0)
    return stdscr


def end():
    """Ends the current curses process."""
    curses.endwin()


def draw_snake(snake, pad):
    """Draws a snake in a curses pad."""

    ps = [None] + snake + [None]
    for p in zip(ps[:-2], ps[1:-1], ps[2:]):
        d0 = None if p[0] is None else ((p[1] - p[0])[0], (p[1] - p[0])[1])
        d1 = None if p[2] is None else ((p[1] - p[2])[0], (p[1] - p[2])[1])

        c = {
            None:    {None: None, (-1, 0): '‥', (1, 0): '¨', (0, -1): ':', (0, 1): ':'},
            (-1, 0): {None: '╽', (-1, 0): None, (1, 0): '║', (0, -1): '╔', (0, 1): '╗'},
            (1, 0):  {None: '╿', (-1, 0): '║', (1, 0): None, (0, -1): '╚', (0, 1): '╝'},
            (0, -1): {None: '╼', (-1, 0): '╔', (1, 0): '╚', (0, -1): None, (0, 1): '═'},
            (0, 1):  {None: '╾', (-1, 0): '╗', (1, 0): '╝', (0, -1): '═', (0, 1): None},
        }[d0][d1]

        pad.addch(p[1][0], p[1][1], c)
