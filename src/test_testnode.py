import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq_different_text_type(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq_none_url(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT)
        node2 = TextNode("This is a text node",
                         TextType.TEXT, "https://www.boodev.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_text(self):
        node = TextNode("This is an italic text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq_different_urls(self):
        node = TextNode("This is a text node",
                        TextType.TEXT, "https://www.bootdev.com")
        node2 = TextNode("This is a text node",
                         TextType.TEXT, "https://www.google.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
