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

def span(elem, doc):
    pandoc_latex_fontsize.main(doc)
    assert isinstance(elem.content[0], RawInline)
    assert elem.content[0].format == 'tex'
    assert elem.content[0].text == '\\LARGE '

def test_span_classes():
    elem = Span(classes=['class1', 'class2'])
    doc = Doc(Para(elem), metadata=metadata(), format='latex', api_version=(1, 17, 2))
    span(elem, doc)

def test_span_attributes():
    elem = Span(attributes={'latex-fontsize': 'LARGE'})
    doc = Doc(Para(elem), format='latex', api_version=(1, 17, 2))
    span(elem, doc)

def div(elem, doc):
    pandoc_latex_fontsize.main(doc)
    opening(elem.content[0], RawBlock)
    closing(elem.content[1], RawBlock)

def test_div_classes():
    elem = Div(classes=['class1', 'class2'])
    doc = Doc(elem, metadata=metadata(), format='latex', api_version=(1, 17, 2))
    div(elem, doc)

def test_div_attributes():
    elem = Div(attributes={'latex-fontsize': 'LARGE'})
    doc = Doc(elem, format='latex', api_version=(1, 17, 2))
    div(elem, doc)

def code(elem, doc):
    pandoc_latex_fontsize.main(doc)
    opening(doc.content[0].content[0], RawInline)
    closing(doc.content[0].content[2], RawInline)

def test_code_classes():
    elem = Code('', classes=['class1', 'class2'])
    doc = Doc(Para(elem),  metadata=metadata(), format='latex', api_version=(1, 17, 2))
    code(elem, doc)

def test_code_attributes():
    elem = Code('', attributes={'latex-fontsize': 'LARGE'})
    doc = Doc(Para(elem),  format='latex', api_version=(1, 17, 2))
    code(elem, doc)

def codeblock(elem, doc):
    pandoc_latex_fontsize.main(doc)
    opening(doc.content[0], RawBlock)
    closing(doc.content[2], RawBlock)

def test_codeblock_classes():
    elem = CodeBlock('', classes=['class1', 'class2'])
    doc = Doc(elem, metadata=metadata(), format='latex', api_version=(1, 17, 2))
    codeblock(elem, doc)

def test_codeblock_attributes():
    elem = CodeBlock('', attributes={'latex-fontsize': 'LARGE'})
    doc = Doc(elem, format='latex', api_version=(1, 17, 2))
    codeblock(elem, doc)

