from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        # Early exists
        if self.tag == None:
            return ValueError("tag must be provided")
        if self.children == None:
            return ValueError("child nodes must be provided for a parent node")

        # recursion loop
        result = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            result += f"{child.to_html()}"
        result += f"</{self.tag}>"

        return result
