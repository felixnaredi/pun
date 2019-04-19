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
import time


def coords(p):
    xs = []
    for y in range(p[0]):
        for x in range(p[1]):
            xs.append((y, x))
    return xs

PUNLOGO = r"""   ____   _   _       _
  // //  //  //  /\  //
 //_//  //  //  //\\// 
//     //__//  //  \/  """
PUNLOGO_SIZE = (4, 24)


stdscr = curses.initscr()
stdscr.clear()
stdscr.refresh()

lgpad = curses.newpad(4, 24)
for (c, (y, x)) in zip(PUNLOGO, coords(PUNLOGO_SIZE)):
    lgpad.addch(y, x, c)

(h, w) = stdscr.getmaxyx()
for y in range(h):
    y_off = h - y - 1
    stdscr.clear()
    stdscr.refresh()
    lgpad.refresh(0, 0, y_off, 8, min(h - 1, y_off + PUNLOGO_SIZE[0]), 8 + PUNLOGO_SIZE[1])
    time.sleep(0.16)
stdscr.addstr(5, 4, '-' * min((w - 5), 28))
stdscr.addstr(7, 7, "New Game")
stdscr.addstr(9, 7, "Highscore")
    
stdscr.getch()

curses.endwin()