import unittest
from block_to_block_type import BlockType
from block_to_block_type import block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# This is a heading with one #"
        block_2 = "#### This is a heading with multiple #s"

        self.assertEqual(block_to_block_type(block),
                         BlockType.BLOCK_TYPE_HEADING)
        self.assertEqual(block_to_block_type(block_2),
                         BlockType.BLOCK_TYPE_HEADING)

    def test_not_heading(self):
        block = "###kfdj;adfka;fdk"
        block_2 = " # # #not heading"
        self.assertEqual(block_to_block_type(block),
                         BlockType.BLOCK_TYPE_PARAGRAPH)
        self.assertEqual(block_to_block_type(block_2),
                         BlockType.BLOCK_TYPE_PARAGRAPH)

    def test_code(self):
        code = r'```v = 10\nprint(f"{v}")```'
        self.assertEqual(block_to_block_type(code), BlockType.BLOCK_TYPE_CODE)

    def test_not_code(self):
        code = r'``v=567``'
        self.assertEqual(block_to_block_type(
            code), BlockType.BLOCK_TYPE_PARAGRAPH)

    def test_ordered_list(self):
        ordered_list = "1. Wake up\n2. Eat\n3. Sleep\n4. Code"
        self.assertEqual(block_to_block_type(
            ordered_list), BlockType.BLOCK_TYPE_ORDERED_LIST)

    def test_not_ordered_list(self):
        not_ordered_list_1 = "1. Wake up\n45. Work out"
        not_ordered_list_2 = "2. Sleep\n3. Code again"
        not_ordered_list_3 = "This is not an ordered list"
        not_ordered_list_4 = "> This is a quote\n> This is another quote"

        not_ordered_list_array = [
            not_ordered_list_1, not_ordered_list_2, not_ordered_list_3, not_ordered_list_4]

        result = all(block_to_block_type(block) !=
                     BlockType.BLOCK_TYPE_ORDERED_LIST for block in not_ordered_list_array)

        self.assertEqual(result, True)

    def test_quote(self):
        quote_block = "> This is a quote\n> This is another quote"
        self.assertEqual(block_to_block_type(
            quote_block), BlockType.BLOCK_TYPE_QUOTE)

    def test_not_quote(self):
        not_quote = "# This is a heading"
        not_quote_2 = "1. This is not a quote also"
        not_quote_3 = "```v=15```"
        not_quote_4 = "Not a quote. Just a paragraph"

        not_quote_list = [not_quote, not_quote_2, not_quote_3, not_quote_4]

        result = all(block_to_block_type(block) !=
                     BlockType.BLOCK_TYPE_QUOTE for block in not_quote_list)

        self.assertEqual(result, True)

    def test_unordered_list(self):
        unordered_list = "* Beef\n* Chicken\n* Pork"
        unordered_list_2 = "- Cabbage\n- Tomato\n- Lettuce"
        unordered_list_3 = "* single item"

        self.assertEqual(block_to_block_type(
            unordered_list), BlockType.BLOCK_TYPE_UNORDERED_LIST)
        self.assertEqual(block_to_block_type(
            unordered_list_2), BlockType.BLOCK_TYPE_UNORDERED_LIST)
        self.assertEqual(block_to_block_type(
            unordered_list_3), BlockType.BLOCK_TYPE_UNORDERED_LIST)

    def test_not_unordered_list(self):
        not_unordered_list = "* Beef.\n*Chicken"
        not_unordered_list_2 = "- Beef.\n-Chicken"
        not_unordered_list_3 = "* Tomato\n***Apple"
        not_unordered_list_4 = ">>>Not an unordered list"

        not_unordered_list_array = [
            not_unordered_list, not_unordered_list_2, not_unordered_list_3, not_unordered_list_4]

        result = all(block_to_block_type(
            block) != BlockType.BLOCK_TYPE_UNORDERED_LIST for block in not_unordered_list_array)
        self.assertEqual(result, True)

    def test_paragraph(self):
        paragraph = "This is a paragraph. The story continues"
        self.assertEqual(block_to_block_type(paragraph),
                         BlockType.BLOCK_TYPE_PARAGRAPH)
