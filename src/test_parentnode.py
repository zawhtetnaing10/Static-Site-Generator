from parentnode import ParentNode
from leafnode import LeafNode
import unittest


class TestParentNode(unittest.TestCase):
    def test_to_html_nested_one_level(self):
        parent_node = ParentNode(tag="p", children=[
            LeafNode("This is a text", tag="p"),
            LeafNode("Click me", tag="a", props={
                     "href": "https://www.google.com"}),
            LeafNode("Italic Text", tag="i"),
            LeafNode("Multiple Props", tag="a", props={
                     "href": "https://www.bootdev.com", "target": "_blank"})
        ])
        correct_html = '<p><p>This is a text</p><a href="https://www.google.com">Click me</a><i>Italic Text</i><a href="https://www.bootdev.com" target="_blank">Multiple Props</a></p>'
        self.assertEqual(parent_node.to_html(), correct_html)

    def test_to_html_nested_multiple_levels(self):
        parent_node = ParentNode(tag="p", children=[
            ParentNode("div", children=[
                LeafNode("This is a bold text", tag="b"),
                ParentNode("p", children=[
                    LeafNode("This is a nested paragraph", None)
                ])
            ]),
            LeafNode("This is a text", tag="p"),
            LeafNode("Click me", tag="a", props={
                     "href": "https://www.google.com"}),
            LeafNode("Italic Text", tag="i"),
            LeafNode("Multiple Props", tag="a", props={
                     "href": "https://www.bootdev.com", "target": "_blank"})
        ])
        correct_html = '<p><div><b>This is a bold text</b><p>This is a nested paragraph</p></div><p>This is a text</p><a href="https://www.google.com">Click me</a><i>Italic Text</i><a href="https://www.bootdev.com" target="_blank">Multiple Props</a></p>'
        self.assertEqual(parent_node.to_html(), correct_html)

    def test_to_html_no_children(self):
        parent_node = ParentNode(tag="div", children=[])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_a_child_with_no_children(self):
        parent_node = ParentNode(tag="p", children=[
            ParentNode("div", children=[]),
            LeafNode("This is a text"),
        ])
        correct_html = "<p><div></div>This is a text</p>"
        self.assertEqual(parent_node.to_html(), correct_html)
