#!/usr/bin/env python

# Copyright (c) 2011 Chris Howie
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
from PyQRNative import QRCode, QRErrorCorrectLevel

try:
    text = sys.argv[1]
except:
    print('Usage: python', sys.argv[0], 'content')
    sys.exit(1)

levels = [17, 32, 53, 78, 106, 134, 154, 192, 230, 271]
level = None

for i in zip(list(range(1, 11)), levels):
    if len(text) <= i[1]:
        level = i[0]
        break

if level is None:
    print('Content too long (271 characters maximum).')
    sys.exit(1)

qr = QRCode(level, QRErrorCorrectLevel.L)
qr.addData(text)
qr.make()

dark = '  '
light = u'\u2588\u2588'

width = qr.moduleCount

for i in range(4):
    print(light * (qr.moduleCount + 8))

for y in range(qr.moduleCount):
    row = light * 4

    for x in range(qr.moduleCount):
        row += dark if qr.isDark(y, x) else light

    row += light * 4
    print(row)

for i in range(4):
    print(light * (qr.moduleCount + 8))

