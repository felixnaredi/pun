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

"""Test cases for adjecent list functions."""

import unittest
import numpy as np
import pun.adjecentlist as adj


class AdjecentListTest(unittest.TestCase):
    """Test cases for adjecent list functions."""

    def __array_equal(self, a1, a2):
        """Fails if array a1 and a2 are not equal."""

        self.assertEqual(len(a1), len(a2))
        for e in zip(a1, map(np.array, a2)):
            self.assertTrue(np.array_equal(e[0], e[1]))

    def test_connect(self):
        """Test the connect function."""

        # Single point.
        self.__array_equal(adj.connect([[0, 0]]), [[0, 0]])

        # Connect two points.
        self.__array_equal(adj.connect(
            ([0, 0], [2, 0])), ([0, 0], [1, 0], [2, 0]))
        self.__array_equal(adj.connect(
            ([0, 0], [0, 2])), ([0, 0], [0, 1], [0, 2]))
        self.__array_equal(adj.connect(
            ([-1, -1], [1, 1])), ([-1, -1], [0, -1], [1, -1], [1, 0], [1, 1]))
        self.__array_equal(adj.connect(
            ([1, 1], [-1, -1])), ([1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]))

        # Connect three points.
        self.__array_equal(adj.connect(
            ([-1, -1], [1, 1], [2, 2])), (
                [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [2, 1], [2, 2]))

    def test_rect(self):
        """Tests the rect function."""

        r = adj.rect(np.array([[0, 1]]))
        self.assertTrue(np.array_equal(r[0], [0, 1]))
        self.assertTrue(np.array_equal(r[1], [0, 1]))

        r = adj.rect(adj.connect(([0, 0], [2, 2], [-1, 1], [-2, 3])))
        self.assertTrue(np.array_equal(r[0], [-2, 0]))
        self.assertTrue(np.array_equal(r[1], [2, 3]))
