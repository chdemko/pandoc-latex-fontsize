# pandoc-latex-fontsize
[![Build Status](https://img.shields.io/travis/chdemko/pandoc-latex-fontsize/1.1.1.svg)](https://travis-ci.org/chdemko/pandoc-latex-fontsize/branches)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-fontsize/1.1.1.svg)](https://coveralls.io/github/chdemko/pandoc-latex-fontsize?branch=1.1.1)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-fontsize.svg)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-fontsize/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-fontsize.svg)](https://pypi.org/project/pandoc-latex-fontsize/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-fontsize/1.1.1.svg)](https://pypi.org/project/pandoc-latex-fontsize/1.1.1/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-fontsize/1.1.1.svg)](https://raw.githubusercontent.com/chdemko/pandoc-latex-fontsize/1.1.1/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-latex-fontsize.svg)](https://pypi.org/project/pandoc-latex-fontsize/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-fontsize.svg)](https://pypi.org/project/pandoc-latex-fontsize/)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-fontsize.svg)](https://pypi.org/project/pandoc-latex-fontsize/)

*pandoc-latex-fontsize* is a [pandoc] filter for modifying font size to `Code`, `CodeBlock`, `Span`, and `Div` that have speficied classes or `latex-fontsize` attribute.

[pandoc]: http://pandoc.org/

Documentation
-------------

See the [wiki pages](https://github.com/chdemko/pandoc-latex-fontsize/wiki).

Usage
-----

To apply the filter, use the following option with pandoc:

    --filter pandoc-latex-fontsize

Installation
------------

*pandoc-latex-fontsize* requires [python], a programming language that comes pre-installed on linux and Mac OS X, and which is easily installed [on Windows]. Either python 2.7 or 3.x will do.

Install *pandoc-latex-fontsize* as root using the bash command

    pip install pandoc-latex-fontsize

To upgrade to the most recent release, use

    pip install --upgrade pandoc-latex-fontsize

`pip` is a script that downloads and installs modules from the Python Package Index, [PyPI].  It should come installed with your python distribution. If you are running linux, `pip` may be bundled separately. On a Debian-based system (including Ubuntu), you can install it as root using

    apt-get update
    apt-get install python-pip

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with *pandoc-latex-fontsize*, please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-fontsize/issues

