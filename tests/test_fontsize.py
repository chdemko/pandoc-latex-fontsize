# This Python file uses the following encoding: utf-8

from unittest import TestCase
from panflute import *

import pandoc_latex_fontsize

def metadata():
    return {
        'pandoc-latex-fontsize': MetaList(
            MetaMap(
                size=MetaString('LARGE'),
                classes=MetaList(MetaString('class1'), MetaString('class2'))
            )
        )
    }

def opening(value, type):
    assert isinstance(value, type)
    assert value.format == 'tex'
    assert value.text == '{\\LARGE '

def closing(value, type):
    assert isinstance(value, type)
    assert value.format == 'tex'
    assert value.text == '}'

def test_span():
    elem = Span(classes=['class1', 'class2'])
    doc = Doc(Para(elem), metadata=metadata(), format='latex', api_version=(1, 17, 2))

    pandoc_latex_fontsize.main(doc)

    assert isinstance(elem.content[0], RawInline)
    assert elem.content[0].format == 'tex'
    assert elem.content[0].text == '\\LARGE '

def test_div():
    elem = Div(classes=['class1', 'class2'])
    doc = Doc(elem, metadata=metadata(), format='latex', api_version=(1, 17, 2))

    pandoc_latex_fontsize.main(doc)

    opening(elem.content[0], RawBlock)
    closing(elem.content[1], RawBlock)

def test_code():
    elem = Code('', classes=['class1', 'class2'])
    doc = Doc(Para(elem),  metadata=metadata(), format='latex', api_version=(1, 17, 2))

    pandoc_latex_fontsize.main(doc)

    opening(doc.content[0].content[0], RawInline)
    closing(doc.content[0].content[2], RawInline)

def test_codeblock():
    elem = CodeBlock('', classes=['class1', 'class2'])
    doc = Doc(elem, metadata=metadata(), format='latex', api_version=(1, 17, 2))

    pandoc_latex_fontsize.main(doc)

    opening(doc.content[0], RawBlock)
    closing(doc.content[2], RawBlock)

