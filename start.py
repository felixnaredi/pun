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

"""Start program by running this file."""

import curses
import numpy as np
from pun.adjecentlist import connect, preppend
from pun.term import draw_snake, init, end


STDSRC = init()
(MAXY, MAXX) = STDSRC.getmaxyx()
PAD = curses.newpad(MAXY, MAXX)

SNK = connect(([0, 0], [4, 4]))

while True:
    PAD.clear()
    draw_snake(SNK, PAD)
    PAD.refresh(0, 0, 0, 0, MAXY, MAXX)

    D = {97: np.array([0, -1]),
         115: np.array([1, 0]),
         100: np.array([0, 1]),
         119: np.array([-1, 0]),
         113: 'quit'}[STDSRC.getch()]

    if D == 'quit':
        break
    SNK = preppend(SNK, SNK[0] + D, keep_length=True)

end()
