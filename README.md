Installation
============

[![Python package](https://img.shields.io/github/actions/workflow/status/chdemko/pandoc-latex-fontsize/python-package.yml?logo=github&branch=develop)](https://github.com/chdemko/pandoc-latex-fontsize/actions/workflows/python-package.yml)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-fontsize/develop.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-latex-fontsize?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-fontsize.svg?logo=scrutinizer)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-fontsize/)
[![Code Climate](https://img.shields.io/codeclimate/maintainability/chdemko/pandoc-latex-fontsize?logo=codeclimate&barnch=develop)](https://codeclimate.com/github/chdemko/pandoc-latex-fontsize/)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/chdemko/pandoc-latex-fontsize/develop.svg?logo=codefactor)](https://www.codefactor.io/repository/github/chdemko/pandoc-latex-fontsize)
[![Codacy](https://img.shields.io/codacy/grade/19a716cec0934fd4be291455aef205d0.svg?logo=codacy)](https://app.codacy.com/gh/chdemko/pandoc-latex-fontsize/dashboard)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-fontsize.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-fontsize/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-fontsize.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-fontsize/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-fontsize.svg?logo=pypi&logoColor=white)](https://raw.githubusercontent.com/chdemko/pandoc-latex-fontsize/develop/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-latex-fontsize?logo=pypi&logoColor=white)](https://pepy.tech/project/pandoc-latex-fontsize)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-fontsize.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-fontsize/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-fontsize.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-latex-fontsize/)
[![Pandoc version](https://img.shields.io/badge/pandoc-2.11%20..%203.6-blue.svg?logo=markdown)](https://pandoc.org/)
[![Latest release](https://img.shields.io/github/release-date/chdemko/pandoc-latex-fontsize.svg?logo=github)](https://github.com/chdemko/pandoc-latex-fontsize/releases)
[![Last commit](https://img.shields.io/github/last-commit/chdemko/pandoc-latex-fontsize/develop?logo=github)](https://github.com/chdemko/pandoc-latex-fontsize/commit/develop/)
[![Repo Size](https://img.shields.io/github/repo-size/chdemko/pandoc-latex-fontsize.svg?logo=github)](http://pandoc-latex-fontsize.readthedocs.io/en/latest/)
[![Code Size](https://img.shields.io/github/languages/code-size/chdemko/pandoc-latex-fontsize.svg?logo=github)](http://pandoc-latex-fontsize.readthedocs.io/en/latest/)
[![Source Rank](https://img.shields.io/librariesio/sourcerank/pypi/pandoc-latex-fontsize.svg?logo=libraries.io&logoColor=white)](https://libraries.io/pypi/pandoc-latex-fontsize)
[![Docs](https://img.shields.io/readthedocs/pandoc-latex-fontsize.svg?logo=read-the-docs&logoColor=white)](http://pandoc-latex-fontsize.readthedocs.io/en/latest/)

*pandoc-latex-fontsize* is a [pandoc] filter for modifying font size to `Code`,
`CodeBlock`, `Span`, and `Div` that have speficied classes or `latex-fontsize`
attribute.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-latex-fontsize* requires [python], a programming language that comes
pre-installed on linux and Mac OS X, and which is easily installed
[on Windows].

Install *pandoc-latex-fontsize* using the bash command

~~~shell-session
$ pipx install pandoc-latex-fontsize
~~~

To upgrade to the most recent release, use

~~~shell-session
$ pipx upgrade pandoc-latex-fontsize
~~~

`pipx` is a script to install and run python applications in isolated environments from the Python Package Index, [PyPI]. It can be installed using instructions given [here](https://pipx.pypa.io/stable/).

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with *pandoc-latex-fontsize*, please feel welcome
to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-fontsize/issues

Contribute
==========

Instructions
------------

Install `hatch`, then run

~~~shell-session
$ hatch run pip install pre-commit
$ hatch run pre-commit install
~~~

to install `pre-commit` before working on your changes.

Tests
-----

When your changes are ready, run

~~~shell-session
$ hatch test
$ hatch fmt --check
$ hatch run lint:check
$ hatch run docs:build
$ hatch build -t wheel
~~~

for running the tests, checking the style, building the documentation
and building the wheel.

