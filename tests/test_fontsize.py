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

def test_span():
    elem = Span(classes=['class1', 'class2'])
    doc = Doc(Para(elem), metadata=metadata(), format='latex', api_version=(1, 17, 2))

    pandoc_latex_fontsize.main(doc)

    assert isinstance(elem.content[0], RawInline)
    assert elem.content[0].format == 'tex'
    assert elem.content[0].text == '\\LARGE '

def test_div():
    elem = Div(classes=['class1', 'class2'])
    doc = Doc( elem, metadata=metadata(), format='latex', api_version=(1, 17, 2))

    pandoc_latex_fontsize.main(doc)

    assert isinstance(elem.content[0], RawBlock)
    assert elem.content[0].format == 'tex'
    assert elem.content[0].text == '{\\LARGE '
    assert isinstance(elem.content[0], RawBlock)
    assert elem.content[1].format == 'tex'
    assert elem.content[1].text == '}'

def test_code():
    elem = Code('', classes=['class1', 'class2'])
    doc = Doc(Para(elem),  metadata=metadata(), format='latex', api_version=(1, 17, 2))

    pandoc_latex_fontsize.main(doc)

    assert isinstance(doc.content[0].content[0], RawInline)
    assert doc.content[0].content[0].format == 'tex'
    assert doc.content[0].content[0].text == '{\\LARGE '
    assert isinstance(doc.content[0].content[2], RawInline)
    assert doc.content[0].content[2].format == 'tex'
    assert doc.content[0].content[2].text == '}'

def test_codeblock():
    elem = CodeBlock('', classes=['class1', 'class2'])
    doc = Doc( elem, metadata=metadata(), format='latex', api_version=(1, 17, 2))

    pandoc_latex_fontsize.main(doc)

    assert isinstance(doc.content[0], RawBlock)
    assert doc.content[0].format == 'tex'
    assert doc.content[0].text == '{\\LARGE '
    assert isinstance(doc.content[2], RawBlock)
    assert doc.content[2].format == 'tex'
    assert doc.content[2].text == '}'

