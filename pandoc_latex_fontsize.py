#!/usr/bin/env python

"""
Pandoc filter for changing font size in LaTeX
"""

from pandocfilters import RawInline, RawBlock, Span, Code, CodeBlock, stringify, toJSONFilters

def fontsize(key, value, format, meta):
    # Is it a Span and the right format?
    if key in ['Span', 'Div', 'Code', 'CodeBlock'] and format == 'latex':

        # Get the attributes
        [[id, classes, properties], content] = value

        # Use the Span classes as a set
        currentClasses = set(classes)

        # Loop on all fontsize definition
        for elt in getDefined(meta):

            # Is the classes correct?
            if currentClasses >= elt['classes']:

                # Prepend a tex block for inserting fontsize
                if key == 'Span':
                    content.insert(0, RawInline('tex', elt['latex']))
                elif key == 'Div':
                    content.insert(0, RawBlock('tex', '{' + elt['latex']))
                    content.append(RawBlock('tex', '}'))
                elif key == 'CodeBlock':
                    return [
                        RawBlock('tex', '{' + elt['latex']),
                        CodeBlock([id, classes, properties], content),
                        RawBlock('tex', '}')
                    ]
                else: # Code case
                    return [
                        RawInline('tex', '{' + elt['latex']),
                        Code([id, classes, properties], content),
                        RawInline('tex', '}')
                    ]
                    

def getDefined(meta):
    if not hasattr(getDefined, 'value'):
        # Prepare the values
        getDefined.value = []

        # Get the meta data
        if 'pandoc-latex-fontsize' in meta and meta['pandoc-latex-fontsize']['t'] == 'MetaList':
            fontMeta = meta['pandoc-latex-fontsize']['c']

            # Loop on all definitions
            for definition in fontMeta:

                # Verify the definition type
                if definition['t'] == 'MetaMap':

                     # Get the classes
                    classes = []
                    if 'classes' in definition['c'] and definition['c']['classes']['t'] == 'MetaList':
                        for klass in definition['c']['classes']['c']:
                            classes.append(stringify(klass))

                    # Get the size
                    size = 'normalsize'

                    # Test the size definition
                    if 'size' in definition['c'] and definition['c']['size']['t'] == 'MetaInlines':
                        newsize = stringify(definition['c']['size']['c'])
                        if newsize in ['Huge', 'huge', 'LARGE', 'Large', 'large', 'normalsize', 'small', 'footnotesize', 'scriptsize', 'tiny']:
                            size = newsize

                    # Add a definition if correct
                    if bool(classes) and bool(size):
                        getDefined.value.append({'classes' : set(classes), 'latex': '\\' + size + ' '})

    return getDefined.value

def main():
    toJSONFilters([fontsize])

if __name__ == '__main__':
    main()

