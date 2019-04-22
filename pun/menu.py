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

class Menu:
    """Main menu of the game."""

    LOGO = r"""   ____   _   _       _
  // //  //  //  /\  //
 //_//  //  //  //\\// 
//     //__//  //  \/  """
    LOGO_SIZE = (4, 24)

    def __init__(self, screen):
        self.screen = screen
        self.option = None

    @staticmethod
    def __logo_pad():
        (h, w) = Menu.LOGO_SIZE
        pad = curses.newpad(h, w)
        for (c, (y, x)) in zip(Menu.LOGO, [(y, x) for y in range(h) for x in range(w)]):
            pad.addch(y, x, c)
        return pad

    def __intro(self):
        lgpad = Menu.__logo_pad()
        (lg_h, lg_w) = Menu.LOGO_SIZE
        h = self.screen.getmaxyx()[0]

        for y in range(h):
            y_off = h - y - 1
            self.screen.clear()
            self.screen.refresh()
            lgpad.refresh(0, 0, y_off, 8, min(h - 1, y_off + lg_h), 8 + lg_w)
            time.sleep(0.16)

    def run(self):
        w = self.screen.getmaxyx()[1]
        self.__intro()

        scr = self.screen
        scr.addstr(5, 4, '-' * min((w - 5), 28))
        scr.addstr(7, 7, "New Game")
        scr.addstr(9, 7, "Highscore")
