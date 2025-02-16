from textnode import TextNode
from textnode import TextType
from text_to_textnodes import text_to_textnodes
import re
from markdown_to_blocks import markdown_to_blocks

from block_to_block_type import are_orders_correct


def main():
    text = "This is not an ordered list"
    print(f"are orders correct ====> {are_orders_correct(text)}")


main()
