import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_three_blocks(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        blocks = markdown_to_blocks(text)
        correct_output = ["# This is a heading",
                          "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                          "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                          ]
        self.assertListEqual(blocks, correct_output)

    def test_two_blocks(self):
        text = """# This is another heading

This is another paragraph. Just a paragraph.
"""
        blocks = markdown_to_blocks(text)
        correct_output = ["# This is another heading",
                          "This is another paragraph. Just a paragraph."]
        self.assertListEqual(blocks, correct_output)

    def test_one_block(self):
        text = "# Only heading here"
        blocks = markdown_to_blocks(text)
        correct_output = ["# Only heading here"]
        self.assertListEqual(blocks, correct_output)
