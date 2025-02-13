import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_prop(self):
        html_node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(html_node.props_to_html(),
                         ' href="https://www.google.com"')

    def test_multiple_props(self):
        html_node = HTMLNode(
            props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(html_node.props_to_html(),
                         ' href="https://www.google.com" target="_blank"')

    def test_none_props(self):
        html_node = HTMLNode(tag="h1", value="Welcome")
        self.assertEqual(html_node.props_to_html(), "")

    def test_default_none(self):
        html_node = HTMLNode(tag="h1", value="Welcome")
        self.assertEqual(html_node.tag, "h1")
        self.assertEqual(html_node.value, "Welcome")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)


if __name__ == "__main__":
    unittest.main()
