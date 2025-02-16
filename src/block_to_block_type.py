import re

BLOCK_TYPE_PARAGRAPH = "paragraph"
BLOCK_TYPE_HEADING = "heading"
BLOCK_TYPE_CODE = "code"
BLOCK_TYPE_QUOTE = "quote"
BLOCK_TYPE_UNORDERED_LIST = "unordered_list"
BLOCK_TYPE_ORDERED_LIST = "ordered_list"

REGEX_HEADING = r"^#{1,6} "


def block_to_block_type(block):
    lines = block.split("\n")

    if (re.match(REGEX_HEADING, block)):
        return BLOCK_TYPE_HEADING

    if block.startswith("```") and block.endswith("```"):
        return BLOCK_TYPE_CODE

    if block.startswith("> "):
        return BLOCK_TYPE_QUOTE

    is_unordered_list = all(line.startswith(
        "* ") or line.startswith("- ") for line in lines)
    if is_unordered_list:
        return BLOCK_TYPE_UNORDERED_LIST

    first_line = lines[0]
    if first_line.startswith("1. ") and are_orders_correct(block):
        return BLOCK_TYPE_ORDERED_LIST

    return BLOCK_TYPE_PARAGRAPH


def are_orders_correct(block):
    lines = block.split("\n")

    try:
        order_numbers = list(
            map(lambda line: get_order_number_from_line(line), lines))
    except ValueError:
        return False

    for i in range(0, len(order_numbers) - 1):
        if order_numbers[i + 1] != order_numbers[i] + 1:
            return False

    return True


def get_order_number_from_line(line):
    return int(line.split(".")[0])
