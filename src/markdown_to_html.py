import re
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import BlockType
from block_to_block_type import block_to_block_type
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node

HEADING_AND_TAGS = {"# ": "h1", "## ": "h2", "### ": "h3",
                    "#### ": "h4", "##### ": "h5", "###### ": "h6"}


def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = list(map(lambda block: block_to_html(block), blocks))
    result = ParentNode("div", children=html_nodes)
    return result


def block_to_html(block):
    block_type = block_to_block_type(block)

    match block_type:
        case BlockType.BLOCK_TYPE_HEADING:
            return convert_heading_block_to_html_node(block)
        case BlockType.BLOCK_TYPE_QUOTE:
            return convert_quote_block_to_html_node(block)
        case BlockType.BLOCK_TYPE_UNORDERED_LIST:
            return convert_unordered_list_block_to_html_node(block)
        case BlockType.BLOCK_TYPE_ORDERED_LIST:
            return convert_ordered_list_block_to_html_node(block)
        case BlockType.BLOCK_TYPE_CODE:
            return convert_code_block_to_html_node(block)
        case BlockType.BLOCK_TYPE_PARAGRAPH:
            return convert_paragraph_block_to_html_node(block)
        case _:
            raise ValueError("invalid block type")


def convert_heading_block_to_html_node(block):
    tag = ""
    matching_key = ""
    for key in HEADING_AND_TAGS:
        if block.startswith(key):
            matching_key = key
            tag = HEADING_AND_TAGS[key]
    block_to_convert = block.replace(matching_key, "")
    children = text_to_children(block_to_convert)
    return ParentNode(tag=tag, children=children)


def convert_quote_block_to_html_node(block):
    tag = "blockquote"
    block_to_convert = block.replace(">", "").strip()
    children = text_to_children(block_to_convert)
    return ParentNode(tag=tag, children=children)


def convert_unordered_list_block_to_html_node(block):
    outer_tag = "ul"
    inner_tag = "li"

    lines = block.split("\n")
    line_texts = list(map(lambda line: line.replace(
        "* ", "").replace("- ", "").strip(), lines))
    item_htmls = list(map(lambda line_text: ParentNode(
        inner_tag, children=text_to_children(line_text)), line_texts))
    return ParentNode(outer_tag, children=item_htmls)


def convert_ordered_list_block_to_html_node(block):
    outer_tag = "ol"
    inner_tag = "li"

    lines = block.split("\n")
    line_texts = list(
        map(lambda line: remove_number_prefix(line).strip(), lines))
    item_htmls = list(map(lambda line_text: ParentNode(
        inner_tag, children=text_to_children(line_text)), line_texts))
    return ParentNode(outer_tag, children=item_htmls)


def convert_code_block_to_html_node(block):
    return ParentNode("pre", children=text_to_children(block))


def convert_paragraph_block_to_html_node(block):
    return ParentNode("p", children=text_to_children(block))


def remove_number_prefix(text):
    return re.sub(r"^\d+\.\s*", "", text)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return list(map(lambda text_node: text_node_to_html_node(text_node), text_nodes))
