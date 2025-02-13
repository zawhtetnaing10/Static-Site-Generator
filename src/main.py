from textnode import TextNode
from textnode import TextType
from leafnode import LeafNode
from parentnode import ParentNode


def main():
    # textnode = TextNode("This is a text node",
    #                     TextType.BOLD_TEXT, "https://www.boot.dev")
    # print(textnode)

    # leaf_node = LeafNode(tag="a", value="Click me!")
    # print(leaf_node)

    parent_node = ParentNode(
        "p",
        [
            ParentNode("div", [
                LeafNode("Hello this is a div", tag="p"),
                LeafNode("Click me here", tag="a", props={
                         "href": "https://www.google.com"})
            ], props={"id": "_inner"}),
            LeafNode("Bold text", tag="b"),
            LeafNode("Normal text", tag=None),
            LeafNode("italic text", tag="i"),
            LeafNode("Normal text", tag=None),
        ],
    )
    print(parent_node.to_html())


main()
