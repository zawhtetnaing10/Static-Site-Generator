from leafnode import LeafNode
import unittest


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf_node = LeafNode("Click me!", tag="a", props={
                             "href": "https://www.google.com"})
        self.assertEqual(leaf_node.to_html(),
                         '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_multiple_props(self):
        leaf_node = LeafNode("Click", tag="a", props={
                             "href": "https://www.bootdev.com", "target": "_blank"})
        self.assertEqual(leaf_node.to_html(
        ), '<a href="https://www.bootdev.com" target="_blank">Click</a>')

    def test_to_html_no_props(self):
        leaf_node = LeafNode("Hello", tag="h1")
        self.assertEqual(leaf_node.to_html(), "<h1>Hello</h1>")
