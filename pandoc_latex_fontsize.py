#!/usr/bin/env python

"""
Pandoc filter for changing font size in LaTeX.
"""

from panflute import (
    Code,
    CodeBlock,
    Div,
    RawBlock,
    RawInline,
    Span,
    debug,
    run_filter,
)


def latex_code(size):
    """
    Get LaTeX code for size.

    Arguments
    ---------
    size
        The size name.

    Returns
    -------
        LaTeX code for size.
    """
    return "\\" + size + " "


def get_correct_size(size):
    """
    Get correct size.

    Arguments
    ---------
    size
        The size name.

    Returns
    -------
        The correct size.
    """
    if size in (
        "Huge",
        "huge",
        "LARGE",
        "Large",
        "large",
        "normalsize",
        "small",
        "footnotesize",
        "scriptsize",
        "tiny",
    ):
        return size
    debug(
        "[WARNING] pandoc-latex-fontsize: "
        + size
        + " is not a correct LaTeX size; using normalsize"
    )
    return "normalsize"


def add_latex(elem, latex):
    """
    Add LaTeX code to elem.

    Arguments
    ---------
    elem
        A pandoc element
    latex
        A LaTeX code

    Returns
    -------
        A list of pandoc elements or None
    """
    # Is it a Span?
    if isinstance(elem, Span):
        elem.content.insert(0, RawInline(latex, "tex"))

    # Is it a Div?
    elif isinstance(elem, Div):
        elem.content.insert(0, RawBlock("{" + latex, "tex"))
        elem.content.append(RawBlock("}", "tex"))

    # Is it a Code?
    elif isinstance(elem, Code):  # noqa: R505
        return [RawInline("{" + latex, "tex"), elem, RawInline("}", "tex")]

    # Is it a CodeBlock?
    elif isinstance(elem, CodeBlock):
        return [RawBlock("{" + latex, "tex"), elem, RawBlock("}", "tex")]

    return None


def fontsize(elem, doc):
    """
    Generate fontsize for elem.

    Arguments
    ---------
    elem
        A pandoc element
    doc
        The pandoc document

    Returns
    -------
        A list of pandoc elements or None
    """
    # Is it in the right format and is it a Span, Div, Code or CodeBlock?
    if doc.format in ("latex", "beamer") and elem.tag in (
        "Span",
        "Div",
        "Code",
        "CodeBlock",
    ):
        # Is there a latex-fontsize attribute?
        if "latex-fontsize" in elem.attributes:
            return add_latex(
                elem, latex_code(get_correct_size(elem.attributes["latex-fontsize"]))
            )
        # Get the classes
        classes = set(elem.classes)

        # Loop on all fontsize definition
        for definition in doc.defined:
            # Are the classes correct?
            if classes >= definition["classes"]:
                return add_latex(elem, definition["latex"])

    return None


def prepare(doc):
    """
    Prepare the doc.

    Arguments
    ---------
    doc
        The pandoc document
    """
    # Prepare the definitions
    doc.defined = []

    # Get the meta data
    meta = doc.get_metadata("pandoc-latex-fontsize")

    if isinstance(meta, list):
        # Loop on all definitions
        for definition in meta:
            # Verify the definition
            if (
                isinstance(definition, dict)
                and "classes" in definition
                and isinstance(definition["classes"], list)
            ):
                add_definition(doc.defined, definition)


def add_definition(defined, definition):
    """
    Add definition to doc.

    Arguments
    ---------
    defined
        A list of definition
    definition
        A new definition
    """
    # Get the classes
    classes = definition["classes"]

    # Get the size
    if "size" in definition:
        size = get_correct_size(definition["size"])
    else:
        debug("[WARNING] pandoc-latex-fontsize: size is not defined; using normalsize")
        size = "normalsize"

    # Add a definition
    defined.append({"classes": set(classes), "latex": latex_code(size)})


def main(doc=None):
    """
    Convert the pandoc document.

    Arguments
    ---------
    doc
        The pandoc document.

    Returns
    -------
        The modified document.
    """
    return run_filter(fontsize, prepare=prepare, doc=doc)


if __name__ == "__main__":
    main()
