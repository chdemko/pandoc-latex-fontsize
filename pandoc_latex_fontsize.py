#!/usr/bin/env python

"""
Pandoc filter for changing font size in LaTeX
"""

from panflute import *

def fontsize(elem, doc):
    # Is it in the right format and is it a Span, Div, Code or CodeBlock?
    if doc.format == 'latex' and elem.tag in ['Span', 'Div', 'Code', 'CodeBlock']:

        # Get the classes
        classes = set(elem.classes)

        # Loop on all fontsize definition
        for definition in doc.defined:

            # Is the classes correct?
            if classes >= definition['classes']:

                # Is it a span?
                if isinstance(elem, Span):
                    elem.content.insert(0, RawInline(definition['latex'], 'tex'))

                # Is it a Div?
                elif isinstance(elem, Div):
                    elem.content.insert(0, RawBlock('{' + definition['latex'], 'tex'))
                    elem.content.append(RawBlock('}', 'tex'))

                # Is it a Code?
                elif isinstance(elem, Code):
                    return [RawInline('{' + definition['latex'], 'tex'), elem, RawInline('}', 'tex')]

                # Is it a CodeBlock?
                elif isinstance(elem, CodeBlock):
                    return [RawBlock('{' + definition['latex'], 'tex'), elem, RawBlock('}', 'tex')]

def prepare(doc):
    # Prepare the definitions
    doc.defined = []

    # Get the meta data
    meta = doc.get_metadata('pandoc-latex-fontsize')

    if isinstance(meta, list):

        # Loop on all definitions
        for definition in meta:

            # Verify the definition type
            if isinstance(definition, dict):

                if 'classes' in definition and isinstance(definition['classes'], list):

                    # Get the classes
                    classes = definition['classes']

                    # Get the size
                    if 'size' in definition and definition['size'] in ['Huge', 'huge', 'LARGE', 'Large', 'large', 'normalsize', 'small', 'footnotesize', 'scriptsize', 'tiny']:
                        size = definition['size']
                    else:
                        size = 'normalsize'

                    # Add a definition
                    doc.defined.append({'classes' : set(classes), 'latex': '\\' + size + ' '})

def main(doc = None):
    run_filter(fontsize, prepare = prepare, doc = doc)

if __name__ == '__main__':
    main()

