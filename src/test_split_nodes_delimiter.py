import unittest
from textnode import TextNode
from textnode import TextType
from split_nodes_delimiter import split_nodes_delimiter

DELIMITERS = {"**": TextType.BOLD_TEXT,
              "*": TextType.ITALIC_TEXT, "`": TextType.CODE}


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_bold(self):
        text_node = TextNode(
            text="This is a **bold text**. Let's go", text_type=TextType.TEXT)
        input = [text_node]

        result = split_nodes_delimiter(input, "**", TextType.BOLD_TEXT)
        correct_nodes = [TextNode(text="This is a ", text_type=TextType.TEXT), TextNode(
            text="bold text", text_type=TextType.BOLD_TEXT), TextNode(text=". Let's go", text_type=TextType.TEXT)]

        self.assertListEqual(result, correct_nodes)

    def test_italic(self):
        input = [TextNode(
            text="This is an *italic text*. It looks better", text_type=TextType.TEXT)]
        result = split_nodes_delimiter(input, "*", TextType.ITALIC_TEXT)
        correct_nodes = [TextNode(text="This is an ", text_type=TextType.TEXT), TextNode(
            text="italic text", text_type=TextType.ITALIC_TEXT), TextNode(text=". It looks better", text_type=TextType.TEXT)]
        self.assertListEqual(result, correct_nodes)

    def test_code(self):
        input = [TextNode(text="This is `code`", text_type=TextType.TEXT)]
        result = split_nodes_delimiter(input, "`", TextType.CODE)
        correct_nodes = [TextNode(text="This is ", text_type=TextType.TEXT), TextNode(
            text="code", text_type=TextType.CODE)]
        self.assertListEqual(result, correct_nodes)

    def test_bold_italic_and_code(self):
        text_node = TextNode(
            text="This is a **bold text**. I'm off. This is an *italic text*. This is **another bold text**. This is `The CODE`.", text_type=TextType.TEXT)
        another_text_node = TextNode(
            text="Another text node with `THE CODE AGAIN`", text_type=TextType.TEXT)
        input = [text_node, another_text_node]

        result = []

        for delimiter_key in DELIMITERS:
            result = split_nodes_delimiter(
                input, delimiter_key, DELIMITERS[delimiter_key])

        correct_result = "[TextNode(This is a ,Normal Text,None), TextNode(bold text,Bold Text,None), TextNode(. I'm off. This is an ,Normal Text,None), TextNode(italic text,Italic Text,None), TextNode(. This is ,Normal Text,None), TextNode(another bold text,Bold Text,None), TextNode(. This is ,Normal Text,None), TextNode(The CODE,Code,None), TextNode(.,Normal Text,None), TextNode(Another text node with ,Normal Text,None), TextNode(THE CODE AGAIN,Code,None)]"

        self.assertEqual(f"{result}", correct_result)

    def test_error_without_closing_delimiter(self):
        text_node = TextNode(text="**", text_type=TextType.TEXT)
        input = [text_node]

        with self.assertRaises(Exception) as context:
            for delimiter_key in DELIMITERS:
                split_nodes_delimiter(
                    input, delimiter_key, DELIMITERS[delimiter_key])

            self.assertEqual(context.exception, Exception(
                "No matching end delimiter found"))
