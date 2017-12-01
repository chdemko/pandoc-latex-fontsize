#!/usr/bin/env python

"""
Pandoc filter for changing font size in LaTeX
"""

from panflute import *

def latex_code(size):
    return '\\' + size + ' '

def get_correct_size(size):
    if size in ['Huge', 'huge', 'LARGE', 'Large', 'large', 'normalsize', 'small', 'footnotesize', 'scriptsize', 'tiny']:
        return size
    else:
        debug('[WARNING] pandoc-latex-fontsize: ' + size + ' is not a correct LaTeX size; using normalsize')
        return 'normalsize'

def add_latex(elem, latex):
    # Is it a Span?
    if isinstance(elem, Span):
        elem.content.insert(0, RawInline(latex, 'tex'))

    # Is it a Div?
    elif isinstance(elem, Div):
        elem.content.insert(0, RawBlock('{' + latex, 'tex'))
        elem.content.append(RawBlock('}', 'tex'))

    # Is it a Code?
    elif isinstance(elem, Code):
        return [RawInline('{' + latex, 'tex'), elem, RawInline('}', 'tex')]

    # Is it a CodeBlock?
    elif isinstance(elem, CodeBlock):
        return [RawBlock('{' + latex, 'tex'), elem, RawBlock('}', 'tex')]

def fontsize(elem, doc):
    # Is it in the right format and is it a Span, Div, Code or CodeBlock?
    if doc.format == 'latex' and elem.tag in ['Span', 'Div', 'Code', 'CodeBlock']:

        # Is there a latex-fontsize attribute?
        if 'latex-fontsize' in elem.attributes:
            return add_latex(elem, latex_code(get_correct_size(elem.attributes['latex-fontsize'])))
        else:
            # Get the classes
            classes = set(elem.classes)

            # Loop on all fontsize definition
            for definition in doc.defined:

                # Are the classes correct?
                if classes >= definition['classes']:
                    return add_latex(elem, definition['latex'])

def prepare(doc):
    # Prepare the definitions
    doc.defined = []

    # Get the meta data
    meta = doc.get_metadata('pandoc-latex-fontsize')

    if isinstance(meta, list):

        # Loop on all definitions
        for definition in meta:

            # Verify the definition
            if isinstance(definition, dict) and 'classes' in definition and isinstance(definition['classes'], list):
                add_definition(doc.defined, definition)

def add_definition(defined, definition):
    # Get the classes
    classes = definition['classes']

    # Get the size
    if 'size' in definition:
        size = get_correct_size(definition['size'])
    else:
        debug('[WARNING] pandoc-latex-fontsize: size is not defined; using normalsize')
        size = 'normalsize'

    # Add a definition
    defined.append({'classes' : set(classes), 'latex': latex_code(size)})

def main(doc = None):
    run_filter(fontsize, prepare = prepare, doc = doc)

if __name__ == '__main__':
    main()

