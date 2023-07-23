# This Python file uses the following encoding: utf-8

from unittest import TestCase
from panflute import (
    Code,
    CodeBlock,
    Div,
    Doc,
    MetaList,
    MetaMap,
    MetaString,
    Para,
    RawBlock,
    RawInline,
    Span,
)

import pandoc_latex_fontsize


class FontSizeTest(TestCase):
    def metadata(self):
        return {
            "pandoc-latex-fontsize": MetaList(
                MetaMap(
                    size=MetaString("LARGE"),
                    classes=MetaList(MetaString("class1"), MetaString("class2")),
                )
            )
        }

    def opening(self, value, type):
        self.assertIsInstance(value, type)
        self.assertEqual(value.format, "tex")
        self.assertEqual(value.text, "{\\LARGE ")

    def closing(self, value, type):
        self.assertIsInstance(value, type)
        self.assertEqual(value.format, "tex")
        self.assertEqual(value.text, "}")

    def span(self, elem, doc, size):
        pandoc_latex_fontsize.main(doc)
        self.assertIsInstance(elem.content[0], RawInline)
        self.assertEqual(elem.content[0].format, "tex")
        self.assertEqual(elem.content[0].text, "\\" + size + " ")

    def test_span_classes(self):
        elem = Span(classes=["class1", "class2"])
        doc = Doc(Para(elem), metadata=self.metadata(), format="latex")
        self.span(elem, doc, doc.get_metadata()["pandoc-latex-fontsize"][0]["size"])

    def test_span_attributes(self):
        elem = Span(attributes={"latex-fontsize": "LARGE"})
        doc = Doc(Para(elem), format="latex")
        self.span(elem, doc, "LARGE")

    def div(self, elem, doc):
        pandoc_latex_fontsize.main(doc)
        self.opening(elem.content[0], RawBlock)
        self.closing(elem.content[1], RawBlock)

    def test_div_classes(self):
        elem = Div(classes=["class1", "class2"])
        doc = Doc(elem, metadata=self.metadata(), format="latex")
        self.div(elem, doc)

    def test_div_attributes(self):
        elem = Div(attributes={"latex-fontsize": "LARGE"})
        doc = Doc(elem, format="latex")
        self.div(elem, doc)

    def code(self, elem, doc):
        pandoc_latex_fontsize.main(doc)
        self.opening(doc.content[0].content[0], RawInline)
        self.closing(doc.content[0].content[2], RawInline)

    def test_code_classes(self):
        elem = Code("", classes=["class1", "class2"])
        doc = Doc(Para(elem), metadata=self.metadata(), format="latex")
        self.code(elem, doc)

    def test_code_attributes(self):
        elem = Code("", attributes={"latex-fontsize": "LARGE"})
        doc = Doc(Para(elem), format="latex")
        self.code(elem, doc)

    def codeblock(self, elem, doc):
        pandoc_latex_fontsize.main(doc)
        self.opening(doc.content[0], RawBlock)
        self.closing(doc.content[2], RawBlock)

    def test_codeblock_classes(self):
        elem = CodeBlock("", classes=["class1", "class2"])
        doc = Doc(elem, metadata=self.metadata(), format="latex")
        self.codeblock(elem, doc)

    def test_codeblock_attributes(self):
        elem = CodeBlock("", attributes={"latex-fontsize": "LARGE"})
        doc = Doc(elem, format="latex")
        self.codeblock(elem, doc)

    def test_bad_size(self):
        metadata = {
            "pandoc-latex-fontsize": MetaList(
                MetaMap(
                    size=MetaString("BADSIZE"),
                    classes=MetaList(MetaString("class1"), MetaString("class2")),
                )
            )
        }
        elem = Span(classes=["class1", "class2"])
        doc = Doc(Para(elem), metadata=metadata, format="latex")
        pandoc_latex_fontsize.main(doc)
        self.assertIsInstance(elem.content[0], RawInline)
        self.assertEqual(elem.content[0].format, "tex")
        self.assertEqual(elem.content[0].text, "\\normalsize ")

    def test_missing_size(self):
        metadata = {
            "pandoc-latex-fontsize": MetaList(
                MetaMap(classes=MetaList(MetaString("class1"), MetaString("class2")))
            )
        }
        elem = Span(classes=["class1", "class2"])
        doc = Doc(Para(elem), metadata=metadata, format="latex")
        self.span(elem, doc, "normalsize")
