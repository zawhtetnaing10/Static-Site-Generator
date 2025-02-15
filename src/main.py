from textnode import TextNode
from textnode import TextType
from text_to_textnodes import text_to_textnodes
import re


def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    result = text_to_textnodes(text)

    formatted_result = "\n".join(list(map(lambda x: f"{x}", result)))
    print(f"Result ====> {formatted_result}")


main()
