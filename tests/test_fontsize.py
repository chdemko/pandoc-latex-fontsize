# This Python file uses the following encoding: utf-8
from unittest import TestCase
from pandocfilters import Para, Str, Space, Span, Strong, RawInline, Emph, Header

import pandoc_latex_fontsize

def test_fontsize():

    src = Span(['', ['class1', 'class2'], []], [])
    meta = {
        'pandoc-latex-fontsize': {
            't': 'MetaList',
            'c': [
                {
                    't': 'MetaMap',
                    'c': {
                        'classes': {
                            't': 'MetaList',
                            'c': [
                                {
                                    't': 'MetaInlines',
                                    'c': [
                                        {
                                            't': 'Str',
                                            'c': 'class1'
                                        }
                                    ]
                                },
                                {
                                    't': 'MetaInlines',
                                    'c': [
                                        {
                                            't': 'Str',
                                            'c': 'class2'
                                        }
                                    ]
                                }
                            ]
                        },
                    }
                }
            ]
        }
    }


    dest = pandoc_latex_fontsize.fontsize(src['t'], src['c'], 'latex', meta)
    assert isinstance(dest, list)
    assert len(dest) == 3
    assert dest[0]['t'] == 'RawInline'
    assert dest[2]['t'] == 'RawInline'

