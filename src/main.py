from textnode import TextNode
from textnode import TextType
from split_nodes_delimiter import split_nodes_delimiter


def main():
    text_node = TextNode(
        text="This is a **bold text**. I'm off. This is an *italic text*. This is **another bold text**. This is `The CODE`.", text_type=TextType.TEXT)
    another_text_node = TextNode(
        text="Another text node with `THE CODE AGAIN`", text_type=TextType.TEXT)
    input = [text_node, another_text_node]

    delimiters = {"**": TextType.BOLD_TEXT,
                  "*": TextType.ITALIC_TEXT, "`": TextType.CODE}
    result = []

    for delimiter_key in delimiters:
        result = split_nodes_delimiter(
            input, delimiter_key, delimiters[delimiter_key])
    print(f"Final result =====> {result}")


main()
