from textnode import TextNode
from textnode import TextType
from text_to_textnodes import text_to_textnodes
import re
from markdown_to_blocks import markdown_to_blocks

from block_to_block_type import are_orders_correct
from markdown_to_html import markdown_to_html


def main():
    markdown = """
# This is a **bold heading**. This one is *italic* as well. This is an image. ![image in heading](https://www.gstatic.com/webp/gallery/4.sm.jpg)

>This is a quote.

* This is a the first item
* This is the second item
- This is the third item

1. This is the first ordered item
2. This is the second ordered item

```v=10print(v)```

This is a paragraph. Nothing more.
"""
    print(markdown_to_html(markdown))


main()
