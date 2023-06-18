# Usage

To apply the filter, use the following option with pandoc:

~~~shell
$ pandoc --filter pandoc-latex-fontsize
~~~

Explanation
-----------

In the metadata block, specific set of classes can be defined to specify the font size for `span`, `code`, `div` and `codeblock` elements.

The metadata block add information using the `pandoc-latex-fontsize` entry by a list of definitions:

~~~
pandoc-latex-fontsize:
  - classes: [smallcontent]
    size: tiny
  - classes: [largecontent, important]
    size: huge
~~~

The metadata block above is used to set the fontsize:

* to `tiny` for `span`, `code`, `div` and `codeblock` elements that have the `smallcontent` class;
* to `huge` for `span`, `code`, `div` and `codeblock` elements that have the `largecontent` and `important` classes;

The font size specified must be either:

* `Huge`
* `huge`
* `LARGE`
* `Large`
* `large`
* `normalsize`
* `small`
* `footnotesize`
* `scriptsize`
* `tiny`

which are the name of LaTeX font sizes.

It's also possible to set a specific LaTeX font size using the `latex-fontsize` attribute.

Example
-------

Demonstration: Using
[pandoc-latex-fontsize-sample.txt](https://raw.githubusercontent.com/chdemko/pandoc-latex-fontsize/develop/docs/images/pandoc-latex-fontsize-sample.txt)
as input gives output file in
[pandoc-beamer-block-sample.pdf](https://raw.githubusercontent.com/chdemko/pandoc-latex-fontsize/develop/docs/images/pandoc-latex-fontsize-sample.pdf).

