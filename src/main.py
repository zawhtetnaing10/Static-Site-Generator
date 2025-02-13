from textnode import TextNode
from textnode import TextType
from leafnode import LeafNode


def main():
    textnode = TextNode("This is a text node",
                        TextType.BOLD_TEXT, "https://www.boot.dev")
    print(textnode)

    leaf_node = LeafNode(tag="a", value="Click me!")
    print(leaf_node)


main()
