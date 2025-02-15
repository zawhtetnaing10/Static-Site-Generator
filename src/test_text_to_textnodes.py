import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode
from textnode import TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_all_types_of_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        correct_output = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGES,
                     "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(text_to_textnodes(text), correct_output)

    def test_only_bold(self):
        text = "This is **bold text**. There's nothing else"
        correct_output = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD_TEXT),
            TextNode(". There's nothing else", TextType.TEXT)
        ]
        self.assertListEqual(text_to_textnodes(text), correct_output)

    def test_only_bold_and_italic(self):
        text = "This is a **bold text**. This is an *italic text*. Thats all."
        correct_output = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD_TEXT),
            TextNode(". This is an ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC_TEXT),
            TextNode(". Thats all.", TextType.TEXT)
        ]
        self.assertListEqual(text_to_textnodes(text), correct_output)

    def test_only_bold_italic_and_code(self):
        text = "This is a **bold text**. This is an *italic text*. This is `THE CODE`. This is `ANOTHER BIG CODE`"
        correct_output = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD_TEXT),
            TextNode(". This is an ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC_TEXT),
            TextNode(". This is ", TextType.TEXT),
            TextNode("THE CODE", TextType.CODE),
            TextNode(". This is ", TextType.TEXT),
            TextNode("ANOTHER BIG CODE", TextType.CODE)
        ]
        self.assertListEqual(text_to_textnodes(text), correct_output)

    def test_only_image(self):
        text = "There's one image. ![image](https://i.imagur.com/adfafa.jpeg)"
        correct_output = [
            TextNode("There's one image. ", TextType.TEXT),
            TextNode("image", text_type=TextType.IMAGES,
                     url="https://i.imagur.com/adfafa.jpeg")
        ]
        self.assertListEqual(text_to_textnodes(text), correct_output)

    def test_only_link(self):
        text = "There's only one link. [to google](https://www.google.com)"
        correct_output = [
            TextNode("There's only one link. ", TextType.TEXT),
            TextNode("to google", TextType.LINK, url="https://www.google.com")
        ]
        self.assertListEqual(text_to_textnodes(text), correct_output)
