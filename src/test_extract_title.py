import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = """
# This is the title

### This is the second title

#### This is the third title

> This is a quote
"""
        title = extract_title(markdown)
        self.assertEqual(title, "This is the title")

    def test_extract_title_2(self):
        markdown = "# This is the only title"
        title = extract_title(markdown)
        self.assertEqual(title, "This is the only title")
