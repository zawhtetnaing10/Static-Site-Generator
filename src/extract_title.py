from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    heading_blocks = filter(lambda block: block_to_block_type(block), blocks)

    title_blocks = list(filter(
        lambda heading_block: heading_block.startswith("# "), heading_blocks))
    if not title_blocks:
        raise Exception("there should be a title block")

    title_block = title_blocks[0].replace("# ", "")
    return title_block
