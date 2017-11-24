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
                        'size': {
                            't': 'MetaInlines',
                            'c': [
                                {
                                    't': 'Str',
                                    'c': 'LARGE'
                                }
                            ]
                        }
                    }
                }
            ]
        }
    }

    dest = pandoc_latex_fontsize.fontsize(src['t'], src['c'], 'latex', meta)
    assert src['c'][1][0]['c'][0] == 'tex'

