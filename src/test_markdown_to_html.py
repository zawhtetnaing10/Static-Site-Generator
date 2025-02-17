import unittest
from markdown_to_html import markdown_to_html


class TestMarkdownToHtml(unittest.TestCase):
    def test_mark_down_to_html_one(self):
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
        correct_html = '<div><h1>This is a <b>bold heading</b>. This one is <i>italic</i> as well. This is an image. <img src="https://www.gstatic.com/webp/gallery/4.sm.jpg" alt="image in heading"></img></h1><blockquote>This is a quote.</blockquote><ul><li>This is a the first item</li><li>This is the second item</li><li>This is the third item</li></ul><ol><li>This is the first ordered item</li><li>This is the second ordered item</li></ol><pre><code>v=10print(v)</code></pre><p>This is a paragraph. Nothing more.</p></div>'
        self.assertEqual(markdown_to_html(markdown), correct_html)

    def test_mark_down_to_html_two(self):
        markdown = """
###### This is a **bold heading**.

1. This is the first ordered item
2. This is the second ordered item

This is a paragraph. Nothing more.
"""
        correct_html = "<div><h6>This is a <b>bold heading</b>.</h6><ol><li>This is the first ordered item</li><li>This is the second ordered item</li></ol><p>This is a paragraph. Nothing more.</p></div>"
        self.assertEqual(markdown_to_html(markdown), correct_html)
