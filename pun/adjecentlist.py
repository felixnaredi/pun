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


"""Functions that are to be applied on lists of adjacent points. Diagonal
adjecency is not accounted for.
"""

from functools import reduce
import numpy as np


def connect(points):
    """Connect all points in list. If two points are not adjecent points will
    first be added along the y-axis and then the x-axis.

    The connected points will be in the same order as the argument with maybe
    additional points in between.
    """

    if len(points) < 2:
        return [np.array(points[0])]

    ps = []

    for (fst, snd) in zip(points[:-1], points[1:]):
        (fy, fx) = fst
        (sy, sx) = snd

        if sy - fy != 0:
            for y in range(fy, sy, np.sign(sy - fy)):
                ps.append(np.array([y, fx]))
        if sx - fx != 0:
            for x in range(fx, sx, np.sign(sx - fx)):
                ps.append(np.array([sy, x]))

    ps.append(np.array(points[-1]))
    return ps


def preppend(points, point, keep_length=False):
    """Prepends point to the list. If it is not adjecent it will be connected.

    If keep_length is True the new list will have the same length as points.
    """

    ps = connect((point, points[0]))
    ps += points[1:]

    if keep_length:
        return ps[:len(points)]
    return ps


def rect(points):
    """Returns a matrix of two points that covers the area of the points in the
    argument.
    """

    return np.array([
        reduce(lambda p, q: q if p is None else np.minimum(p, q), points, None),
        reduce(lambda p, q: q if p is None else np.maximum(p, q), points, None)])
