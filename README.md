## pypinproc

pypinproc is a native Python extension exposing the [libpinproc](http://github.com/preble/libpinproc) API to Python
programs. pypinproc provides a low-level interface for controlling a Multimorphic [P-ROC or P3-ROC](http://pinballcontrollers.com/)
Pinball Remote Operations Controller from Python.

## Prerequisites

- [Python 2.6, 2.7, 3.4, or 3.5](http://python.org/)
- [FTDI D2XX driver](http://www.ftdichip.com/Drivers/D2XX.htm)

Note that [libpinproc](http://github.com/preble/libpinproc) is required to build pypinproc, but pre-compiled wheels are
available for Mac OS X, 32-bit Windows, and 64-bit Windows which include the pre-compiled libpinproc, so you only need to
download and build libpinproc if you're manually building pypinproc for another platform or version of Python.

Most likely you'll use pypinproc with a higher-level Python-based pinball game framework, such as:

- [pyprocgame](http://www.pinballcontrollers.com/forum/index.php?board=9.0)
- [PyProcGameHD](http://mjocean.github.io/PyProcGameHD-SkeletonGame/)
- [Mission Pinball Framework](https://missionpinball.com/mpf)

## Installation

To install pypinproc (automatically downloads and includes libpinproc)

    pip install pypinproc

Or if you want to build it yourself (requires that you have previously built and installed libpinproc)

	python setup.py install


## Documentation

API documentation for pypinproc can be found in the [pyprocgame documentation](http://pyprocgame.pindev.org/).

## License

The MIT License (MIT)

Copyright (c) 2009-2011 Adam Preble and Gerry Stellenberg

Extended in 2016 to support Python 3 (along with 2) by the Mission Pinball Framework team.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.