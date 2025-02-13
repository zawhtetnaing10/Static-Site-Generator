import unittest

from textnode import TextNode
from textnode import TextType
from leafnode import LeafNode
from parentnode import ParentNode
from text_node_to_html_node import text_node_to_html_node


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_node_to_html_node_normal(self):
        text_node = TextNode(text="This is a normal text",
                             text_type=TextType.NORMAL_TEXT)
        correct_html = "This is a normal text"
        self.assertEqual(text_node_to_html_node(
            text_node).to_html(), correct_html)

    def test_text_node_to_html_node_bold_and_italic(self):
        bold_node = TextNode(text="This is a bold text",
                             text_type=TextType.BOLD_TEXT)
        italic_node = TextNode(text="This is an italic text",
                               text_type=TextType.ITALIC_TEXT)
        correct_bold_html = "<b>This is a bold text</b>"
        correct_italic_html = "<i>This is an italic text</i>"
        self.assertEqual(text_node_to_html_node(
            bold_node).to_html(), correct_bold_html)
        self.assertEqual(text_node_to_html_node(
            italic_node).to_html(), correct_italic_html)

    def test_text_node_html_node_code(self):
        code_node = TextNode("a,b,c=5,19,34", text_type=TextType.CODE)
        corrct_code_html = "<code>a,b,c=5,19,34</code>"
        self.assertEqual(text_node_to_html_node(
            code_node).to_html(), corrct_code_html)

    def test_text_node_html_node_link(self):
        link_node = TextNode(
            "Click me", text_type=TextType.LINK, url="https://www.google.com")
        correct_link_html = '<a href="https://www.google.com">Click me</a>'
        self.assertEqual(text_node_to_html_node(
            link_node).to_html(), correct_link_html)

    def test_text_node_html_node_image(self):
        image_node = TextNode(
            "This is an image", text_type=TextType.IMAGES, url="https://www.bootdev.com")
        correct_image_html = '<img src="https://www.bootdev.com" alt="This is an image"></img>'
        self.assertEqual(text_node_to_html_node(
            image_node).to_html(), correct_image_html)
