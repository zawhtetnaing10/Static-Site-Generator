from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_elements import split_nodes_images
from split_nodes_elements import split_nodes_link
from textnode import TextNode
from textnode import TextType


def text_to_textnodes(text):
    input = [TextNode(text, text_type=TextType.TEXT)]
    splitted_bold = split_nodes_delimiter(input, "**", TextType.BOLD_TEXT)
    splitted_italic = split_nodes_delimiter(
        splitted_bold, "*", TextType.ITALIC_TEXT)
    splitted_code = split_nodes_delimiter(splitted_italic, "`", TextType.CODE)
    splitted_image = split_nodes_images(splitted_code)
    final_result = split_nodes_link(splitted_image)

    return final_result
