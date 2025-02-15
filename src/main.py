from textnode import TextNode
from textnode import TextType
from text_to_textnodes import text_to_textnodes
import re
from markdown_to_blocks import markdown_to_blocks


def main():
    text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
    blocks = markdown_to_blocks(text)
    for block in blocks:
        print(block)


main()
